import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate(data):
    avg=np.mean(data['Score'])
    max = np.max(data['Score'])
    min = np.min(data['Score'])
    n = len(data)
    return avg,max,min,n

def create(data):
    # plt.figure(figsize=(8,6))
    # plt.hist(data['Score'],bins=10,edgecolor='black')
    # plt.xlabel('Score')
    # plt.ylabel('Frequency')
    # plt.title("exam")
    # plt.show()

    tp = data[data['Score']>=40]
    plt.figure(figsize=(8,6))
    plt.bar(tp['Name'],tp['Score'],color='green')
    plt.xlabel('Student name')
    plt.ylabel('Score')
    plt.title("top")
    plt.xticks(rotation=45)
    plt.show()

def main():
    exam = pd.read_csv("Exam_scores.csv")
    avg,max,min,n=calculate(exam)
    print("Average - ",avg)
    print("Max - ", max)
    print("min - ", min)
    print("n - ", n)
    create(exam)

if __name__=="__main__":
    main()




