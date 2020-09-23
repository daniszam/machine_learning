import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

vowels = ("A", "E", "I", "O", "U", "Y")


def main():
    names = pd.read_csv("./test.csv", usecols=['Name', "Age", "Fare"])

    vowel_names_age = []
    consonants_names_age = []

    vowel_names_fare = []
    consonants_names_fare = []

    for index, row in names.iterrows():
        if (start_with_vowel(row['Name'])):
            vowel_names_age.append(row['Age'])
            vowel_names_fare.append(row['Fare'])
        else:
            consonants_names_age.append(row['Age'])
            consonants_names_fare.append(row['Fare'])

    fig, ax = plt.subplots()
    plt.xlabel('Fare')
    plt.ylabel('Age')

    ax.bar(vowel_names_fare, vowel_names_age, color='green', width=5)
    ax.bar(consonants_names_fare, consonants_names_age, color='blue', width=1.5)

    green_patch = mpatches.Patch(color='green', label='People with name start from vowel')
    blue_patch = mpatches.Patch(color='blue', label='People with name start from consonants')
    plt.legend(handles=[green_patch, blue_patch])

    plt.show()


def start_with_vowel(name: str) -> bool:
    return name.upper().startswith(vowels)


main()
