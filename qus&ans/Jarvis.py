import pyttsx
import linecache
engine = pyttsx.init()

rate = engine.getProperty('rate')

engine.setProperty('rate',rate-40)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


while True:
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      string1 =raw_input("").lower()
      for char in string1:
        if char not in punctuations:
            string1= string1 + char 
      if string1 in open("question.txt","r").read():
        file1 = "question.txt"
        with open(file1,"r") as text:
            for num,line in enumerate(text):
                if string1 in line:
                    num
                    k = linecache.getline('answer.txt',num+1)
                    print k
                    engine.say(k)
                    engine.runAndWait()
                    
      else:
        file1 = open("question.txt","a+")
        file1.write(string1+"\n")
        file1.close()

        engine.say("Can You tell me the answer")
        engine.runAndWait()
        

        string2 = raw_input("Can You tell me the answer")
        file2 = open("answer.txt","a+")
        file2.write(string2+"\n")
        file2.close()

     

