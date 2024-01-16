import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

filename = 'dashboard 3.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    frequency_uses = []
    frequency_use = int
    for row in reader:
        frequency_use = (row[13])
        frequency_uses.append(frequency_use)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree or Disagree', 'Disagree', 'Strongly Disagree']
    values = ['3', '1', '5', '', '', '', '', '4', '5', '2', '', '5', '', '', '3', '5', '3', '4', '', '5', '5', '5', '5', '']

    # Convert valid values to integers
    valid_values = [int(val) for val in values if val.isdigit()]

    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values = valid_values[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Potential to be used frequently', fontsize=14)


    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    complexities = []
    complexity = int
    for row in reader:
        complexity = (row[14])
        complexities.append(complexity)

def addlabels1(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['3', '', '2', '', '', '', '', '1', '1', '3', '', '1', '', '', '2', '2', '3', '2', '', '2', '3', '1', '1', '']


    valid_values1 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values1 = valid_values1[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values1[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values1[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Complexity of the Dashboard', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ease_of_uses = []
    ease_of_use = int
    for row in reader:
        ease_of_use = (row[15])
        ease_of_uses.append(ease_of_use)

print(ease_of_uses)


def addlabels2(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['2', '', '2', '', '', '', '', '5', '5', '2', '', '5', '', '', '4', '5', '3', '3', '', '5', '4', '5', '5', '']

    valid_values2 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values2 = valid_values2[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values2[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values2[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Ease of Use', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    technical_guidances = []
    technical_guidance = int
    for row in reader:
        technical_guidance = (row[16])
        technical_guidances.append(technical_guidance)

print(technical_guidances)


def addlabels3(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['2', '', '2', '', '', '', '', '2', '2', '3', '', '1', '', '', '2', '2', '2', '3', '', '2', '1', '1', '5', '']

    valid_values3 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values3 = valid_values3[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values3[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values3[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Technical Guidance', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    well_integrated_functions = []
    well_integrated_function = int
    for row in reader:
        well_integrated_function = (row[17])
        well_integrated_functions.append(well_integrated_function)

print(well_integrated_functions)


def addlabels4(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['4', '', '3', '', '', '', '', '1', '1', '4', '', '1', '', '', '2', '3', '3', '2', '', '3', '1', '1', '1', '']

    valid_values4 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values4 = valid_values4[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values4[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values4[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Well-Integrated Functions', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    inconsistencies = []
    inconsistency = int
    for row in reader:
        inconsistency = (row[18])
        inconsistencies.append(inconsistency)

print(inconsistencies)


def addlabels5(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['2', '', '2', '', '', '', '', '2', '2', '3', '', '1', '', '', '2', '2', '2', '3', '', '2', '1', '1', '5', '']

    valid_values5 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values5 = valid_values5[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values5[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values5[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Inconsistencies', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    easy_to_learns = []
    easy_to_learn = int
    for row in reader:
        easy_to_learn = (row[19])
        easy_to_learns.append(easy_to_learn)

print(easy_to_learns)


def addlabels6(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['2', '', '5', '', '', '', '', '5', '5', '3', '', '5', '', '', '4', '5', '3', '3', '', '5', '5', '5', '2', '']

    valid_values6 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values6 = valid_values6[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values6[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values6[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Easy to Learn', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    cumbersome_to_uses = []
    cumbersome_to_use = int
    for row in reader:
        cumbersome_to_use = (row[20])
        cumbersome_to_uses.append(cumbersome_to_use)

print(cumbersome_to_uses)


def addlabels7(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['4', '', '5', '', '', '', '', '1', '1', '4', '', '1', '', '', '2', '2', '3', '2', '', '1', '1', '1', '1', '']

    valid_values7 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values7 = valid_values7[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values7[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values7[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Cumbersome to Use', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    confidences = []
    confidence = int
    for row in reader:
        confidence = (row[21])
        confidences.append(confidence)

print(confidences)


def addlabels8(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['4', '', '5', '', '', '', '', '5', '5', '2', '', '5', '', '', '4', '3', '2', '3', '', '5', '5', '5', '5', '']

    valid_values8 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values8 = valid_values8[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values8[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values8[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Confident to Use', fontsize=14)

    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    prior_knowledges = []
    prior_knowledge = int
    for row in reader:
        prior_knowledge = (row[22])
        prior_knowledges.append(prior_knowledge)

print(prior_knowledges)


def addlabels9(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


if __name__ == '__main__':

    categories = ['Strongly Agree', 'Agree', 'Neither Agree of Disagree', 'Disagree', 'Strongly Disagree']
    values = ['4', '', '4', '', '', '', '', '2', '1', '3', '', '5', '', '', '4', '2', '2', '3', '', '1', '2', '1', '5', '']

    valid_values9 = [int(val) for val in values if val.isdigit()]


    min_length = min(len(categories), len(valid_values))
    categories = categories[:min_length]
    valid_values9 = valid_values9[:min_length]


    sorted_indices = sorted(range(len(valid_values)), key=lambda k: valid_values9[k])
    categories_sorted = [categories[i] for i in sorted_indices]
    values_sorted = [valid_values9[i] for i in sorted_indices]

    plt.figure(figsize=(15, 6))
    plt.bar(categories_sorted, values_sorted, color='skyblue')
    addlabels(categories_sorted, values_sorted)

    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Prior Knowledge', fontsize=14)

    plt.show()


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    service_qualities = []
    service_quality = str
    for row in reader:
        service_quality = (row[23])
        service_qualities.append(service_quality)

print(service_qualities)

rating = ['Excellent', 'Good', 'Fair', 'Poor']
data = [7, 6, 1, 0]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data))))
colors[0] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data, labels=rating, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0.1, 0, 0, 0))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Quality of Service', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    provision_datas = []
    provision_data = str
    for row in reader:
        provision_data = (row[24])
        provision_datas.append(provision_data)

print(provision_datas)

rating1 = ['No, definitely not', 'No, not really', 'Yes, generally', 'Yes, definitely']
data1 = [0, 2, 6, 6]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data1))))
colors[3] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data1, labels=rating1, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0, 0, 0.1))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Provided the needed data', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    data_needs = []
    data_need = str
    for row in reader:
        data_need = (row[25])
        data_needs.append(data_need)

    print(data_needs)

rating2 = ['Almost all of my needs have been met', 'Most of my needs have been met ', 'Only a few of my needs have been met ', 'None of my need have been met']
data2 = [5, 6, 3, 0]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data2))))
colors[1] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data2, labels=rating2, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0.1, 0, 0.0))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Data Need Have been Met', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    recommends = []
    recommend = str
    for row in reader:
        recommend = (row[26])
        recommends.append(recommend)

    print(recommends)

rating3 = ['No, definitely not', 'No, I do not think so ', 'Yes, I think so', 'Yes, definitely']
data3 = [0, 2, 5, 7]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data3))))
colors[3] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data3, labels=rating3, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0, 0, 0.1))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Will Recommend to Friend/Colleague', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    satisfactions = []
    satisfaction = str
    for row in reader:
        satisfaction = (row[27])
        satisfactions.append(satisfaction)

    print(satisfactions)

rating4 = ['Quite dissatisfied ', 'Indifferent or mildly dissatisfied ', 'Mostly satisfied ', 'Very satisfied ']
data4 = [0, 2, 5, 7]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data4))))
colors[3] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data4, labels=rating3, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0, 0, 0.1))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('User Satisfaction on the Data Provided', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    problems = []
    problem = str
    for row in reader:
        problem = (row[28])
        problems.append(problem)

    print(problems)

rating5 = ['Yes, they helped a lot ', 'Yes, they helped somewhat', 'No, they did not help', 'No, they seemed to make things worse']
data5 = [5, 8, 1, 0]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data5))))
colors[1] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data5, labels=rating5, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0.1, 0, 0))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Addressed Data-related problems/concerns', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    overall_satisfactions = []
    overall_satisfaction = str
    for row in reader:
        overall_satisfaction = (row[29])
        overall_satisfactions.append(overall_satisfaction)

    print(overall_satisfactions)

rating6 = ['Very satisfied  ', 'Mostly satisfied ', 'Indifferent or mildly satisfied ', 'Quite dissatisfied ']
data6 = [8, 5, 1, 0]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data6))))
colors[0] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data6, labels=rating6, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0.1, 0, 0, 0))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Overall Satisfaction', fontsize=18)
plt.tight_layout()

plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    realiabilities = []
    reliability = str
    for row in reader:
        realiability = (row[29])
        realiabilities.append(realiability)

    print(realiabilities)

rating7 = ['No, definitely not   ', 'No, I do not think so ', 'Yes, I think so ', 'Yes, definitely ']
data7 = [1, 1, 5, 7]

fig, ax = plt.subplots(figsize=(12, 6))

cmap = plt.get_cmap('CMRmap')
colors = list(cmap(np.linspace(0.45, 0.85, len(data7))))
colors[3] = 'dodgerblue'

patches, texts, pcts = ax.pie(
    data7, labels=rating7, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90,
    colors=colors,

    explode=(0, 0, 0, 0.1))

for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='black')
plt.setp(texts, fontweight=600)
ax.set_title('Reliability', fontsize=18)
plt.tight_layout()

plt.show()





