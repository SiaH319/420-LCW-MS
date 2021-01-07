'''
Sia Ham, 17308123
Tuesday, April 12 
R. Vincent, instructor
Assignment 4 
'''



from extra_trees import extra_trees # suggestion!
from classifier import data_item, normalize_dataset  ##KNN normalize features.
from random import shuffle
from knnclassifier import knnclassifier

fp = open('spambase.data')
dataset = []
for line in fp:
    fields = line.split(',') #each values in each line
    data = [float(x) for x in fields[:-1]] #data without spam indication in a list
    label = int(fields[-1]) #spam = 1 / not spam = 0
    dataset.append(data_item(label, data)) #dataset = [spam, data]

print("Read {} items.".format(len(dataset)))
print("{} features per item.".format(len(dataset[0].data)))

# Add your code here...

def five_fold_random_sampling(dataset, n_folds = 5):
    
    test_size = round(len(dataset) / n_folds) 
    TN = 0 #correct = predicted = 0
    TP = 0 #correct = predicted = 1
    FP = 0 #correct = 0, predicted = 1
    FN = 0 #correct = 1, predicted = 0

    classifier = input("Choose one of the classifiers (extra_trees, KNN):")
    if classifier == "KNN": #normalize the dataset for KNN
        normalize_dataset (dataset)
        K = int(input("Enter the value of K:"))
        dt = knnclassifier(K)
    elif classifier == "extra_trees":
        M = int(input("Enter the number of trees (M):"))
        K = int(input("Enter the number of evaluated size per node (K):"))
        Nmin = int(input("Enter the minimum split size (Nmin):"))
        dt = extra_trees(M, K, Nmin) #create a classifier for each folder
    else:
        print ("please choose one of the given classifiers")

    for fold in range(n_folds): 
        shuffle(dataset) #reshuffle the dataset on every fold
        train_data = dataset[test_size:] #4/5 data = training data
        test_data = dataset[:test_size] #1/5 data = testing data
        
        dt.train (train_data) #train the classifier on the training set
        for t_item in test_data:
            if dt.predict(t_item.data) == t_item.label: #if predicted == correct 
                if t_item.label == 0:
                    TN += 1
                else: #item.label == 1
                    TP +=1
            else: #if predicted != correct 
                if t_item.label == 0: #correct = 0, predicted = 1
                    FP +=1
                else: #correct = 1, predicted = 0
                    FN +=1
    confusion_matrix = [[TN,FN],[FP,TP]]             
    TPR = TP / (TP+FN)
    TNR = TN/(TN+FP)
    FPR = 1-TNR
    return (TPR, FPR, confusion_matrix)

x = 0
while x != "E":
    x = input ("Enter E to stop 5-fold random sub-sampling cross validation:")
    a, b, c= five_fold_random_sampling(dataset)
    print(" TPR =", a, ",", "FPR =", b, "\n", "confusion matrix =", c, "\n")



