import string
import socket
import os

def main():
    outputresult = open("/home/output/outputresult.txt", "w+")
    path = "/home/data"
    dir_list = os.listdir(path)

    outputresult.write("Files in ")
    outputresult.write(path)
    for dir in dir_list:
        outputresult.write(" \n")
        outputresult.write(dir)

    IF_file = open('/home/data/IF.txt','r')
    data = IF_file.read()
    word_IF_file=data.split()

    Lime_file = open('/home/data/Limerick.txt','r')
    data = Lime_file.read()
    word_Lime_file=data.split()

    outputresult.write(" \n")
    outputresult.write("word count in Limerick "+str(len(word_Lime_file)))
    word_IF=[]

    for word in word_IF_file:
        w=word.translate(str.maketrans('', '', string.punctuation))
        w=w.capitalize()
        word_IF.append(w)

    outputresult.write(" \n")
    outputresult.write("word count in IF: "+str(len(word_IF)))
    outputresult.write(" \n")
    outputresult.write(" Total word count in both files: "+str(len(word_IF) + len(word_Lime_file)))

    count_IF = []
    unique = set(word_IF)

    for word in unique: 
        count_IF.append(word_IF.count(word))
    word_IF = list(set(word_IF))
    order_count_IF= sorted(count_IF,reverse=True)
    outputresult.write("\n")
    outputresult.write("Top 3 words with most word counts in IF")
    
    j=0
    for j in range(0,3):
         for i in range(0,len(count_IF)):
             if(count_IF[i]== order_count_IF[j]):
                 outputresult.write("\n")
                 outputresult.write(""+word_IF[i]+" - "+ str(count_IF[i]) )

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    outputresult.write("\n")
    outputresult.write(" IP Address:" + IPAddr) 
    outputresult.close()
    result_file = open('/home/output/outputresult.txt','r')
    data_result = result_file.read()
    print(data_result)
             

if __name__ == "__main__":
    main()

