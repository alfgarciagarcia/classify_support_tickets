# Classify Support Tickets 
Classify support tickets depending of text in description and short description fields of the ticket, the model classifies the ticket in 2 categories

### Assumptions
These are the categories to classify the tickets in 2 levels: Level 1 with 7 categories and each of them with subcategories

|1 Account Management | 2 Application Error  | 3 Service Request |
|---------------------|----------------------|-------------------|
|  - Access Request   |   - App Error        |  - Request        |
|  - Account Update   |   - App Functionality|  - Enhancement    |
|  - Login Issue      |   - App Down         |  - Configuration  |
  

|4 Integrations    | 5 Alert Monitoring  | 6 Data Error      |7 Infrastructure   |
|------------------|---------------------|-------------------|-------------------|
|  - Job           |   - Alert DB        |  - Data Issue     |  - Infrastructure |
|  - File Transfer |   - Alert App       |  - Report Issue   |  - DB Related     |
|  - Integration   |                     |                   |  - Hardware       |
|                  |                     |                   |  - Printing Issue |
|                  |                     |                   |  - DB Related     |
|                  |                     |                   |  - Server Reboot  |

Due that the inbalance of categories in a sample of tickets, F1-score was the metric used to determine the best model.

Subcategories only belong to one category

### Solution Benefits
Reduce the time to classify a group of tickets acording to a pre defined categories and subcategories.
Take advantage of ML / AI algorithms to classify tickets using experience in 26K+ tickets.

### Use Case
- Case 1:
  Classify a group of tickets to understand the kind of work received and prepare the information for a deep analysis about workload, structure of teams resolving tickets, productivity, etc.
  
- Case 2:
  Classify a ticket as soon as it is received and route to the correct team according to caracteristic of the ticket and the classification generate by the model
### Step by Step solution
1) Collect data:
   - 1.1 Used 32K+ preclassified tickets
   - 1.2 Clean tickets and resolve incongruencies in the classification
2) Train different algorithms considering F1 score metric to determine the best model.
   - 2.1 Use 80% of tickets to test algorithms
   - 2.2 Run different algorithms with different parameters
     - 2.2.1 Use a cross validation with 10 fold to obtain metrics
   - 2.2 Compare algorithms and resutls, with F1 score metric and select model with best results.
3) Test algorithm with 20% of tickets

## Use
[Review this file for detail instructions to use the model.](instructions_to_run,md)
### Inputs:
Excel or CVS file with tickets information, at least a description for the ticket

### Outputs:
The process will classify tickets in the input file and return an Excel file with the information about each ticket with a category adn subcategory assigned and a confidence of the classification in the formprobability that that category or subcategory fit accordign to the model. Also provide a confidence field about the classification, with 3 possible values: Excellent, Great and Possible, based in the probability of the category and subvategory.

## Results
Below a summary of results for training dataset and test dataset. For training, 80% of tickets were used (26,268) and for testing 20% of tickets were used (6567)

For training a cross validation with a 10 fold was used to verify the results of the model

Final algorithm with best result was Random Forest
#### Training Results

|Level 1|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|1         |80.449% |81.297% |  84.364%| 81.297%
|2         |87.034% |87.650% |  87.950%| 87.650%
 
 #### Test Results

|Level|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|1         |81.978% |82.747% |  85.101%| 82.747%
|2         |75.110%|75.970%|  79.429%| 75.970%

For more details about results including parameters used, and classification report,review this [file](results.md)
