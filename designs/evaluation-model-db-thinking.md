## What is this?
Here I try to look at how the current Excel file used for perfomance evaluation is structured and how this can transfer into Django models and views.

## The current situation
### Scoring
The Excel file used for appraisal as of the writing of this is made up of various sections each allowing staff make comments and score themselves. The scores go from 0.00 to 5.00.    
Managers can then add comments and scores alongside the staff's score. They can do this only for staff they supervise.    
The scores are as follow:
* Development required / Poor role fit: 0 - 1.29
* Improvement required: 1.3 - 2.54
* Achieved: 2.55 - 4.29
* Exceptional: 4.3 - 4.79
* Distinguished: 4.8 - 5.00    

There is a final percentage score calculated for each section that uses this formula in the Excel sheet: `=(SUM(M29:M36)/(COUNT(M29:M36,"<>0")*5)*20/100)`.    
The score is calculated for both the manager's scores and the staff's scores. The resultant scores are a percentage.    
The scores are rated as:
* Development required / Poor role fit: 0 - 49%
* Improvement required: 50 - 69%
* Achieved: 70 - 85%
* Exceptional: 86 - 100%
* Distinguished: above 100%

### Sections
The sections and what they need submitted are:

**Section 1: Review Key Perfomance Indicators**

These are you previous years goals. The fields to fill in are:
* Goal - text
* KPI - On hold, ongoing or achieved with a comment from the user should include percentages if possible
* Staff comments - The staff's comment
* Staff score - The score the staff has given themselves
* Supervisor comment - The supervisor's comment on the goal
* Manager score - The supervisor's score on the goal

