import pandas as pd
import numpy as np
from _collections import defaultdict

def process_data(data):
        data_list = []
        data_name = data.replace('^', '_').split('_')
        n = 1
        for names in data_name:
            if n % 2 == 0:
                data_list.append(names)
            n += 1
        return data_list

def look_up(symptoms:list):
    df = pd.read_excel("raw_data.xlsx")

    data = df.fillna(method='ffill')

    disease_list = []
    disease_symptom_dict = defaultdict(list)
    disease_symptom_count = {}
    count = 0
    symptom_dict = defaultdict(list)
    l = []
    for idx, row in data.iterrows():

        # Get the Disease Names
        if (row['Disease'] != "\xc2\xa0") and (row['Disease'] != ""):
            disease = row['Disease']
            disease_list = process_data(data=disease)
            count = row['Count of Disease Occurrence']

        # Get the Symptoms Corresponding to Diseases
        if (row['Symptom'] != "\xc2\xa0") and (row['Symptom'] != ""):
            symptom = row['Symptom']
            symptom_list = process_data(data=symptom)
            for d in disease_list:
                for s in symptom_list:
                    disease_symptom_dict[d].append(s)
                disease_symptom_count[d] = count
    for x in disease_symptom_dict:
        for y in disease_symptom_dict[x]:
            if y not in l:
                l.append(y)
    for x in l:
        for y in disease_symptom_dict:
            if x in disease_symptom_dict[y]:
                symptom_dict[x].append(y)

    l = []
    l1 = symptom_dict[symptoms[0]]
    l2 = []
    for i in range(1, len(symptoms)):
        l2 = symptom_dict[symptoms[i]]
        l2 = [value for value in l1 if value in l2]
        l1 = l2.copy()

    return l1
