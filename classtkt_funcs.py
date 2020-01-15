#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:41:11 2019

@author: alfredogarcia

Read excel file and classify tickets in 7 catgories and 20 subcategories.
"""
import re
from wordcloud import WordCloud
import numpy as np
import pandas as pd
from pandas import ExcelWriter
import gensim
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import STOPWORDS
import matplotlib.pyplot as plt
import classtkt_config as config

plt.rcParams['figure.figsize'] = (20, 10)
def cleanlines2(text):
    '''Clean text removing urls, punctation, numbers, whitespace and convert
    to lowecase'''
    text1 = str(text).lower()

    lines = []   #split in lines
    for line in text1.split('\n'):
        line = str(line)
        line = line.strip('\n')
        if line:
            lines.append(line)
    cleantext = ''
    for line in lines:
        filterreg = config.LABELREGEX.search(line)
        if filterreg is None:
            cleantext = cleantext + line #+ '\n'
        else:
            if filterreg.group():
                pass
            else:
                cleantext = cleantext + line #+ '\n'
    cleantext = str(cleantext)
    text1 = re.sub('\\S*@\\S*\\s?', '', cleantext)  # Remove Emails
    text1 = re.sub("\'", "", text1)                 #remove single quotes
    text1 = re.sub('\\s+', ' ', text1)              #remove new line character
    text1 = re.sub(r'http\S+', '', text1)           #remove URLs
    text1 = tokenize(str(text1))
    text1 = str(text1)
    #using gensim to remove numbers, punctuation, whitespace, stopwords,
    #non-alfa, convert lowercase and stem
    text1 = ' '.join(preprocess_string(str(text1)))
    return text1

def tokenize(text):
    '''Lematization and tokenization of text'''
    output = []
    text1 = config.NLP(text)

    doc = [token.lemma_ for token in text1 \
           if token.is_alpha and not token.is_stop and not token.is_digit]
    doc = [token for token in doc if token not in STOPWORDS]
    output.append(' '.join(doc))
    return output

def verify_level1(level1, level2):
    '''Verify that L2 corrspond to L1, if not update L1'''
    #relation L1 and L2, mark L1_shouldbe with the correct L! according to L2

    rel_categories2 = {2:1, 3:1, 4:1, 1:2, 7:2, 12:2, 6:3, 8:3, 13:3, 18:4,
                       19:4, 20:4, 15:5, 17:5, 9:6, 10:6,
                       11:6, 14:6, 5:7, 16:7}
    if level1 == rel_categories2.get(level2):
        return level1
    return rel_categories2.get(level2)

def train_bigrams(str3, genbig=False):
    '''generate bigrams and trigrams with text use to train model'''
    #train bigrams and trigrams
    processed_docs = []
    batchsize = 1
    if genbig:
        batchsize = 100
    for doc in config.NLP.pipe(str3, n_threads=4, batch_size=batchsize):
        # Process document using Spacy NLP pipeline.
        ents = doc.ents  # Named entities.
        # Lemmatize tokens
        doc = [token.lemma_ for token in doc
               if token.is_alpha and not token.is_stop and not token.is_digit]
        doc = [token for token in doc if token not in STOPWORDS]
        # Remove common words from a stopword list.
        # Add named entities, but only if they are a compound of more than word
        doc.extend([str(entity) for entity in ents if len(entity) > 1])
        processed_docs.append(doc)

    #use bigram and trigrams
    if genbig:   #if true generate biagram model
        bigram = gensim.models.phrases.Phrases(processed_docs, min_count=50)
        trigram = gensim.models.phrases.Phrases(bigram[processed_docs],
                                                min_count=10)
        bigram = gensim.models.phrases.Phraser(trigram)
        bigram.save(config.BIGRAMFILE)
    return processed_docs


def read_file():
    '''read file and load to memory'''
    #read file
    if config.FILE_EXTENSION == '.pkl':
        df2 = pd.read_pickle(config.FILEORIGINALTICKETS, 'gzip')
        dfreadfile = df2.copy()
    elif config.FILE_EXTENSION == '.csv':
        dfreadfile = pd.read_csv(config.FILEORIGINALTICKETS)
    elif config.FILE_EXTENSION in ['.xlsx', '.xls']:
        tickets_file = pd.ExcelFile(config.FILEORIGINALTICKETS)
        print(f'Sheets in the file: {tickets_file.sheet_names}')
        sheetname = input(f'Sheet to load: [{tickets_file.sheet_names[0]}] : ') \
                    or tickets_file.sheet_names[0]
        skiprows = input("Skip rows: [0]: ") or str(0)
        dfreadfile = tickets_file.parse(sheetname, skiprows=int(skiprows))
    print(f'Total rows and columns in the file: {dfreadfile.shape}')
    print(f'{dfreadfile.shape[1]} Columns in the file: {dfreadfile.columns}')
    column_desc = ''
    column_short_desc = ''
    found_records = False
    if not dfreadfile.empty:
        found_records = True
        column_desc = input('Column for [Description]: ') or 'Description'
        column_short_desc = input('Column for Short Description [xshort_title]: ') or 'xshort_title'
        if column_short_desc == 'xshort_title':
            dfreadfile['xshort_title'] = ''
    return dfreadfile, column_desc, column_short_desc, found_records


def cleaning_preprocessing(dfreadfile, column_desc, column_short_desc,
                           trainbiagrams= False):
    '''Clean and preprocessing file, generating bigrams for the text and
    hasigh vector returns df with clean text'''
    print('Cleaning and preprocessing...')
    #concatenate short and long descriptions
    dfreadfile['z_classtxt'] = dfreadfile[column_short_desc].apply(str) +\
                               ' ' + dfreadfile[column_desc].apply(str)

    #remove description null
    dfreadfile = dfreadfile[dfreadfile.z_classtxt.notnull()]

    dfreadfile['z_cleanclasstxt2'] = dfreadfile.apply(lambda \
                                                      row: \
                                                      cleanlines2(row['z_classtxt']),
                                                      axis=1)

    ##generate bigrams and trigrams from file and save
    print('Generating bigrams')
    dfreadfile.reset_index(drop=True)
    str3 = dfreadfile['z_cleanclasstxt2']
    processed_docs = train_bigrams(str3, trainbiagrams)
    bigram = gensim.models.phrases.Phraser.load(config.BIGRAMFILE)
    #put back bigrams in dfreadfile
    processed_docs1 = []
    for doc in processed_docs:
        bigram_sentence = ' '.join(bigram[doc])
        processed_docs1.append(bigram_sentence)
    processed_docs = []
    batchsize= 100
    if trainbiagrams:
        batchsize= 1
    for doc in config.NLP.pipe(processed_docs1, n_threads=4, batch_size=batchsize):
        ents = doc.ents  # Named entities.
        doc = [token.lemma_ for token in doc]  # Lemmatize tokens,
        doc = [token for token in doc if token not in STOPWORDS]
        # Add named entities, but only if they are a compound of more than word.
        doc.extend([str(entity) for entity in ents if len(entity) > 1])
        processed_docs.append(doc)
    del processed_docs1
    docs = processed_docs
    del processed_docs
    for num, entity in enumerate(ents):
        print('Entity {%d}-{%s} : {%s}' % (num+1, entity, entity.label_))
    docs1 = []
    for doc in docs:
        docs1.append(' '.join(doc))
    dfcleantxtnew = pd.DataFrame(docs1, columns=['z_newclean'])
    dfreadfile.reset_index(drop=True)
    dfcleantxtnew.reset_index(drop=True)
    dfreadfile = pd.concat([dfreadfile.reset_index(drop=True),
                            dfcleantxtnew.reset_index(drop=True)], axis=1)
    dfreadfile['z_cleanclasstxt2'] = dfreadfile['z_newclean']
    dfreadfile.drop(['z_newclean'], axis=1, inplace=True)
    print(f'dfreadfile {dfreadfile.shape}')
    print('Generating vectors...')
    # create hasing vectors
    dfreadfile['z_hashvector'] = list(config.\
              VECTORIZER.transform(dfreadfile['z_cleanclasstxt2']).toarray())
    print('Done cleaning and preprocessing')
    return dfreadfile


def predict_categories(dfreadfile):
    '''Predict  categories for level 1 & 2, return df with
    categories and probabilities
    '''
    ynew = config.MODEL.predict(dfreadfile['z_hashvector'].tolist())
    dfynew = pd.DataFrame(ynew, columns=['z_RCA_predicted'])
    #add desc for predicted RCA

    dfynew['z_RCA_predicted_desc'] = dfynew['z_RCA_predicted'].\
                                     map(config.DICTRCA).fillna(0)
    #predict probabilities using Random Forest results
    ynew_prob = config.MODEL.predict_proba(dfreadfile['z_hashvector'].tolist())
    dfprobynew = pd.DataFrame(ynew_prob,
                              columns=['z_Prob_class1', 'z_Prob_class2',
                                       'z_Prob_class3', 'z_Prob_class4',
                                       'z_Prob_class5', 'z_Prob_class6',
                                       'z_Prob_class7'])
    dfynew2 = pd.concat([dfynew, dfprobynew], axis=1)

    dfreadfile = dfreadfile.reset_index(drop=True)
    dfynew2 = dfynew2.reset_index(drop=True)

    test3 = pd.concat([dfreadfile, dfynew2], axis=1)
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 1,
                                    test3["z_Prob_class1"], 0)
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 2,
                                    test3["z_Prob_class2"], test3['z_prob_pred'])
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 3,
                                    test3["z_Prob_class3"], test3['z_prob_pred'])
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 4,
                                    test3["z_Prob_class4"], test3['z_prob_pred'])
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 5,
                                    test3["z_Prob_class5"], test3['z_prob_pred'])
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 6,
                                    test3["z_Prob_class6"], test3['z_prob_pred'])
    test3['z_prob_pred'] = np.where(test3['z_RCA_predicted'] == 7,
                                    test3["z_Prob_class7"], test3['z_prob_pred'])

    #get second max prob
    test3['z_prob_pred_sec']= 0
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 1,
                                        test3[['z_Prob_class2', 'z_Prob_class3',
                                               'z_Prob_class4', 'z_Prob_class5',
                                               'z_Prob_class6', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 2,
                                        test3[['z_Prob_class1', 'z_Prob_class3',
                                               'z_Prob_class4', 'z_Prob_class5',
                                               'z_Prob_class6', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 3,
                                        test3[['z_Prob_class1', 'z_Prob_class2',
                                               'z_Prob_class4', 'z_Prob_class5',
                                               'z_Prob_class6', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 4,
                                        test3[['z_Prob_class1', 'z_Prob_class2',
                                               'z_Prob_class3', 'z_Prob_class5',
                                               'z_Prob_class6', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 5,
                                        test3[['z_Prob_class1', 'z_Prob_class2',
                                               'z_Prob_class3', 'z_Prob_class4',
                                               'z_Prob_class6', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 6,
                                        test3[['z_Prob_class1', 'z_Prob_class2',
                                               'z_Prob_class3', 'z_Prob_class4',
                                               'z_Prob_class5', 'z_Prob_class7']].max(axis=1),
                                        test3['z_prob_pred_sec'])
    test3['z_prob_pred_sec'] = np.where(test3['z_RCA_predicted'] == 7,
                                        test3[['z_Prob_class1', 'z_Prob_class2',
                                               'z_Prob_class3', 'z_Prob_class4',
                                               'z_Prob_class5', 'z_Prob_class6']].max(axis=1),
                                        0)


    test3['z_match'] = np.where(test3['z_prob_pred'] >= .80, 'excellent',
                                np.where(test3['z_prob_pred'] > .50,
                                         'great', 'possible'))
    #If difference between 1st and 2nd less than 120% move to 'possible match'
    test3['z_match'] = np.where(test3['z_prob_pred']-test3['z_prob_pred_sec'] < .1,
                                'possible', test3['z_match'])

    #predict L2
    #predict with mapper
    features2 = config.MAPPER2.fit_transform(test3)

    ynewlevel2 = config.MODEL3.predict(features2)
    dfynew = pd.DataFrame(ynewlevel2, columns=['z_RCAL2_predicted'])
    #add desc for predicted RCA

    dfynew['z_RCAL2_predicted_desc'] = dfynew['z_RCAL2_predicted'].\
                                       map(config.DICTRCAL2).fillna("No subclass")

    #predict probabilities using Random Forest results
    rf_level2_preds_validproba = config.MODEL3.predict_proba(features2)

    colsubclass = ['z_class'+str(x) for x in range(len(rf_level2_preds_validproba[1]))]
    dfprobynew = pd.DataFrame(rf_level2_preds_validproba, columns=colsubclass)
    dfynew2 = pd.concat([dfynew, dfprobynew], axis=1)
    test4 = pd.concat([test3, dfynew2], axis=1)
    test4['z_prob_predL2'] = test4[colsubclass].max(axis=1)
    test4['z_matchL2'] = np.where(test4['z_prob_predL2'] >= .80, 'excellent',
                                  np.where(test4['z_prob_predL2'] > .50,
                                           'great', 'possible'))
    #relation L1 and L2, mark L1_shouldbe with the correct L! according to L2
    test4['z_L1_shouldbe'] = test4.apply(lambda row: verify_level1(row['z_RCA_predicted'],
                                                                   row['z_RCAL2_predicted']),
                                         axis=1)

    return test4

def print_results(test4):
    '''Generate tables to save in xls file and generate xls file'''
    pd.set_option('max_colwidth', 200)
    prob_pred_describe = test4.z_prob_pred.describe()
    print(prob_pred_describe)
    matrix_match1 = pd.crosstab([test4['z_match']],
                                [test4['z_RCA_predicted_desc']],
                                margins=True,
                                dropna=False).sort_values('All',
                                                          ascending=False)
    matrix_match = pd.crosstab([test4['z_match']],
                               [test4['z_RCA_predicted_desc']],
                               margins=True, dropna=False,
                               normalize=True).sort_values('All',
                                                           ascending=False)
    print(matrix_match)

    prob_pred_describelevel2 = test4.z_prob_predL2.describe()
    print(prob_pred_describelevel2)
    matrix_match1level2 = pd.crosstab([test4['z_matchL2']],
                                      [test4['z_RCAL2_predicted_desc']],
                                      margins=True,
                                      dropna=False).sort_values('All',
                                                                ascending=False)
    matrix_matchlevel2percent = pd.crosstab([test4['z_matchL2']],
                                            [test4['z_RCAL2_predicted_desc']],
                                            margins=True, dropna=False,
                                            normalize=True).sort_values('All',
                                                                        ascending=False)
    print(matrix_matchlevel2percent)

    matrix_rca_rcalevel2 = pd.crosstab([test4['z_RCAL2_predicted_desc']],
                                       [test4['z_RCA_predicted_desc']],
                                       margins=True,
                                       dropna=False).sort_values('All',
                                                                 ascending=False)

    matrix_rca_rcalevel2_percent = pd.crosstab([test4['z_RCAL2_predicted_desc']],
                                               [test4['z_RCA_predicted_desc']],
                                               margins=True, dropna=False,
                                               normalize=True).sort_values('All',
                                                                           ascending=False)
    print(matrix_rca_rcalevel2_percent)

    matrix_l1_poss = pd.crosstab([test4['z_RCA_predicted']],
                                 [test4['z_L1_shouldbe']],
                                 margins=True, dropna=False)

    print(test4.filter(['z_RCA_predicted', 'z_L1_shouldbe'], axis=1).corr())

    #generate word cloud
    docs = test4['z_classtxt']
    docs = tokenize(str(docs))
    str1 = ''.join(str(r) for v in docs for r in v)

    # Generate a word cloud image

    #to change backgroud color use background_color='rgba(255, 255, 255, 0)'
    wordcloud = WordCloud(mode='RGBA', max_font_size=50).generate(str1)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    wordcloud.to_file(config.WORDCLOUDFILE)

    #save file
    test4.to_pickle(config.FILE_W_PREDICTIONS_PKL, 'gzip')
    print(f'tickets WITH RCA file saved as {config.FILE_W_PREDICTIONS_PKL}')
    writer = ExcelWriter(config.FILE_W_PREDICTIONS_XLSX,
                         engine='xlsxwriter',
                         options={'strings_to_formulas': False, 'strings_to_urls': False})

    workbook = writer.book
    wks1 = workbook.add_worksheet('WordCloud')
    wks1.write(0, 0, 'wordcloud')
    wks1.insert_image(2, 2, config.WORDCLOUDFILE, {'x_scale': 1.5, 'y_scale': 1.5})

    test4.to_excel(writer, sheet_name='tickets_with_predcited_rca')
    prob_pred_describe.to_excel(writer, sheet_name='Distribution Predictions')
    prob_pred_describelevel2.to_excel(writer, sheet_name='Distribution PredictionsL2')
    matrix_match.to_excel(writer, sheet_name='matrix match_perct')
    matrix_match1.to_excel(writer, sheet_name='matrix match_tkts')
    matrix_matchlevel2percent.to_excel(writer, sheet_name='matrix_matchL2percent')
    matrix_match1level2.to_excel(writer, sheet_name='matrix_matchL2')
    matrix_rca_rcalevel2.to_excel(writer, sheet_name='matrix_rca_rcaL2')
    matrix_rca_rcalevel2_percent.to_excel(writer, sheet_name='matrix_rca_rcaL2perct')
    matrix_l1_poss.to_excel(writer, sheet_name='matrix_L1_possL1')
    writer.save()
    print(f'tickets with Predicted RCA XLSX file saved as {config.FILE_W_PREDICTIONS_XLSX}')


def main():
    '''Main function to read file'''
    print('reading file...')
    #dfreadfile, column_desc, column_short_desc, found_records =
    read_file()

if __name__ == "__main__":
    main()
