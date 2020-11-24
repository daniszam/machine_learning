import numpy as np
import pandas as pd

symptom = pd.read_csv('symptom.csv', delimiter=';')
disease = pd.read_csv('disease.csv', delimiter=';')


def get_p(our_symptoms, p_disease):
    for i in range(len(p_disease) - 1):
        for j in range(len(symptom) - 1):
            if our_symptoms[j] == 1:
                p_disease[i] *= float(symptom.iloc[j][i + 1].replace(',', '.'))
    return p_disease


our_symptoms = [np.random.randint(0, 2) for i in range(len(symptom) - 1)]
p_disease = dict(
    zip(disease['Болезнь'], (disease['Количество'] / disease['Количество'][len(disease['Количество']) - 1])))

p_disease_values = list(p_disease.values())
p_disease_values = p_disease_values[:-1]
p = get_p(our_symptoms, p_disease_values.copy())
print(list(p_disease.keys())[p.index(max(p))])