#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:01:36 2019

@author: alfredogarcia
Using xlsx file and description in tickets, classify in one of 7
possible categories and 20 subcategories.

"""

import classtkt_funcs as funcs

def main():
    '''main function to call functiosn to classifgy tickets'''
    print('Reading file')
    try:
        dfreadfile, col_desc, col_short_desc, found_records = funcs.read_file()
    except IOError:
        print('Error: can\'t find the file or read data')
    else:
        if found_records:
            print('cleaning & preprocessing')
            dfreadfile = funcs.cleaning_preprocessing(dfreadfile,
                                                      col_desc,
                                                      col_short_desc)
            print('Classifing tickets')
            data_frame = funcs.predict_categories(dfreadfile)
            print('Saving results to disk')
            funcs.print_results(data_frame)

if __name__ == "__main__":
    main()
