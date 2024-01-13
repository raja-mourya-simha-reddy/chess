import pygame
import sys
import threading
from chess import valid
from chess import validvoice
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
send = [[0,0],[0,0]]
class Piece:
    def __init__(self, color, x, y, piece_type):
        self.color = color
        self.x = x
        self.y = y
        self.type = piece_type

    def draw(self, surface):
        img = pygame.image.load(f"images/{self.color}{self.type}.png")
        img = pygame.transform.scale(img,(60,60))
        surface.blit(img, (self.x*75+10, self.y*75+10))
def move(boo,empty,en,cas):
                 print(boo,empty,en,cas)
                 if boo: 
                      if(not empty or en ):
                           print(en)
                           kill(send[1],en) 
                      change(send)
                      print(send)
                      if cas:
                           Rmove(cas)
def change(rec):
     for piece in pieces:
                if piece.x == rec[0][0] and piece.y == rec[0][1]:
                    piece.x = rec[1][0]
                    piece.y = rec[1][1]
                    return
def ispiece(x,y):
    for piece in pieces:
                if piece.x == x and piece.y == y:   
                     return True                 
    return False    
def kill(k,en):
    print(k[0],k[1]+en)
    for piece in pieces:
                if piece.x == k[0] and piece.y == k[1]+en:
                     pieces.remove(piece)
def Rmove(cas):
     if cas==1:
          change([[7,7],[5,7]])
     elif cas==2:
          change([[7,0],[5,0]])
     elif cas==3:
          change([[0,7],[3,7]])
     elif cas==4:
          change([[0,0],[3,0]])           
def recloop():
                 global send      
                 try:
                     print("A moment of silence, please...")
                     with m as source: r.adjust_for_ambient_noise(source)
                     print("Set minimum energy threshold to {}".format(r.energy_threshold))
                     value=None
                     while value!='stop':
                       print("Say something!")
                       with m as source: audio = r.listen(source)
                       print("Got it! Now to recognize it...")
                       try:
                          # recognize speech using Google Speech Recognition
                          value = r.recognize_google(audio)

                          # we need some special handling here to correctly print unicode characters to standard output
                          if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                            print(u"You said {}".format(value).encode("utf-8"))
                            validvoice((value.lower()).replace(" ",""))
                          else:  # this version of Python uses unicode for strings (Python 3+)
                            print("You said {}".format((value.lower()).replace(" ","")))
                            
                            boo,empty,en,cas,send=validvoice( (value.lower()).replace(" ",""))
                            print(boo,empty,en,cas,send,"bruh")
                            move(boo,empty,en,cas)
                       except sr.UnknownValueError:
                         print("Oops! Didn't catch that")
                       except sr.RequestError as e:
                         print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                 except KeyboardInterrupt:
                         pass
                            
pygame.init()

# set up the window
size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")

# set up the board
board = pygame.Surface((600, 600))
board.fill((255, 206, 158))
voice = pygame.Surface((640,40))
voice.fill((225,225,225))

# draw the board
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
        pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

# set up the pieces
pieces = []
for i in range(8):
    pieces.append(Piece("B", i, 1, "P"))
    pieces.append(Piece("W", i, 6, "P"))
pieces.append(Piece("B",0,0,"R"))
pieces.append(Piece("B",1,0,"N"))
pieces.append(Piece("B",2,0,"B"))
pieces.append(Piece("B",3,0,"Q"))
pieces.append(Piece("B",4,0,"K"))
pieces.append(Piece("B",5,0,"B"))
pieces.append(Piece("B",6,0,"N"))
pieces.append(Piece("B",7,0,"R"))

pieces.append(Piece("W",0,7,"R"))
pieces.append(Piece("W",1,7,"N"))
pieces.append(Piece("W",2,7,"B"))
pieces.append(Piece("W",3,7,"Q"))
pieces.append(Piece("W",4,7,"K"))
pieces.append(Piece("W",5,7,"B"))
pieces.append(Piece("W",6,7,"N"))
pieces.append(Piece("W",7,7,"R"))            
# draw the pieces
for piece in pieces:
    piece.draw(board)

# add the board to the screen
screen.blit(board, (20, 40))
screen.blit(voice,(0,0))
img = pygame.image.load("images/mic.png")
img = pygame.transform.scale(img,(40,40))
voice.blit(img, (300, 0))
pygame.display.update()

# main loop
i=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if  event.type == pygame.MOUSEBUTTONDOWN:
            # get the position of the click
            pos = pygame.mouse.get_pos()
            #voice click
            if pos[1]<40 :
                t1=threading.Thread(target=recloop)  
                t1.start() 
                
            # convert the position to board coordinates
            x = (pos[0] - 20) // 75
            y = (pos[1] - 40) // 75           #hereeee
            global a,b
            a,b=x,y
            if i==0 and ispiece(x,y):
                send[i]=[x,y]
                i+=1
            elif i==1 :
                 send[i]=[x,y]
                 boo,empty,en,cas=valid(send)
                 print(boo,empty,en,cas)
                 move(boo,empty,en,cas)
                 i=0        

    # redraw the board and pieces
    board.fill((255, 206, 158))
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
            pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

    for piece in pieces:
        piece.draw(board)

    # add the board to the screen
    screen.blit(board, (20, 40))
    screen.blit(voice,(0,0))
    img = pygame.image.load("images/mic.png")
    img = pygame.transform.scale(img,(40,40))
    voice.blit(img, (300, 0))
    # update the display
    pygame.display.update()




