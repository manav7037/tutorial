import linecache
while True:
    string1 = raw_input("");
    if string1 == "how are you":
        print("I am fine")
    elif string1 in open("question.txt","r").read():
        file1 = "question.txt"
        with open(file1,"r") as text:
            for num,line in enumerate(text):
                if string1 in line:
                    num
                    k = linecache.getline('answer.txt',num+1)
                    print k 
        
    else:
        file1 = open("question.txt","a+")
        file1.write(string1+"\n")
        file1.close()

        string2 = raw_input("Can You tell me the answer")
        file2 = open("answer.txt","a+")
        file2.write(string2+"\n")
        file2.close()

     
