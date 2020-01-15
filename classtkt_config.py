#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:00:00 2019

@author: alfredogarcia

Config for Tickets Classification model
"""
import re
import os
from pathlib import Path
import datetime
import spacy
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.externals import joblib
from sklearn_pandas import DataFrameMapper

NLP = spacy.load('en', disable=['parser', 'ner'])

STOPWORDS = ['FW', 'ssw', 'SSW', 'SSW:', 'thank', '\n', '\n\n', '\n\n\n\n',\
             'thank', '\t', '\t ', 'â', ':', '/', '-', '_', 'pm', 'am', ',', 'PM']

LABELREGEX = re.compile(r'SSW:|Department:|Work Extension:|From:|Sent:|To:|\
                        Cc:|Please provide your application logon name:|\
                        The information transmitted in this email|\
                        .@staples.com|Tel:|Mob:|Preferred.ca')

TARGET_NAMESL1 = ['account_mgmt', 'app_error', 'service_request', 'integrations',
                  'alert_monitoring', 'Infrastructure', 'Data Error']
TARGET_NAMESL2 = ['App Error', 'Access Request', 'Account Update',
                  'Login Issue', 'Data Issue', 'Request', 'App Functionality',
                  'Configuration', 'DB Related', 'Hardware', 'Printing Issue',
                  'App Down', 'Enhancement', 'Server Reboot', 'Alert DB',
                  'Report Issue', 'Alert App', 'File Transfer', 'Integration',
                  'Job']

DICTRCA = dict(zip(range(1, len(TARGET_NAMESL1)+1, 1), TARGET_NAMESL1))
DICTRCAL2 = dict(zip(range(1, len(TARGET_NAMESL2)+1, 1), TARGET_NAMESL2))


ORIGINAL_PATH = os.getcwd()
PATH = str(Path(ORIGINAL_PATH))

MODELPATH = os.path.join(PATH, 'models')

#load model
MODNAME = 'RCAPRedictormodelRF_v1'
MODELFILENAME = os.path.join(MODELPATH, MODNAME + '.mod')
MODEL = joblib.load(MODELFILENAME)

MODNAME3 = 'RCAPRedictormodelRFLevel2_v2'
MODELFILENAME3 = os.path.join(MODELPATH, MODNAME3 + '.mod')
MODEL3 = joblib.load(MODELFILENAME3)

TODAY = datetime.datetime.today()
DIRECTORY_NAME = 'autrca'

INPUTFILE = input('File name: ')
FILENAME, FILE_EXTENSION = os.path.splitext(INPUTFILE)
FILEORIGINALTICKETS = os.path.join(PATH, 'data', 'to_process', INPUTFILE)

BIGRAMFILE = os.path.join(MODELPATH, DIRECTORY_NAME + 'bigramfile_lda')
DIRECTORYFILE = os.path.join(MODELPATH, DIRECTORY_NAME + 'dictionary_lda')
LDAMODEL = os.path.join(MODELPATH, DIRECTORY_NAME + 'ldamodel')

#outputfiles
FILE_W_PREDICTIONS_PKL = os.path.join(PATH, 'data', 'processed',
                                      FILENAME + '{:%m%d%y}.pkl').format(TODAY)
FILE_W_PREDICTIONS_XLSX = os.path.join(PATH, 'data', 'processed',
                                       FILENAME + '{:%m%d%y}.xlsx').format(TODAY)

WORDCLOUDFILE = os.path.join(PATH, 'data', 'processed',
                             'wordcloud_' + '{:%m%d%y}.png').format(TODAY)
# create hasing vectors
VECTORIZER = HashingVectorizer(n_features=60)

MAPPER2 = DataFrameMapper([
    ('z_RCA_predicted_desc', HashingVectorizer(n_features=60)),
    ('z_cleanclasstxt2', HashingVectorizer(n_features=60)),
])
