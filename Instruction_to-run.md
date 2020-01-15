
# Instructions to run the model.

### Prerequisites

Your computer should have python 3.6 installed
These are the libraries required: (*You can use requirements.txt file to install the correct versions*)
- numpy==1.17.0
- matplotlib==3.1.1
- pandas==0.25.0
- wordcloud==1.5.0
- sklearn_pandas==1.8.0
- spacy==2.1.4
- gensim==3.4.0
- scikit_learn==0.21.3

Create the following structure of directories in your computer:

- class
  - models
  - to_process
  - processed

### Files:
Download and/ or copy:

1. RCAPRedictormodelRF_v1.mod , RCAPRedictormodelRFLevel2_v2.mod adn autrcabigramfile_lda to models directory
2. classtkt_config.py to class directory
   - This program contains configuration for the model, including directory strcuture, name of input and output file
3. classtkt_main.py to class directory
   - This program ins the main program to run the model
4. classtkt_funcs.py to class directory
   - Thsi program contains functions to clean, predict and save the file 
3. Copy your Excel input file  to to_process directory

### Inputs:

Excel or CVS file with tickets information, at least a description for the ticket

### Outputs:

The process will classify tickets in the input file and return an Excel file with the information about each ticket with a category adn subcategory assigned and a confidence of the classification in the formprobability that that category or subcategory fit accordign to the model. Also provide a confidence field about the classification, with 3 possible values: Excellent, Great and Possible, based in the probability of the category and subvategory.

## To Run
From a terminal run: python classtkt_main.py

The program will ask for details about
1. Name of the file to process
2. Name of the sheet in the excel file to use
3. Number of row to skip to reach the titles of the fields
4. Name of the column with the description of the ticket
5. Name of the column with the short description of the ticket

## Results
The program will display results of the process and will save 2 files with the tickets classified in the "processed" directory. One file in Excel format and one in pkl format (zip format). 

The name of the files will be the origianl name of the input file  plius the date.
