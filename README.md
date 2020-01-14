# Classify Support Tickets 
Classify support tickets depending of text in the ticket, the model classifies the ticket in 2 categories

### Assumptions
These are the categories to classify the tickets:

1 account_mgmt
  - Access Request
  - Account Update
  - Login Issue
2 app_error
  - App Error
  - App Functionality
  - App Down
3 service_request
  - Request
  - Enhancement
  - Configuration
4 integrations
  - Job
  - File Transfer
  - Integration
5 alert_monitoring
  - Alert DB
  - Alert App 
6 Data Error
  - Data Issue
  - Report Issue
7 Infrastructure
  - Infrastructure
  - DB Related
  - Hardware
  - Printing Issue
  - DB Related
  - Server Reboot

### Motivation
### Solution Benefits
Reduce the time to classify a group of tickets acordign to a pre defined taxonomy.
Take advantage of ML / AI algorithms to classify tickets using experience in 25K+ tickets
### Solution Use
- Case 1:
  Classify a gorup of tickets to understand the kind of work received and prepare the information for a deep analysis about workload, structure of teams resolving tickets, productivity, etc.
  
- Case 2:
  Classify tickets as soon as it is received and route to the correct team according to caracteristic of the ticket and the classification generate by the model
### Step by Step solution
1) Collect data:
    - 1.1) Used 25K+ preclassified tickets
    - 1.2) Clean tickets and resolve incongruencies in the classification
2) Test different algorithms considering F1 scoere metric to determine the best model.
    - 2.1) Use 70% of tickets to test algorithms
    - 2.2) Run different algorithms with different parameters
         - 2.2.1) Use a 10 fold method to run algorithms
    - 2.2) Compare algorithms and resutls, with F1 score metric and select model with best results.
    
