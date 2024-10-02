from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class Role(models.TextChoices):
    REGULAR_STAFF = "RS", _("Regular Staff")
    MANAGERIAL_STAFF = "MS", _("Managerial Staff")
    BOARD_OF_MANAGEMENT = "BOM", _("Board of Management")


class Department(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.abbreviation


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for the CustomUser model.

    This manager provides methods for creating and managing custom users.

    Attributes:
        model (CustomUser): The CustomUser model instance.

    Methods:
        create_user(email, password=None, **extra_fields):
            Creates and saves a new custom user with the given email and password.
        create_superuser(email, password=None, **extra_fields):
            Creates and saves a new custom superuser with the given email and password.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", Role.REGULAR_STAFF)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.

    This model represents a user in the system, with additional fields for first name, last name, age, and email address.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        age (int): The user's age.
        email (str): The user's email address.
        pf_number (str): The user's personnel file number.
        job_title (str): The user's job title.
        department (Department): The user's department.
        date_hired (datetime): The user's date hired.
        is_staff (bool): Whether the user is a staff member.
        is_active (bool): Whether the user is active.
        role (str): The user's role.
        date_joined (datetime): The date the user joined the system.

    Note:
        The email address is used as the unique identifier for the user.
    """

    objects = CustomUserManager()

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    age = models.IntegerField(_("age"), default=0)
    email = models.EmailField(_("email address"), unique=True)

    pf_number = models.CharField(
        _("personnel file number"), max_length=20, unique=True, blank=True, null=True
    )
    job_title = models.CharField(_("job title"), max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_hired = models.DateField(_("date hired"), blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    role = models.CharField(
        max_length=5,
        choices=Role.choices,
        default=Role.REGULAR_STAFF,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def years_of_service(self) -> int:
        return datetime.now().year - self.date_hired.year

    def __str__(self):
        return f"{self.full_name} - {self.job_title}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
