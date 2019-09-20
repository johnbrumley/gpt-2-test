# python script to extract questions from the squad json file

# not really using this one anymore

import json
import pandas as pd
from pandas.io.json import json_normalize

# open file
with open('squad-train.json', encoding='utf8', 'r') as f:
    d = json.load(f)

# parse and flatten every question answer statement ('qas') within data > paragraphs
df = json_normalize(data=d['data'], record_path=['paragraphs','qas'])

df['question']

# save as csv since gpt-2-simple automatically adds start/end tokens

df.to_csv('squad-quest.csv', index=False)