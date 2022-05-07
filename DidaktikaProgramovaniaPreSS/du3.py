import tkinter, random
canvas = tkinter.Canvas(width=600, height=400, bg='white')
canvas.pack()

### Variables ###
circles = []

### Functions ###

#Draw a circle
def draw_circle(x,y,x2,y2):
	id = canvas.create_oval(x,y,x2,y2, fill='#2196f3', outline='black', width=1)
	return id

#Restart game
def restart():
    global circles

    canvas.delete('text')

    for i,v in enumerate(circles):
        canvas.itemconfig(v[0],fill='#2196f3') 
        canvas.coords(v[0],10,10 + (i*50),40,40 + (i*50))
        v[1] = 10

#When start button is clicked, circles start randomly moving forward
def start_race():
    global circles
    winner = False
    leader = 0
    max_distance = 0

    #Restart if race is already finished or in progress when start button pressed
    restart()

    while (winner == False):

        for i,v in enumerate(circles):
            step = random.randint(1,10)
            v[1] += step
            
            if (v[1] > max_distance):
                canvas.itemconfig(circles[leader][0],fill='#2196f3')   
                max_distance = v[1]
                leader = i
                canvas.itemconfig(circles[leader][0],fill='#ff0000')

            canvas.move(v[0],step,0)
            canvas.after(20)            
            canvas.update()


        if (max_distance > 550): 
            winner = True

    final_text = "Vyhral hráč č. " + str(leader+1) + "."
    canvas.create_text(310, 280, fill="red",font="Times 16 bold", text=final_text, tags=("text"))

### Main ###
for n in range(5): 
    circles.append([]) # Vytvorime pole v pre konkrétny balík a jeho info
    circles[n].append(draw_circle(10,10 + (n*50),40,40 + (n*50))) #id of circle
    circles[n].append(10) #circle x position
    canvas.update()

#Start race button
button1=tkinter.Button(canvas, text="Start",padx=20,highlightbackground='#FFF', command=start_race)
button1.place(x=260, y=326)
    
canvas.mainloop()