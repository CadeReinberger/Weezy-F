from qbutil import question
import pandas as pd
from random import choice, sample

cats = ['art', 'lit', 'military', 'music', 'nonfic', 'people']
tags = {'art' : 'who made ', 'lit' : 'who wrote ', 
        'military' : 'what was ', 'music' : 'who composed ', 
        'nonfic' : 'who wrote ', 'people' : 'who was '}

questions = []
cat_questions = {}
for cat in cats:
    fn = 'blueplate/' + cat + '.xlsx'
    qs_raw = pd.read_excel(fn).values.tolist()
    cat_qs = [question(tags[cat] + q[0], q[1]) for q in qs_raw]
    questions.extend(cat_qs)
    cat_questions[cat] = cat_qs

def get_random_fact():
    return choice(questions)

def get_random_facts(num_facts):
    return sample(questions, num_facts)

def get_random_fact_by_cat(cat):
    if not cat in cat_questions:
        raise Exception('ERROR! Invalid Category: ' + str(cat))
    return choice(cat_questions[cat])

def get_random_facts_by_cat(cat, num_facts):
    if not cat in cat_questions:
        raise Exception('ERROR! Invalid Category: ' + str(cat))
    return sample(cat_questions[cat], num_facts)
