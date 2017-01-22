 # programe name - game stone ,paper , scissor
 # programmer name - manav patel
 # date & time - 22/01/2017 23:03 
while(1==1):
 print "welcome to game of stone paper scissor"

 print"player1 please enter your input"
 a= int(raw_input("1. stone 2.paper 3.scissor"))
 print"player2 please enter your input"
 b= int(raw_input("1. stone 2.paper 3.scissor"))

 # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 if a==b:
     print "match draw"
     
 elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
      print('player two win!')

 else:
      print('player one wins')
    
           

 # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

