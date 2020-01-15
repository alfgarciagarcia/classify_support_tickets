
# Instructions to run the model.

Prerequisites
Create the following structure of directories in your computer:

- class
  - models
  - to_process
  - processed

### Files:
Download and copy:

1. RCAPRedictormodelRF_v1.mod , RCAPRedictormodelRFLevel2_v2.mod adn autrcabigramfile_lda to models directory
2. classtkt_config.py, classtkt_main.py, classtkt_funcs.py to class directory


### Inputs:

Excel or CVS file with tickets information, at least a description for the ticket

### Outputs:

The process will classify tickets in the input file and return an Excel file with the information about each ticket with a category adn subcategory assigned and a confidence of the classification in the formprobability that that category or subcategory fit accordign to the model. Also provide a confidence field about the classification, with 3 possible values: Excellent, Great and Possible, based in the probability of the category and subvategory.
