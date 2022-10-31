#Term frequency and Inverted Document frequency python file

import os
from math import *
from colorama import Fore
from wordcloud import STOPWORDS
from nltk.stem import PorterStemmer
stops = set(STOPWORDS)

def colorIs(i):
    if(i%5 == 0):
        return Fore.RED
    elif(i%5 == 1):
        return Fore.GREEN
    elif(i%5 == 2):
        return Fore.YELLOW
    elif(i%5 == 3):
        return Fore.CYAN
    else:
        return Fore.MAGENTA
toStem = PorterStemmer()
print()
print("==========================================================================")
print(f"{Fore.MAGENTA} \t\t\t\tWelcome to tf-IDF computer! \t\t")
set_of_unique_words = set()
print("---------------------------------------------------------------------------")
print(f"{Fore.GREEN}  Please enter the folder location where documents are present")
path = input()
print()
print()
count = 0
# counting the number of documents in the folder
list_of_documents = []
for _ in os.listdir(path):
    if os.path.isfile(os.path.join(path, _)):
        list_of_documents.append(_)
        count += 1
list_of_documents = sorted(list_of_documents)
for fileIs in os.listdir(path):
    fileIs = path + "/" + fileIs
    with open(fileIs,'r',encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                if word not in stops:
                    set_of_unique_words.add(toStem.stem(word))
set_of_unique_words = sorted(set_of_unique_words)

arr = [ [0]*5 for _ in range(len(set_of_unique_words))]

inverseDocFreq = [0]*len(set_of_unique_words)

for i in range(len(set_of_unique_words)):
    noOFDocuments = 0
    current_word = set_of_unique_words[i]
    for j in range(count):
        isThere = False
        with open(path + "/" + list_of_documents[j],"r",encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    if (toStem.stem(word) == current_word):
                        if(isThere == False):
                            noOFDocuments += 1
                            isThere = True
                        arr[i][j] += 1
    inverseDocFreq[i] = log(5/(noOFDocuments+1))
for i in range(len(set_of_unique_words)):
    for j in range(5):
        arr[i][j] *= inverseDocFreq[i]

print(f"{Fore.MAGENTA} \t\t\t\t\t  Tf-IDF Matrix")
print()
for i in range(len(set_of_unique_words)):
    for j in range(5):
        if(arr[i][j]==0):
            print(f"{Fore.WHITE}{round(arr[i][j], 4)}", end=" ")
        elif(arr[i][j] > 0 and arr[i][j] < 0.5):
            print(f"{Fore.RED}{round(arr[i][j],4)}", end = " ")
        elif(arr[i][j] >= 0.5 and arr[i][j] < 1):
            print(f"{Fore.CYAN}{round(arr[i][j],4)}", end = " ")
        elif(arr[i][j] >= 1 and arr[i][j] < 1.5):
            print(f"{Fore.BLUE}{round(arr[i][j],4)}", end = " ")
        else:
            print(f"{Fore.MAGENTA}{round(arr[i][j],4)}", end = " ")
        print("\t\t",end="")
    print()
print("--------------------------------------------------------------------------")
print()
print()

print(f"\t\t\t\t{Fore.RED}Menu")
print()
print(f"\t\t\t{Fore.MAGENTA}1 Single word query")
print(f"\t\t\t{Fore.MAGENTA}2 Multi word query")
print(f"\t\t\t{Fore.MAGENTA}3 Boolean operations")
print(f"\t\t\t{Fore.MAGENTA}-1 Exit")
print()
print()
value = int(input(f"{Fore.WHITE}Enter the option from above table: "))
print()
print()
forColor = 0
while( value != -1):
    if value == 1:
        print(f"{Fore.MAGENTA} \t\t\t\tBasic Retrieval System of Single Word Query \t\t")
        print()
        print(f"{Fore.RED}Note: {Fore.WHITE}If the ranks are equal then documents will be displayed in lexicographic order")
        print()
        word = input("Enter the word: ")
        word = toStem.stem(word.lower())
        dict_ranks = {}
        for i in range(len(set_of_unique_words)):
            if word == set_of_unique_words[i]:
                for j in range(count):
                    dict_ranks[list_of_documents[j]] = arr[i][j]
        ranked_documents = dict(sorted(dict_ranks.items(), key=lambda item: item[1], reverse=True))
        print("--------------------------------------------------------------------------")
        noOF0 = 0
        print("\t\t\t\tRanking the documents")
        print()
        print()
        for i in ranked_documents:
            if(ranked_documents[i] == 0.0):
                noOF0 += 1
            else:
                print(f"\t\t{colorIs(forColor)}{i}")
                forColor += 1
        if(noOF0 == len(ranked_documents)):
            print(f"{Fore.RED}\t\tThe word entered is not present in any document")
        else:
            print()
            print(f"\t\t\t\t\t\t\t\t\t\t{count-noOF0}/{count} documents ranked")
    elif value == 2:
        print("==========================================================================")
        print()
        print(f"{Fore.MAGENTA} \t\t\t\tBasic Retrieval System of Multi Word Query \t\t")
        print()
        print(f"{Fore.RED}Note: {Fore.WHITE}If the ranks are equal then documents will be displayed in lexicographic order")
        print()
        word = input("Enter the query: ")
        word = word.split(' ')
        query = []
        for w in word:
            if w not in stops:
                query.append(toStem.stem(w.lower()))
        query.sort()
        dict_ranks_multi = {}
        index = 0
        for every in query:
            if(every in set_of_unique_words):
                index = set_of_unique_words.index(every)
            for j in range(count):
                if list_of_documents[j] not in dict_ranks_multi:
                    dict_ranks_multi[list_of_documents[j]] = arr[index][j]
                else:
                    dict_ranks_multi[list_of_documents[j]] += arr[index][j]
        ranked_documents_multi = dict(sorted(dict_ranks_multi.items(), key=lambda item: item[1],reverse=True))
        print("--------------------------------------------------------------------------")
        noOF0 = 0
        print("\t\t\t\tRanking the documents")
        print()
        print()
        for i in ranked_documents_multi:
            if(ranked_documents_multi[i] == 0.0):
                noOF0 += 1
            else:
                print(f"\t\t{colorIs(forColor)}{i}")
                forColor += 1
        if(noOF0 == len(ranked_documents_multi)):
            print(f"{Fore.RED}\t\tThe word entered is not present in any document")
        else:
            print()
            print(f"\t\t\t\t\t\t\t\t\t\t{count-noOF0}/{count} documents ranked")
    elif value == 3:
        print("==========================================================================")
        print()
        print(f"{Fore.MAGENTA} \t\t\t\tBoolean Retrieval \t\t")
        print()
        query = []
        print(f"{Fore.RED}Note: {Fore.WHITE}If the ranks are equal then documents will be displayed in lexicographic order")
        print()
        word = input("Enter the query: ")
        word = word.split(' ')
        for w in word:
            query.append(toStem.stem(w.lower()))
        dict_ranks_boolean = {}
        for doc in range(count):
            val1 = query[0]
            index1 = -1
            index2 = -1
            if val1 in set_of_unique_words:
                index1 = set_of_unique_words.index(val1)
            val2 = query[2]
            if val2 in set_of_unique_words:
                index2 = set_of_unique_words.index(val2)
            if(query[1] == 'and') and ((index1!=-1 and arr[index1][doc]!=0.0) and (index2!=-1 and arr[index2][doc]!=0.0)):
                dict_ranks_boolean[list_of_documents[doc]] = arr[index1][doc] + arr[index2][doc]
            elif(query[1] == 'or') and ((index1!=-1 and arr[index1][doc]!=0.0) or (index2!=-1 and arr[index2][doc]!=0.0)):
                if index1!=-1:
                    dict_ranks_boolean[list_of_documents[doc]] = arr[index1][doc]
                if index2!=-1:
                    dict_ranks_boolean[list_of_documents[doc]] += arr[index2][doc]
            elif(query[1] == 'not'):
                if(index2!=-1 and arr[index2][doc] == 0.0):
                    if index1 != -1:
                        dict_ranks_boolean[list_of_documents[doc]] = arr[index1][doc]
        ranked_documents_boolean = dict(sorted(dict_ranks_boolean.items(), key=lambda item: item[1],reverse=True))
        print("--------------------------------------------------------------------------")
        noOF0 = 0
        print("\t\t\t\tRanking the documents")
        print()
        for i in ranked_documents_boolean:
            if(ranked_documents_boolean[i] == 0.0):
                noOF0 += 1
            else:
                print(f"\t\t{colorIs(forColor)}{i}")
                forColor += 1
        if(noOF0 == len(ranked_documents_boolean)):
            print(f"{Fore.RED}\t\tThe word entered is not present in any document")
        else:
            print()
            print(f"\t\t\t\t\t\t\t\t\t\t{forColor}/{count} documents ranked")
    elif value == -1:
        break
    print()
    print()
    print(f"\t\t\t\t{Fore.RED}Menu")
    print()
    print(f"\t\t\t{Fore.MAGENTA}1 Single word query")
    print(f"\t\t\t{Fore.MAGENTA}2 Multi word query")
    print(f"\t\t\t{Fore.MAGENTA}3 Boolean operations")
    print(f"\t\t\t{Fore.MAGENTA}-1 Exit")
    print()
    print()
    value = int(input(f"{Fore.WHITE}Enter the option from above table: "))
    print()
    print()
