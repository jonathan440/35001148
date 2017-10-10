from tkinter import *
from threading import Thread , Condition
from time import *
import time
import random



class balles:
    def __init__(self,rayon,dx,dy):
        

        self.rayon = rayon
        self.px = random.randint(0,(W-self.rayon))
        self.py = random.randint(0,(H-self.rayon))
        self.dx = dx
        self.dy = dy
       
        
            
         
    
        self.px = random.randint(0,(W-self.rayon))
        self.py = random.randint(0,(H-self.rayon))
        color=['purple','cyan','maroon','green','red','blue','orange','yellow']
        couleur  =  color[random.randint(0,7)]
        self.ball = canvas.create_oval(self.px,self.py,self.px+self.rayon,self.py+self.rayon,fill=couleur)
    
       
        
    def move(self):
        
        

        print(" Check_collision")
        if (canvas.coords(self.ball)[3]) > 400 or (canvas.coords(self.ball)[1]) < 0:
            self.dy = -1*self.dy
                
        if(canvas.coords(self.ball)[2] > 500) or (canvas.coords(self.ball)[0]) < 0:
            self.dx= -1*self.dx
                    
        canvas.move(self.ball,self.dx,self.dy)

            
    

    
    def Clear(self):
        print("Done")
        canvas.delete(self.ball)


 
        

class timer:

    def __init__(self):
        self.s = 0
        self.horloge=Label(fenetre,text="T = 0s")
        self.horloge.pack()
        

    def chrono(self):
        self.horloge["text"] = "T: " +str(self.s)+" s  "
        self.s +=1

            
        
        #fenetre.after(1000,self.chrono)
        
         
        
       

            
                
            

    
class Thread1(Thread):
    def __init__(self, b, tempsSommeil, nom,liste):
        Thread.__init__(self)
        self.b = b
        self.tempsSommeil = tempsSommeil
        self.name = nom
        self.daemon = True
        self.l = liste
        

         
    
    
        

    def run(self):
        
        while True:
            if(T2.Begin):
                print("run")
                self.b.move()

                
                
                #collision balles
                """for i in range(len(self.l)):
                    for j in range(len(self.l)):
                        if(i != j):
                            px2 = self.l[j].px + 25
                            py2 = self.l[j].px + 25
                            if(self.l[i].px == px2):
                                T2.Begin = False
                                self.b.Clear()
                                canvas.delete(self.l[i])

                            if(self.l[i].py == py2):
                                
                                self.b.Clear()
                                canvas.delete(self.l[i])"""


                    
                time.sleep(self.tempsSommeil)


                
        

class Thread2 (Thread):
    def __init__(self, T, tempsSommeil, nom):
        Thread.__init__(self)
        self.T = T
        self.tempsSommeil = tempsSommeil
        self.name = nom
        self.daemon = True

        self.Begin  = False

    def begin(self):
        if(self.Begin == False):
            self.Begin = True
            bouton_start["text"] = "stop"
        else:
            self.Begin = False
            bouton_start["text"] = "start"  


    
    def run(self):
        while True:

            if(self.Begin):
                self.T.chrono()
            time.sleep(self.tempsSommeil)
            

##########################################################################################################################################################################################
###############  Programme Principal ####################################################################################################################################################
##########################################################################################################################################################################################


fenetre = Tk()

W = 500
H = 400
label = "Start"

T = timer()

score = Label(fenetre,text=" Score : 0")
score.pack(side ="right")

canvas = Canvas(fenetre,width = W, height = H , bd=0, bg="white")
canvas.pack(padx=10,pady=10)



liste = []


def Create():
    print("Create")
    b =balles(50,4,4)
    liste.append(b)

    for i in range(len(liste)):
        if(len(liste) > 0):
            T1 = Thread1(liste[i],16.67/1000,"T1",liste)
            T1.start()
            


def clear():
    print("clear")

    B = liste[len(liste)-1]
    B.Clear()
    
    del(liste[len(liste)-1])
    
    
    
    

T2 = Thread2(T,1,"T2")
T2.start()





bouton_start = Button(fenetre, text= label, command = T2.begin)
bouton_start.pack(side="left")

bouton_quitter = Button(fenetre, text="Exit", command = quit)
bouton_quitter.pack(side="left")


bouton_moins = Button(fenetre, text ="-", command = clear)
bouton_moins.pack(side ="right")


  
bouton_plus = Button(fenetre, text="+", command = Create)
bouton_plus.pack(side="right")

        







fenetre.mainloop()
