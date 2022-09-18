import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
breast_cancer_data = load_breast_cancer()
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target,test_size = 0.2, random_state = 100)

print(len(training_data),len(training_labels))
print(len(validation_data),len(validation_labels))
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(training_data,training_labels)
print(classifier.score(validation_data,validation_labels))
Best_accuracy = 0
Best_K = 0
for i in range(1,100):
  classifier = KNeighborsClassifier(n_neighbors = i)
  classifier.fit(training_data,training_labels)
  accuracy = classifier.score(validation_data,validation_labels)
  if (accuracy > Best_accuracy):
    Best_accuracy = accuracy
    Best_K = i
print(Best_accuracy)
print(Best_K)

import matplotlib.pyplot as plt
Ks = []
Accuracies = []
for i in range(1,100):
  classifier = KNeighborsClassifier(n_neighbors = i)
  classifier.fit(training_data,training_labels)
  accuracy = classifier.score(validation_data,validation_labels)
  Ks.append(i)
  Accuracies.append(accuracy)

plt.plot(Ks, Accuracies)
plt.title('Breast Cancer Research')
plt.xlabel('K numbers')
plt.ylabel('Accuracy')
plt.show()
