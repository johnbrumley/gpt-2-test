import pandas as pd
import nltk
from nltk import sent_tokenize

import os
import re
import argparse

def get_questions(txt):

    # fill up list of question sentences
    qs = []
    for sent in sent_tokenize(txt):
        if sent[-1] is '?':
            # remove newlines? and tabs
            sent = sent.replace('\n',' ')
            sent = sent.replace('\t',' ')
            
            # remove numbers too
            # first num:num because of bible
            sent = re.sub('[0-9]+:[0-9]+','',sent)
            # then just num
            sent = re.sub('[0-9]+','', sent)

            # also remove weird characters
            sent = re.sub('[@#$%^&*]','', sent)

            # store it
            qs.append(sent)

    print('    found', len(qs), 'questions')
    return qs

def main(files):
    
    # # download punkt ... do i need this every time?
    nltk.download('punkt')

    total_qs = []
    for file in files:
        print('extracting questions from', file)
        # read in the text
        with open(file,'r',encoding='utf8',errors='ignore') as f:
            txt = f.read()
        # get questions
        total_qs.extend(get_questions(txt))

    print(len(total_qs), 'questions in total')
    
    # store as csv
    print('saving file')
    df = pd.DataFrame(total_qs)
    print(df.head())
    df.to_csv('questions.csv', index=False, header=False, encoding='utf-8-sig')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process these text files')
    parser.add_argument('--files', help='directory of texts')
    args = parser.parse_args()
    
    if args.files is None or len(args.files) is 0:
        print('Please use --files to add a file name(s)')
    else:
        files = os.listdir(args.files)
        main(files)

    
    
    

    