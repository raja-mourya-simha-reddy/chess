board={"a8":"|bR","b8":"|bN","c8":"|bB","d8":"|bQ","e8":"|bK","f8":"|bB","g8":"|bN","h8":"|bR"
       ,"a7":"|bp","b7":"|bp","c7":"|bp","d7":"|bp","e7":"|bp","f7":"|bp","g7":"|bp","h7":"|bp"
       ,"a6":"|  ","b6":"|  ","c6":"|  ","d6":"|  ","e6":"|  ","f6":"|  ","g6":"|  ","h6":"|  "
       ,"a5":"|  ","b5":"|  ","c5":"|  ","d5":"|  ","e5":"|  ","f5":"|  ","g5":"|  ","h5":"|  "
       ,"a4":"|  ","b4":"|  ","c4":"|  ","d4":"|  ","e4":"|  ","f4":"|  ","g4":"|  ","h4":"|  "
       ,"a3":"|  ","b3":"|  ","c3":"|  ","d3":"|  ","e3":"|  ","f3":"|  ","g3":"|  ","h3":"|  "
       ,"a2":"|wp","b2":"|wp","c2":"|wp","d2":"|wp","e2":"|wp","f2":"|wp","g2":"|wp","h2":"|wp"
       ,"a1":"|wR","b1":"|wN","c1":"|wB","d1":"|wQ","e1":"|wK","f1":"|wB","g1":"|wN","h1":"|wR"}
wpos={"R":["a1",'h1','a','a'],"N":["b1","g1",'a','a'],"B":["c1",'f1','a','a'],"Q":["d1"," ",'a',' '],"K":["e1"," ",'a',' ']}
bpos={"R":["a8",'h8','a','a'],"N":["b8","g8",'a','a'],"B":["c8",'f8','a','a'],"Q":["d8"," ",'a',' '],"K":["e8"," ",'a',' ']}
ill=False
bcas=[1,1,1]
wcas=[1,1,1]
start=[0,0]
end=[0,0]
gep=0
def showboard():
 for x in board.items() :
    print(x[1],end="")
    if x[0][0]=='h':
      print("|")


def makemove(s,e): 
   global start,end
   dic={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
   start=[dic[s[0]],8-int(s[1])]
   end=[dic[e[0]],8-int(e[1])] 
   board[e]=board[s]
   board[s]="|  "
def morph(s,e):
   global start,end
   dic={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
   start=[dic[s[0]],8-int(s[1])]
   end=[dic[e[0]],8-int(e[1])] 
    

        
        
def kill(k,c,s):
  if board[k][2]!='p': 
   if(c=="w"): 
    if bpos[board[k][2]][0]==k:
                   bpos[board[k][2]][2]=s
    else:
                   bpos[board[k][2]][3]=s
   else:
     if wpos[board[k][2]][0]==k:
                   wpos[board[k][2]][2]=s
     else:
                   wpos[board[k][2]][3]=s   


def Bisvalid(s,e):    
    if abs(ord(s[0])-ord(e[0]))==abs(int(s[1])-int(e[1])):
         if (int(s[1])>int(e[1])) == (ord(s[0])>ord(e[0])): 
           if int(s[1])>int(e[1]):
               f=e
           else:
               f=s
           for i in range(1,abs(int(s[1])-int(e[1]))): 
            if board[chr(ord(f[0])+i)+str(int(f[1])+i)]!="|  ":
               return False
         else:
           if int(e[1])>int(s[1]):
              f=e
           else:
              f=s
           for i in range(1,abs(int(s[1])-int(e[1]))):
            if board[chr(ord(f[0])+i)+str(int(f[1])-i)]!="|  ":
               return False
         return True     
    else:
        return False
    

def Risvalid(s,e):                                         #remove redundancy
    if (s[0]==e[0]):
        if int(s[1])>int(e[1]):                           
            f=s
        else:
            f=e    
        for i in range(1,abs(int(s[1])-int(e[1]))):          #take variable for this with if 
                if board[f[0]+str(int(f[1])-i)]!="|  ":
                    return False
        return True        
    elif s[1]==e[1]:
         if ord(s[0])>ord(e[0]):
            f=s
         else:
            f=e    
         for i in range(1,abs(ord(s[0])-ord(e[0]))):
                if board[chr(ord(f[0])-i)+f[1]]!="|  ":
                    return False          
         return True       
    else:
        return False  
def Nisvalid(s,e):
    a= abs(ord(s[0])-ord(e[0]))
    b= abs(int(s[1])-int(e[1]))
    if( (a in[1,2]) and (b in[1,2]) and a!=b):
        return True
    else:
        return False

def Kisvalid(s,e):
      if(abs(ord(s[0])-ord(e[0]))in[0,1] and abs(int(s[1])-int(e[1]))in [0,1]):
          return True
      else:
          return False
        

def move(p,ip,f,o,c):
    k=0
    m=0
    mm=0
    if(ip.__len__()==3) and board[ip[1:]]=="|  ":
         x=1
    elif ip[1]=='x'and board[ip[2:]][1]==o:
         x=2
         k=1
    elif ip.__len__()==4 and board[ip[2:]]=="|  ":
         x=2
         m=1
    elif ip[2]=='x' and board[ip[3:]][1]==o:
         x=3
         m=1
         k=1     
    elif ip.__len__()==5 and board[ip[3:]]=="|  ":
         x=3
         mm=1
    elif ip[3]=='x' and board[ip[4:]][1]==o:
         x=4
         mm=1
         k=1    
    else:
         return False
   
    if c=="w": 
          if wpos[p][2]=='a'and (not (mm and ( wpos[p][1]==ip[1]+ip[2])))and(not (m and (wpos[p][1][0]==ip[1] or wpos[p][1][1]==ip[1]))) and globals()[f+"isvalid"](wpos[p][0],ip[x:]) :      #try after move in check method for pin 
             if k:
               kill(ip[x:],c,'d')
             ts=board[wpos[p][0]]
             te=board[ip[x:]]
             makemove(wpos[p][0],ip[x:])
             global pmov
             twpos=wpos[p][0]
             wpos[p][0]=ip[x:]
             if InCheck(twpos,ip[x:],c,o,p):
                 wpos[p][0]=twpos
                 board[wpos[p][0]]=ts
                 board[ip[x:]]=te
                 if k:
                   kill(ip[x:],c,'a')
                 return False
             pmov = [twpos,ip[x:],p]
             if p=='K': wcas[1]=0
             elif p=='R': wcas[0]=0
          elif wpos[p][3]=='a' and globals()[f+"isvalid"](wpos[p][1],ip[x:]) :      #try after move in check method for pin  
             if k:
              kill(ip[x:],c,'d')
             ts=board[wpos[p][1]]
             te=board[ip[x:]]
             makemove(wpos[p][1],ip[x:])
             twpos=wpos[p][1]
             wpos[p][1]=ip[x:]
             print(twpos,ip[x:],c,o)
             if InCheck(twpos,ip[x:],c,o,p):
                  
                 wpos[p][1]=twpos
                 board[wpos[p][1]]=ts
                 board[ip[x:]]=te
                 if k:
                    kill(ip[x:],c,'a')
                   
                 return False
             pmov = [twpos,ip[x:],p] 
             if p=='R': wcas[0]=0
             elif p=='K':wcas[2]=0
          else:
            return False
    else:
            if bpos[p][2]=='a'and (not (mm and ( bpos[p][1]==ip[1]+ip[2]))) and(not (m and (bpos[p][1][0]==ip[1] or bpos[p][1][1]==ip[1]))) and globals()[f+"isvalid"](bpos[p][0],ip[x:]):  
               if k:
                 kill(ip[x:],c,'d')
               ts=board[bpos[p][0]]
               te=board[ip[x:]]
               makemove(bpos[p][0],ip[x:])
               twpos=bpos[p][0]
               bpos[p][0]=ip[x:]
               if InCheck(twpos,ip[x:],c,o,p):
                 bpos[p][0]=twpos
                 board[bpos[p][0]]=ts
                 board[ip[x:]]=te
                 if k:
                   kill(ip[x:],c,'a')
                 return False
               pmov = [twpos,ip[x:],p]  
               if p=='R': bcas[0]=0
               elif p=='K':bcas[1]=0
            elif bpos[p][3]=='a' and globals()[f+"isvalid"](bpos[p][1],ip[x:]):
                 if k:
                  kill(ip[x:],c,'d') 
                 ts=board[bpos[p][1]]
                 te=board[ip[x:]]
                 makemove(bpos[p][1],ip[x:])
                 twpos=bpos[p][1]
                 bpos[p][1]=ip[x:]
                 if InCheck(twpos,ip[x:],c,o,p):
                   bpos[p][1]=twpos
                   board[bpos[p][1]]=ts
                   board[ip[x:]]=te
                   if k:
                     kill(ip[x:],c,'a')
                   return False
                 pmov = [twpos,ip[x:],p]
                 if p=='R':bcas[2]=0    
            else:
               return False  
    return True           
def InCheck(s,e,c,o,p):               ####can optimize with pe in pp ,seperate code                  #pin or check
    global pmov
    ps=pmov[0]
    pe=pmov[1]                                #todo: optimize using this,pin using s and pawn pin and check
    pp=pmov[2]                                #todo: kill and revert, pawn thing.
    ck={'b':bpos["K"][0],'w':wpos["K"][0]}    #final todo: pawn check(done),en passant(done),castling(done),multimoves(done),promotion,checkmate,stalemate,repetation,50moves
                                              #: king moves into check(done):- flag;p==K ,check all pieces isvalid method
                                              #king moves into check
    if p=='K':
         if (globals()[o+"pos"]['B'][2]=='a'and Bisvalid(globals()[o+"pos"]["B"][0],ck[c])) or   (globals()[o+"pos"]['B'][3]=='a'and Bisvalid(globals()[o+"pos"]["B"][1],ck[c])) or (globals()[o+"pos"]['Q'][2]=='a'and Bisvalid(globals()[o+"pos"]["Q"][0],ck[c])) or\
            (globals()[o+"pos"]['R'][2]=='a'and Risvalid(globals()[o+"pos"]["R"][0],ck[c])) or   (globals()[o+"pos"]['R'][3]=='a'and Risvalid(globals()[o+"pos"]["R"][1],ck[c])) or (globals()[o+"pos"]['Q'][2]=='a'and Risvalid(globals()[o+"pos"]["Q"][0],ck[c])) or\
            (globals()[o+"pos"]['N'][2]=='a'and Nisvalid(globals()[o+"pos"]["N"][0],ck[c])) or   (globals()[o+"pos"]['N'][3]=='a'and Nisvalid(globals()[o+"pos"]["N"][1],ck[c])) or \
            (ord(e[0])<104 and board[chr(ord(e[0])+1)+str(int(e[1])+(c=='w')-(c=='b'))]=='|'+o+'p') or ( ord(e[0])>97 and board[chr(ord(e[0])-1)+str(int(e[1])+(c=='w')-(c=='b'))]=='|'+o+'p' ) or Kisvalid(ck[o],ck[c]):
             return True 
    #pin and discovery
    if  abs(ord(s[0])-ord(ck[c][0]))==abs(ord(s[1])-ord(ck[c][1])) or abs(ord(ps[0])-ord(ck[c][0]))==abs(ord(ps[1])-ord(ck[c][1])):
         if (globals()[o+"pos"]['B'][2]=='a'and Bisvalid(globals()[o+"pos"]["B"][0],ck[c])) or   (globals()[o+"pos"]['B'][3]=='a'and Bisvalid(globals()[o+"pos"]["B"][1],ck[c])) or (globals()[o+"pos"]['Q'][2]=='a'and Bisvalid(globals()[o+"pos"]["Q"][0],ck[c])) :
             return True
    elif  (s[0]==ck[c][0] or s[1]==ck[c][1]) or (ps[0]==ck[c][0] or ps[1]==ck[c][1]) :
         if (globals()[o+"pos"]['R'][2]=='a'and Risvalid(globals()[o+"pos"]["R"][0],ck[c])) or   (globals()[o+"pos"]['R'][3]=='a'and Risvalid(globals()[o+"pos"]["R"][1],ck[c]))  or (globals()[o+"pos"]['Q'][2]=='a'and Risvalid(globals()[o+"pos"]["Q"][0],ck[c])):
             return True
    #direct check from previous piece    
    if  pp=='N':
         if Nisvalid(pe,ck[c]) and board[pe][1]!=c:          
             return True    
    elif pp == 'B':
        if Bisvalid(pe,ck[c])and board[pe][1]!=c:
            return True
    elif pp == 'R':
        if Risvalid(pe,ck[c])and board[pe][1]!=c:
            return True
    elif pp=='Q':
         if (Bisvalid(pe,ck[c]) or Risvalid(pe,ck[c])) and board[pe][1]!=c:
             return True       
    elif pp=='p' and board[pe][1]!=c:
         if((ord(pe[0])<104 and board[chr(ord(pe[0])+1)+str(int(pe[1])+(o=='w')-(o=='b'))]=='|'+c+'K') or( ord(pe[0])>97 and board[chr(ord(pe[0])-1)+str(int(pe[1])+(o=='w')-(o=='b'))]=='|'+c+'K' )):
           return True   
    return False

def updateboard(ip,c,o):
    global ill,pmov,start,end,gep    
    if ip.__len__()==2:                        #pawn move    (recheck){TRY IF ALLOWED , MAKE MOVE STYLE}
          try:
           if board[ip]=="|  ":
             if board[ip[0]+str(int(ip[1])-(c=="w")+(c=="b"))]=='|'+c+'p' :
                
                board[ip[0]+str(int(ip[1])-(c=="w")+(c=="b"))]="|  "
                board[ip]='|'+c+'p'
                
                if InCheck(ip[0]+str(int(ip[1])-(c=="w")+(c=="b")),ip,c,o,'p'):
                    ill=True
                    board[ip[0]+str(int(ip[1])-(c=="w")+(c=="b"))]='|'+c+'p'
                    board[ip]="|  "
                else:    
                    pmov=[ip[0]+str(int(ip[1])-(c=="w")+(c=="b")),ip,'p'] 
                    morph(ip[0]+str(int(ip[1])-(c=="w")+(c=="b")),ip)
             elif ip[1]=='4' and c=='w' and board[ip[0]+'2']=='|wp' and board[ip[0]+'3']=="|  ":
                
                board[ip[0]+'2']="|  "
                board[ip]='|wp'
                if InCheck(ip[0]+'2',ip,c,o,'p'):
                    ill=True
                    board[ip[0]+'2']='|wp' 
                    board[ip]="|  "
                else:    
                    pmov=[ip[0]+'2',ip,'p']
                    morph(ip[0]+'2',ip)
             elif ip[1]=='5' and c=='b' and board[ip[0]+'7']=='|bp' and board[ip[0]+'6']=="|  ":
                
                board[ip[0]+'7']="|  " 
                board[ip]='|bp'
                if InCheck(ip[0]+'7',ip,c,o,'p'):
                    ill=True
                    board[ip[0]+'7']='|bp'
                    board[ip]="|  "
                else:    
                    pmov=[ip[0]+'7',ip,'p']
                    morph(ip[0]+'7',ip)     
             else:
                ill=True
                print("ILLEGAL MOVE")
            
           else: 
              ill=True
              print("ILLEGAL MOVE")      
            #   break
          except KeyError:
              ill=True
              print("keybruh")    
   #  elif ip[1]=='x':                                   #CAPTURES
    elif ip[0] in ['a','b','c','d','e','f','g','h']:  #pawn takes (implement en passant(done), pin(done),in-check(done))
         cl={'w':['2','4'],'b':['7','5']}
         print(pmov,cl[o][0])                                             #todo: try catch keyerror here ip:d4e,,,,, board[ip[2]+str(cl[c][1])]=='|'+o'p' 
         try: 
          if ((board[ip[2:]][1]== o or (pmov[2]=='p' and pmov[0]==ip[2]+cl[o][0] and pmov[1]==ip[2]+cl[o][1] ))) and (abs(ord(ip[0])-ord(ip[2]))==1) and (board[ip[0]+str(int(ip[3])-(c=="w")+(c=="b"))]=='|'+c+"p"):
 
           if(not board[ip[2:]][1]== o ):
               board[pmov[1]]='|  '
               gep= 1 if c=='w' else -1
           else:    
               tem=board[ip[2:]]
               kill(ip[2:],c,'d')
           board[ip[2:]]="|"+c+"p"
           board[ip[0]+str(int(ip[3])-(c=="w")+(c=="b"))]="|  "
           if InCheck(ip[0]+str(int(ip[3])-(c=="w")+(c=="b")),ip[2:],c,o,'p'):
               if(board[ip[2:]]== "|  " ):
                   board[pmov[1]]='|'+o+'p'
                   board[ip[2:]]='|  '
                   gep=0
               else:   
                   kill(ip[2:],c,'a')
                   board[ip[2:]]=tem
               board[ip[0]+str(int(ip[3])-(c=="w")+(c=="b"))]="|"+c+"p"
               ill=True
           else:    
                    pmov=[ip[0]+str(int(ip[3])-(c=="w")+(c=="b")),ip[2:],'p']
                    morph(ip[0]+str(int(ip[3])-(c=="w")+(c=="b")),ip[2:])   
          else:
             ill = True
             print("ILLEGAL MOVE ")
         except KeyError:
            ill=True
            print("keybruh")

    elif ip[0]=='B':   
        if not move('B',ip,'B',o,c):                         #bishop move
            ill=True
            print("ILLEGAL MOVE")

    elif ip[0]=='R': 
        if not move("R",ip,'R',o,c):                            #rook move
            ill=True
            print("ILLEGAL MOVE")

    elif ip[0]=='Q':                                     #queen move            #todo:in-check,mate,castle,enpassant,promote,stalemate
         if (not move('Q',ip,'R',o,c))and(not move('Q',ip,'B',o,c)):
            ill=True
            print("ILLEGAL MOVE")                                              #maybe: shift ill to while,redundancy check
    elif ip[0]=='N':
         if(not move('N',ip,'N',o,c)):
             ill=True
             print("ILLEGAL MOVE")   
    elif ip[0]=='K':
         if(not move('K',ip,'K',o,c)):
             ill = True
             print("ILLEGAL MOVE") 
                  
    elif ip=='o-o':
        if c=='w':
            if wcas[1] and wcas[2] and wpos["R"][3]=='a' and board['f1']=='|  ' and board['g1']=='|  ':
                wpos["K"][0]='f1'
                board['e1']='|  '
                board['f1']='|wK'
                if InCheck('e1','f1','w','b','K'):
                   wpos['K'][0]='e1'
                   board['e1']='|wK'
                   board['f1']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                wpos["K"][0]='g1'
                board['f1']='|  '
                board['g1']='|wK'
                if InCheck('e1','g1','w','b','K'):
                   wpos['K'][0]='e1'
                   board['e1']='|wK'
                   board['g1']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                board['f1']='|wR'
                board['h1']='|  '
            else:
                ill=True
                print("ILLEGAL MOVE")
        else:
            if bcas[1] and bcas[2] and bpos["R"][3]=='a' and board['f8']=='|  ' and board['g8']=='|  ':
                bpos["K"][0]='f8'
                board['e8']='|  '
                board['f8']='|bK'
                if InCheck('e8','f8','b','w','K'):
                   bpos['K'][0]='e8'
                   board['e8']='|bK'
                   board['f8']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                bpos["K"][0]='g8'
                board['f8']='|  '
                board['g8']='|wK'
                if InCheck('e8','g8','b','w','K'):
                   bpos['K'][0]='e8'
                   board['e8']='|bK'
                   board['g8']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                board['f8']='|bR'
                board['h8']='|  ' 
            else:
                ill=True
                print("ILLEGAL MOVE")   
    elif ip=='o-o-o':
         if c=='w':
            if wcas[1] and wcas[0] and wpos["R"][2]=='a' and board['d1']=='|  ' and board['c1']=='|  ' and board['b1']=='|  ':
                wpos["K"][0]='d1'
                board['e1']='|  '
                board['d1']='|wK'
                if InCheck('e1','d1','w','b','K'):
                   wpos['K'][0]='e1'
                   board['e1']='|wK'
                   board['d1']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                wpos["K"][0]='c1'
                board['d1']='|  '
                board['c1']='|wK'
                if InCheck('e1','d1','w','b','K'):
                   wpos['K'][0]='e1'
                   board['e1']='|wK'
                   board['c1']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                board['d1']='|wR'
                board['a1']='|  '
            else:
                ill=True
                print("ILLEGAL MOVE")
         else:
            if bcas[1] and bcas[0] and bpos["R"][2]=='a' and board['d8']=='|  ' and board['c8']=='|  ' and board['b8']=='|  ':
                bpos["K"][0]='d8'
                board['e8']='|  '
                board['d8']='|bK'
                if InCheck('e8','d8','b','w','K'):
                   bpos['K'][0]='e8'
                   board['e8']='|bK'
                   board['d8']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                bpos["K"][0]='c8'
                board['d8']='|  '
                board['c8']='|bK'
                if InCheck('e8','c8','b','w','K'):
                   bpos['K'][0]='e8'
                   board['e8']='|bK'
                   board['c8']='|  '
                   ill=True
                   print("ILLEGAL MOVE")          
                   return
                board['d8']='|bR'
                board['a8']='|  ' 
    else:
        ill=True
        print("ILLEGAL MOVE")                   
               
c="b"
o="w"
pmov=['g8','f6','N']
# while(True):                                      #MAIN LOOP for standalone mode
#    if(not ill):         #ILLEGAL MOVE, no swap
#       if(c=="b"):       #turn swap
#          c="w"          #current color
#          o="b"          #opponent color  
#       else:
#          c="b"
#          o="w"   
#    else:
#       print("ILLEGAL MOVE")
#       ill=False         
#    if(c=="w"):
#        print("enter x to exit")
#        ip=input("white move:")
       
#    else:
#        print("enter x to exit")
#        ip=input("black move:")
       
#    if ip=="x":
#       break
#    updateboard(ip,c,o)
#    showboard()     
def validvoice(inp):
    global ill,c,o,start,end,gep
    empty=True
    if inp[0]=='b' and inp[1] in ['1','2','3','4','5','6','7','8','x']:
        pass
    elif inp[0] in ['n','r','k','b','q']:
        inp=inp.capitalize()
    if 'x' in inp:
        empty=False    
    if(not ill):         #ILLEGAL MOVE, no swap
      if(c=="b"):       #turn swap
         c="w"          #current color
         o="b"          #opponent color  
      else:
         c="b"
         o="w"   
    else:
      print("ILLEGAL MOVE")
      ill=False         
    updateboard(inp,c,o)
    showboard() 
    return not ill, empty,gep,0,[start,end]
dic = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
def valid(send):
    global ill,c,o
    print(send)
    ep=0
    cas=0
    if(not ill):         #ILLEGAL MOVE, no swap
      if(c=="b"):       #turn swap
         c="w"          #current color
         o="b"          #opponent color  
      else:
         c="b"
         o="w"   
    else:
      print(" prev ILLEGAL MOVE")
      ill=False         
    if(c=="w"):
       print("white move")
       
    else:
       print("balck move")
    ps=dic[send[0][0]]+str(8-send[0][1])
    pe=dic[send[1][0]]+str(8-send[1][1])
    p=board[ps][2]
    c2=board[ps][1]
    if c!=c2:
        ill=True
        return False,False,False,False
    empty=board[pe]=='|  '
    if(p=='p'):
        if(not empty or pe[0]!=ps[0]):
            ip=ps[0]+'x'+pe
            if empty:
                ep= 1 if c=='w' else -1
                print(ep) 
        else:
            ip=pe
    elif(p=='K' and ((ps=='e1'and pe=='g1')or(ps=='e8'and pe=='g8'))):
        ip='o-o'
        if c=='w':
            cas=1
        else:
            cas=2  
    elif(p=='K'and ((ps=='e1'and pe=='c1')or(ps=='e8'and pe=='c8'))):
        ip='o-o-o'
        if c=='w':
            cas=3
        else:
            cas=4                      
    elif(not empty):
        ip=p+ps+'x'+pe
    else:
        ip=p+ps+pe   
    
    updateboard(ip,c,o)
    showboard()
    return (not ill ,empty,ep,cas) 
     

         