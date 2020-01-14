# Classify Support Tickets 
Classify support tickets depending of text in the ticket, the model classifies the ticket in 2 categories

### Assumptions
These are the categories to classify the tickets in 2 levels: Level 1 with 7 categories and each of them with subcategories

|1 Account Management | 2 Application Error  | 3 Service Request |
|---------------------|----------------------|-------------------|
|  - Access Request   |   - App Error        |   - Request       |
|  - Account Update   |   - App Functionality|  - Enhancement    |
|  - Login Issue      |   - App Down         |   - Configuration |
  

|4 Integrations    | 5 Alert Monitoring  | 6 Data Error      |7 Infrastructure   |
|------------------|---------------------|-------------------|-------------------|
|  - Job           |   - Alert DB        |   - Data Issue    |  - Infrastructure |
|  - File Transfer |   - Alert App       |  - Report Issue   |  - DB Related     |
|  - Integration   |                     |                   |  - Hardware       |
|                  |                     |                   |  - Printing Issue |
|                  |                     |                   |  - DB Related     |
|                  |                     |                   |  - Server Reboot  |

### Motivation
### Solution Benefits
Reduce the time to classify a group of tickets acording to a pre defined taxonomy.
Take advantage of ML / AI algorithms to classify tickets using experience in 25K+ tickets
### Solution Use
- Case 1:
  Classify a group of tickets to understand the kind of work received and prepare the information for a deep analysis about workload, structure of teams resolving tickets, productivity, etc.
  
- Case 2:
  Classify tickets as soon as it is received and route to the correct team according to caracteristic of the ticket and the classification generate by the model
### Step by Step solution
1) Collect data:
    - 1.1 Used 25K+ preclassified tickets
    - 1.2 Clean tickets and resolve incongruencies in the classification
2) Test different algorithms considering F1 score metric to determine the best model.
    - 2.1 Use 70% of tickets to test algorithms
    - 2.2 Run different algorithms with different parameters
          - 2.2.1 Use a 10 fold method to run algorithms
    - 2.2 Compare algorithms and resutls, with F1 score metric and select model with best results.
    
