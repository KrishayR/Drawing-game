import tkinter as tk 

root = tk.Tk()

WIDTH = 400
HEIGHT = 400

canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()

x1 = WIDTH / 2
y1 = HEIGHT / 2

text = canvas.create_text(x1,y1*2-20,text="Keys to move = a,d,w,s")

player = canvas.create_rectangle

player((x1,y1,x1+10,y1+10))

def draw_rect():
  player((x1,y1,x1+10,y1+10), fill="green")

def del_rect():
  player((x1,y1,x1+10,y1+10), fill="white")

def move(event):
  global x1,y1
  print(event.char)
  if event.char == "a":
    del_rect()
    x1 -= 10
  elif event.char == "d":
    del_rect()
    x1 += 10
  elif event.char == "w":
    del_rect()
    y1 -= 10
  elif event.char == "s":
    del_rect()
    y1 += 10
  draw_rect()

root.bind("<Key>",move)

def moveIn(direction):
  global x1,y1
  if direction == "a":
    del_rect()
    x1 -= 10
  elif direction == "s":
    del_rect()
    y1 += 10
  draw_rect()

a_button = tk.Button(
                    root,
                    text="a",
                    command=lambda:moveIn("a"),
                    bg="black",
                    fg="white"
)
a_button.pack(side=tk.LEFT)

s_button = tk.Button(
                    root,
                    text="s",
                    command=lambda:moveIn("s"),
                    bg="black",
                    fg="white"
)
s_button.pack(side=tk.LEFT)

root.mainloop()
