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
### Use Case
- Case 1:
  Classify a group of tickets to understand the kind of work received and prepare the information for a deep analysis about workload, structure of teams resolving tickets, productivity, etc.
  
- Case 2:
  Classify a ticket as soon as it is received and route to the correct team according to caracteristic of the ticket and the classification generate by the model
### Step by Step solution
1) Collect data:
    - 1.1 Used 25K+ preclassified tickets
    - 1.2 Clean tickets and resolve incongruencies in the classification
2) Test different algorithms considering F1 score metric to determine the best model.
    - 2.1 Use 70% of tickets to test algorithms
    - 2.2 Run different algorithms with different parameters
      - 2.2.1 Use a cross validation with 10 fold to obtain metrics
    - 2.2 Compare algorithms and resutls, with F1 score metric and select model with best results.
    
### Results

#### Training

For Level 1
total records:    26268
Cross Validation  10 fold
f1 score:         80.449%
Accuracy:         81.297%
Precision:        84.364%
Recall:           81.297%
#### Classifcation report

|                   precision|    recall|  f1-score|   support|
|------------------|---------|----------|----------|----------|
|    account_mgmt  |     0.92|      0.86|      0.89|     11079|
|       app_error  |     0.69|      0.93|      0.80|      9468|
| service_request  |     0.97|      0.62|      0.76|      2528|
|    integrations  |     0.87|      0.68|      0.76|       680|
|alert_monitoring  |     0.97|      0.82|      0.89|       358|
|  Infrastructure  |     0.98|      0.38|      0.55|       488|
|      Data Error  |     0.94|      0.29|      0.45|      166 | 
|                  |         |          |          |          |
|        accuracy  |         |          |      0.81|     26268|
|       macro avg  |     0.90|      0.65|      0.73|     26268|
|    weighted avg  |     0.84|      0.81|      0.80|     26268|

For Level 2
total records:    26268
Cross Validation  10 fold
f1 score:         87.034%
Accuracy:         87.650%
Precision:        87.950%
Recall:           87.650%
Classifcation report

|                   precision|   recall | f1-score |   support|
|------------------|---------|----------|----------|----------|
        App Error       0.82      0.82      0.82      4070
   Access Request       0.87      0.99      0.92      5834
   Account Update       1.00      0.92      0.96      4251
      Login Issue       0.88      0.43      0.58       994
       Data Issue       0.91      1.00      0.95      1450
          Request       0.86      0.93      0.89      1461
App Functionality       0.83      0.87      0.85      4861
    Configuration       0.97      0.85      0.91       342
       DB Related       0.81      0.75      0.78        96
         Hardware       0.97      0.93      0.95       218
   Printing Issue       0.87      0.96      0.91       161
         App Down       0.96      0.49      0.65       537
      Enhancement       0.82      0.75      0.78       725
    Server Reboot       1.00      1.00      1.00        13
         Alert DB       0.98      1.00      0.99       243
     Report Issue       0.95      0.34      0.50       217
        Alert App       1.00      0.97      0.98       115
    File Transfer       0.76      0.42      0.54       132
      Integration       0.00      0.00      0.00        13
              Job       0.86      0.98      0.92       535
|                  |         |          |          |          |
         accuracy                           0.88     26268
        macro avg       0.86      0.77      0.79     26268
     weighted avg       0.88      0.88      0.87     26268
     
 
 #### Test
 For Level 1
 f1 score 0.8197822552765655
RandomForestClassifier Accuracy:  0.8274706867671692
RandomForestClassifier Precision: 0.851012137889825
RandomForestClassifier Recall:    0.8274706867671692
Classifcation report

|                  |precision|   recall | f1-score |   support|
|------------------|---------|----------|----------|----------|
    account_mgmt       0.91      0.88      0.89      2741
       app_error       0.72      0.93      0.81      2405
 service_request       0.97      0.64      0.77       592
    integrations       0.82      0.68      0.74       174
alert_monitoring       0.98      0.90      0.94        97
  Infrastructure       0.97      0.53      0.68       123
      Data Error       0.95      0.33      0.49       435
|                  |         |          |          |          |
        accuracy                           0.83      6567
       macro avg       0.90      0.70      0.76      6567
    weighted avg       0.85      0.83      0.82      6567

For Level 2
f1 score 0.7511059519588367
RandomForestClassifier Accuracy: 0.7597076290543627
RandomForestClassifier Precision: 0.7942976587591652
RandomForestClassifier Recall: 0.7597076290543627
Classifcation report

|                  |precision|   recall | f1-score |   support|
|------------------|---------|----------|----------|----------|
        App Error       0.58      0.77      0.66      1051
   Access Request       0.78      0.84      0.81      1456
   Account Update       1.00      0.93      0.96      1066
      Login Issue       0.77      0.33      0.46       219
       Data Issue       0.94      0.35      0.51       387
          Request       0.97      0.66      0.79       339
App Functionality       0.65      0.86      0.74      1227
    Configuration       0.94      0.81      0.87        81
       DB Related       1.00      0.08      0.14        13
         Hardware       0.98      0.82      0.90        68
   Printing Issue       0.83      0.13      0.22        39
         App Down       0.83      0.54      0.66       127
      Enhancement       0.95      0.48      0.64       172
    Server Reboot       1.00      1.00      1.00         3
         Alert DB       0.96      0.88      0.92        56
     Report Issue       1.00      0.15      0.25        48
        Alert App       1.00      0.93      0.96        41
    File Transfer       0.80      0.22      0.35        36
      Integration       0.00      0.00      0.00         2
              Job       0.79      0.79      0.79       136
|                  |         |          |          |          |
         accuracy                           0.76      6567
        macro avg       0.84      0.58      0.63      6567
     weighted avg       0.79      0.76      0.75      6567
