## Results
Below details results for training and test phases. For training, 80% of tickets were used (26,268) amd for testing 20% of tickets were used (6567)
#### Training Results
During the training phase, different algorithms with different parameters were tested to select the best model. Algorithms include are:

- Logistic Regression
- AdaBoost
- Random Forest
- ELMO
- Output code classfier with Random forest
- SGDC
- Decsion TRee
- Gausian NB
- Radius Neighbors
- K Neighbors
- Naive Bayes
- XGBoost

After reviewed results for each model, Random Forest Classfier was the model that provided the best metric for F1-score.

Fine tuning to the Random Forest Classfier parameters such as: criterion, max_depth, min_samples_leaf and number of trees, improved F1-score metric to **80.44%** 


##### For Level 1

total records:      26,268

|Cross Validation|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|10 Fold         |80.449% |81.297% |  84.364%| 81.297%

##### Classifcation report

|Category          |Precision|    Recall|  f1-score|   support|
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

##### For Level 2

|Cross Validation|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|10 Fold         |87.034% |87.650% |  87.950%| 87.650%

##### Classifcation report

|Subcategory       |Precision |   Recall | f1-score |   support|
|------------------|----------|----------|----------|----------|
|        App Error |      0.82|      0.82|      0.82|      4070
|   Access Request |      0.87|      0.99|      0.92|      5834
|  Account Update  |      1.00|      0.92|      0.96|      4251
|      Login Issue |      0.88|      0.43|      0.58|       994
|       Data Issue |      0.91|      1.00|      0.95|      1450
|          Request |      0.86|      0.93|      0.89|      1461
|App Functionality |      0.83|      0.87|      0.85|      4861
|    Configuration |      0.97|      0.85|      0.91|       342
|       DB Related |      0.81|      0.75|      0.78|        96
|         Hardware |      0.97|      0.93|      0.95|       218
|   Printing Issue |      0.87|      0.96|      0.91|       161
|         App Down |      0.96|      0.49|      0.65|       537
|      Enhancement |      0.82|      0.75|      0.78|       725
|    Server Reboot |      1.00|      1.00|      1.00|        13
|         Alert DB |      0.98|      1.00|      0.99|       243
|     Report Issue |      0.95|      0.34|      0.50|       217
|        Alert App |      1.00|      0.97|      0.98|       115
|    File Transfer |      0.76|      0.42|      0.54|       132
|      Integration |      0.00|      0.00|      0.00|        13
|             Job  |      0.86|      0.98|      0.92|       535
|                  |          |         |         |         
|          Accuracy|          |         |       0.88|     26268
|        macro avg |      0.86|      0.77|      0.79|     26268
|     weighted avg |      0.88|      0.88|      0.87|     26268
     
 
 #### Test Results
 #### For Level 1

|Total Records|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|6567         |81.978% |82.747% |  85.101%| 82.747%

#### Classifcation report

|Category           |Precision|   Recall | f1-score |  support|
|-------------------|---------|----------|----------|---------|
|    account_mgmt   |    0.91 |     0.88 |     0.89 |     2741 
|       app_error   |    0.72 |     0.93 |     0.81 |     2405
| service_request   |    0.97 |     0.64 |     0.77 |      592
|    integrations   |    0.82 |     0.68 |     0.74 |      174
|alert_monitoring   |    0.98 |     0.90 |     0.94 |       97
|  Infrastructure   |    0.97 |     0.53 |     0.68 |      123
|      Data Error   |    0.95 |     0.33 |     0.49 |      435
|                   |         |          |          |          
|        accuracy   |         |          |     0.83 |     6567
|       macro avg   |    0.90 |     0.70 |     0.76 |     6567
|    weighted avg   |    0.85 |     0.83 |     0.82 |     6567

#### For Level  2

|Total Records|f1 score|Accuracy|Precision|Recall
|---|---|---|---|---|
|6567         |75.110%|75.970%|  79.429%| 75.970%

#### Classifcation report

|Subcategory       |Precision|   Recall | f1-score |   support|
|------------------|:---------:|:----------:|:----------:|:----------:|
|        App Error  |     0.58|      0.77|      0.66|      1051
|   Access Request  |     0.78|      0.84|      0.81|      1456
|   Account Update  |     1.00|      0.93|      0.96|      1066
|      Login Issue  |     0.77|      0.33|      0.46|       219
|       Data Issue  |     0.94|      0.35|      0.51|       387
|          Request  |     0.97|      0.66|      0.79|       339
|App Functionality  |     0.65|      0.86|      0.74|      1227
|    Configuration  |     0.94|      0.81|      0.87|        81
|       DB Related  |     1.00|      0.08|      0.14|        13
|         Hardware  |     0.98|      0.82|      0.90|        68
|   Printing Issue  |     0.83|      0.13|      0.22|        39
|         App Down  |     0.83|      0.54|      0.66|       127
|      Enhancement  |     0.95|      0.48|      0.64|       172
|    Server Reboot  |     1.00|      1.00|      1.00|         3
|         Alert DB  |     0.96|      0.88|      0.92|        56
|     Report Issue  |     1.00|      0.15|      0.25|        48
|        Alert App  |     1.00|      0.93|      0.96|        41
|    File Transfer  |     0.80|      0.22|      0.35|        36
|      Integration  |     0.00|      0.00|      0.00|         2
|              Job  |     0.79|      0.79|      0.79|       136
|                  |         |          |          |          
|         accuracy  |         |          |      0.76|      6567
|        macro avg  |     0.84|      0.58|      0.63|      6567
|     weighted avg  |     0.79|      0.76|      0.75|      6567
