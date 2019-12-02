from PIL import ImageTk,Image,ImageDraw
import PIL
from tkinter import *
width = 500
height=500
center=height//2
white=(255,255,255)
green=(0,128,0)

def save():
    filename="image.png"
    image1.save(filename)

def paint(event):
    x1,y1=(event.x-1), (event.y-1)
    x2,y2=(event.x+1), (event.y+1)
    cv.create_oval(x1,y1,x2,y2,fill="black",width=50)
    draw.line([x1,y1,x2,y2],fill="black",width=50)


root=Tk()
cv=Canvas(root,width=500,height=500,bg="white")
cv.pack()
image1=PIL.Image.new("RGB",(700,700),white)
draw=ImageDraw.Draw(image1)
cv.pack(expand=YES,fill=BOTH)
cv.bind("<B1-Motion>",paint)

button=Button(text="save",command=save)
button.pack()
root.mainloop()
    
