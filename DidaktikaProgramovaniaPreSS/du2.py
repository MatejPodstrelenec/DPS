import tkinter, random, time
canvas = tkinter.Canvas(width=600, height=600, bg='white')
canvas.pack()

### Variables ###
square_size = 40
mouse_click = False
xs = 1
ys = 1


### Functions ###

#Draw a rectangle
def draw_rect(x,y,x2,y2):
	random_color = hexadecimal = ["#2196f3"];
	id = canvas.create_rectangle(x,y,x2,y2, fill=random_color, outline='black', width=1)
	return id

#Mouse click handler
def mouse_click_action(event):
    global mouse_click

    square_x = canvas.coords(square)[0]
    square_y = canvas.coords(square)[1]

    if (event.x >= square_x and event.x <= (square_x + square_size) and event.y >= square_y and event.y <= (square_y + square_size)):
        mouse_click = True    

#Is rectangle near border
def near_border():
    global xs, ys

    square_x = canvas.coords(square)[0] + xs
    square_y = canvas.coords(square)[1] + ys
    
    if (square_x <1 or square_x > (600 - square_size) or square_y < 1 or square_y > (600 - square_size)):
        return True
    else:
        return False

#Change direction of square when near a canvas
def change_direction():
    global xs, ys

    xs = random.choice([-1,1]) 
    ys = random.choice([-1,1]) 


### Main ###
canvas.bind('<Button-1>', mouse_click_action)

square_x = random.randint(100,500)
square_y = random.randint(100,500)

square = draw_rect(square_x,square_y,square_x + square_size,square_y + square_size)
canvas.update()
start = time.time()

#Move rectangle until user does mouse click on it
while (mouse_click == False):   
    if (near_border() == True): 
        change_direction()
    
    else:
        canvas.move(square,xs,ys)
        canvas.update()
    
end = time.time()
final_text = "No konečne! Trvalo Ti to " + str(round(end-start,2)) + " sekúnd." 
canvas.create_text(300, 50,fill="black",font="Times 16 bold", text=final_text, tags=("text"))

canvas.mainloop()