"""this is project is basically making a tic tac toe game using python the 
description of eac function is give above the function"""

print("WELCOME TO THE TIC TAC TOE GAAAAAAAAAAAAME!!!")

players1=input("enter the name of player1\n")
players2=input("enter the name of player2\n")
players1="P1_"+players1
players2="p2_"+players2

"""player1 is a function which is used to take input from player 1 it will take input as 
the position in the matrix where he want to enter"""
def player1():
    print(players1,": enter row and coloumn")
    r=int(input())
    c=int(input())
    return r-1,c-1

"""player2 is a function which is used to take input from player 2 it will take input as 
the position in the matrix where he want to enter"""
def player2():
     print(players2,": enter row and column")
     r=int(input())
     c=int(input())
     return r-1,c-1

"""game(playerr1,playerr2) is the function which is the main game the different constraints
playing and wining is defined iniside this function"""    
def game(playerr1,playerr2):
    if(input("press any key to start the game...")):
        k=0
        cnt=0
        while(k!=1):
            cnt=cnt+1
            for i in l:
                print(i)
            m=0
            while(m!=1):#input from first player
                r1,c1=playerr1()
                if l[r1][c1]=='O':
                    print(players2," have entered here, please enter again: ")
                elif l[r1][c1]=='X':
                    print("you yourself entered here, please enter again: ")
                else:
                    l[r1][c1]='X'
                    m=1
            m=0
            while(m!=1):#input from second player
                r2,c2=playerr2()
                if l[r2][c2]=='X':
                    print(players1," have entered here, please enter again: ")
                    
                elif l[r2][c2]=='O':
                    print("you yourself have entered here, please enter again: ")
                else:
                    l[r2][c2]='O'
                    m=1
            if(cnt>=3):        
                #wining condition-comparing through rows
                for i in l:
                    #for player 1
                    c=0
                    for j in range(len(i)):
                        if(i[j]=='X'):
                            c=c+1
                    if(c==3):
                        print("congratulations!!\n",players1," has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                    #for player 2
                    c=0
                    for j in range(len(i)):
                        if(i[j]=='O'):
                            c=c+1
                    if(c==3):
                        print("congratulations!!\n",players2," has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                   
                if(k==1):
                    continue
                
                #wining condition-comparing through column
                for i in range(3):
                    #player 1
                    c=0
                    for j in range(3):
                        if l[j][i]=='X':
                            c=c+1
                            
                    if(c==3):
                        print("congratulations!!\n",players1," has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                    #player 2
                    c=0
                    for j in range(3):
                        if l[j][i]=='O':
                            c=c+1
                            
                    if(c==3):
                        print("congratulations!!\n",players2," has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                if(k==1):
                    continue
                
                #wining condition-comparing through daigonal1
                c=0
                i=0
                j=0
                #for player 1
                for g in range(3):
                    if(l[i][j]=='X'):
                        c=c+1
                    i=i+1
                    j=j+1
                if(c==3):
                    print("congratulations!!\n",players1," has won: ")
                    for g in l:
                        print(g)
                        k=1
                    continue
                        
                c=0
                i=0
                j=0
                # for player 2
                for g in range(3):
                    if(l[i][j]=='O'):
                        c=c+1
                    i=i+1
                    j=j+1
                if(c==3):
                    print("congratulations!!\n",players2," has won: ")
                    for g in l:
                        print(g)
                        k=1
                    continue
                
                #wining condition-comparing through daigonal2
                c=0
                i=0
                j=2
                #for player 1
                for g in range(3):
                    if(l[i][j]=='X'):
                        c=c+1
                    i=i+1
                    j=j-1
                if(c==3):
                    print("congratulations!!\n",players1," has won: ")
                    for g in l:
                        print(g)
                        k=1
                    continue
                        
                c=0
                i=0
                j=2
                # for player 2
                for g in range(3):
                    if(l[i][j]=='O'):
                        c=c+1
                    i=i+1
                    j=j-1
                if(c==3):
                    print("congratulations!!\n",players2," has won: ")
                    for g in l:
                        print(g)
                        k=1
                    continue


l=[]
#p=[]
for i in range(3):
    l1=[]
    p1=[]
    for j in range(3):
        l1.append(0)
        #p1.append(j+1)
    l.append(l1)
    #p.append(p1)
print("who want to start first: \n1.",players1,"\n2.",players2)
ch=int(input())
if ch==1:
    game(player1,player2)
else:
    game(player2,player1)
            
                
                 
                             
                             
                         
                
                
                    
                        
                
            
            
        
        
    