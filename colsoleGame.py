#!/usr/bin/env python
# coding: utf-8

# In[25]:


import itertools
import random
from os import system as cmd   # will be used to clear the screen
from threading import Thread
import queue
from pynput import keyboard  # used to listen the keyboard in parallel
import time
from IPython.display import clear_output #  clear jupyter notebook output


# In[41]:


displayboard=[] # Main drawing board on which all the snake,food,boundries are there
height=25
width=50
width-=(width-2)%3 #  did in this in hope than in future we would increase horizontal 1move to 3chars


cornerchar='+'
verticalchar='|'
horizontalchar='='
snakeskin='#'
foodskin='$'


# In[42]:


# clears the console and jupyter screen
def clear():
    clear_output()
    cmd('cls')


# In[43]:


# set up boundries on the board
for i in range(height):
    displayboard.append([])
    for j in range(width):
        displayboard[i].append(' ')
        if( (i==0 and (j==0 or j==width-1)) or (i==height-1 and (j==0 or j==width-1)) ):
            displayboard[i][j]=cornerchar
        elif(j==0 or j==width-1):
            displayboard[i][j]=verticalchar
        elif(i==0 or i==height-1):
            displayboard[i][j]=horizontalchar


# In[44]:


# it is used to print the main board
def printmatrix(mat):
    brr=[]
    for arr in mat:
        for c in arr:
            brr.append(c)
        brr.append('\n')
    return ''.join(brr)


# In[45]:


print(printmatrix(displayboard))


# In[47]:


# all position where snake body is
snake=[(height//2,width//2),
       (height//2,width//2+1),
       (height//2,width//2+2),
       (height//2,width//2+3)
      ]


# In[48]:


#put the snake on the board middle
for y,x in snake:
    displayboard[y][x]=snakeskin


# In[49]:


# will give locaiton of next food item (a random blank square)
def foodlocation(board):
    firsttime=True
    while(firsttime or board[y][x]!=' '):
        x=random.randint(0,width-1)
        y=random.randint(0,height-1)
        if(firsttime):
            firsttime=False
    return y,x


# In[50]:


#listening the keyboard

keyboardbutton=[-1] # -1 signifies no input:in neutral state
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
    elif key == keyboard.Key.space:# -2 indicate exit
        keyboardbutton=[-2]
        return False
listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread


# In[51]:


directionsX=[1,0,-1,0] # clockwise
directionsY=[0,-1,0,1]
snakeDirection=0 #1,2,3

#first food location set up
fy,fx=foodlocation(displayboard)
displayboard[fy][fx]=foodskin

# game loop
while(True):
    clear()
    
    #head location of snake
    y,x=snake[-1]
    
    
    ##for keyboardbutton[0]
    # -1 -> blank
    # -2 -> exit
    # 0,1,2,3 -> directions
    #
    #
    # updating snake's direction
    newdirection=keyboardbutton[0]
    if(abs((snakeDirection-newdirection)%4)==2):
        newdirection=snakeDirection
    if(newdirection==-1):
        newdirection=snakeDirection
    elif(newdirection==-2):
        break
    else:
        snakeDirection=newdirection
    keyboardbutton[0]=-1
    
    
    ## updating the displayboard with new position of the snake and/or the fruit
    newy,newx=(y+directionsY[snakeDirection], x+directionsX[snakeDirection])
    if(displayboard[newy][newx]==foodskin): # if snake eats food
        snake.append((newy,newx))
        displayboard[newy][newx]=snakeskin
        fy,fx=foodlocation(displayboard)
        displayboard[fy][fx]=foodskin
        
    elif(displayboard[newy][newx]==' '): # if there is free area
        snake.append((newy,newx))
        displayboard[newy][newx]=snakeskin
        displayboard[snake[0][0]][snake[0][1]]=' '
        snake.pop(0)
        
    elif(displayboard[newy][newx]==snakeskin and c):# if it touches itself
        break
        
    elif(displayboard[newy][newx]==horizontalchar or displayboard[newy][newx]==verticalchar):# if it touches the boundry
        break
        
    
    print(printmatrix(displayboard))
    time.sleep(0.025)
        
cmd('cls')
print('gameover')
input()


# In[ ]:





# In[50]:





# In[ ]:




