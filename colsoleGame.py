#!/usr/bin/env python
# coding: utf-8

# In[38]:


import itertools
import random
from os import system as cmd
from threading import Thread
import queue
from pynput import keyboard
import time
from IPython.display import clear_output


# In[39]:


displayboard=[]
backendboard=[]
height=25
width=100
width-=(width-2)%3

cornerchar='+'
verticalchar='|'
horizontalchar='='
snakeskin='#'
foodskin='$'


# In[48]:


def clear():
    clear_output()
    cmd('cls')


# In[40]:


for i in range(height):
    displayboard.append([])
    backendboard.append([])
    for j in range(width):
        displayboard[i].append(' ')
        backendboard[i].append(' ')
        if( (i==0 and (j==0 or j==width-1)) or (i==height-1 and (j==0 or j==width-1)) ):
            displayboard[i][j]=cornerchar
            backendboard[i][j]='#'
        elif(j==0 or j==width-1):
            displayboard[i][j]=verticalchar
            backendboard[i][j]='#'
        elif(i==0 or i==height-1):
            displayboard[i][j]=horizontalchar
            backendboard[i][j]='#'


# In[41]:


def printmatrix(mat):
    for arr in mat:
        for c in arr:
            print(c,sep='',end='')
        print()


# In[42]:


printmatrix(displayboard)


# In[43]:


snake=[(height//2,width//2),
       (height//2,width//2+1),
       (height//2,width//2+2),
       (height//2,width//2+3)
      ]


# In[44]:


for y,x in snake:
    displayboard[y][x]=snakeskin


# In[45]:


def foodlocation(board):
    firsttime=True
    while(firsttime or board[y][x]!=' '):
        x=random.randint(0,width-1)
        y=random.randint(0,height-1)
        if(firsttime):
            firsttime=False
    return y,x


# In[46]:


keyboardbutton=[-1]
def on_press(key):
    global keyboardbutton
    if key == keyboard.Key.right:
        keyboardbutton=[0]
    elif key == keyboard.Key.up:
        keyboardbutton=[1]
    elif key == keyboard.Key.left:
        keyboardbutton=[2]
    elif key == keyboard.Key.down:
        keyboardbutton=[3]
    elif key == keyboard.Key.space:
        keyboardbutton=[-2]
        return False
listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread


# In[47]:


directionsX=[1,0,-1,0] # clockwise
directionsY=[0,-1,0,1]
snakeDirection=0 #1,2,3
fy,fx=foodlocation(displayboard)
displayboard[fy][fx]=foodskin
while(True):
    clear()
    # game loop
    y,x=snake[-1]
    ##
    # -1 -> blank
    # -2 -> exit
    newdirection=keyboardbutton[0]
    if(newdirection==-1):
        newdirection=snakeDirection
    else:
        snakeDirection=newdirection
    keyboardbutton[0]=-1
    
    
    ##
    newy,newx=(y+directionsY[snakeDirection], x+directionsX[snakeDirection])
    if(displayboard[newy][newx]==foodskin):
        snake.append((newy,newx))
        displayboard[newy][newx]=snakeskin
        fy,fx=foodlocation(displayboard)
        displayboard[fy][fx]=foodskin
        
    elif(displayboard[newy][newx]==' '):
        snake.append((newy,newx))
        displayboard[newy][newx]=snakeskin
        displayboard[snake[0][0]][snake[0][1]]=' '
        snake.pop(0)
    elif(displayboard[newy][newx]==snakeskin):### to be filled more, direction k ulta ni hona chahie
        break
    elif(displayboard[newy][newx]==horizontalchar or displayboard[newy][newx]==verticalchar):
        break
        
    
    
    printmatrix(displayboard)
    time.sleep(0.1)
        
cmd('cls')
print('gameover')


# In[ ]:





# In[ ]:




