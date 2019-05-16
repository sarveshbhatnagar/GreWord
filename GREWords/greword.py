from tkinter import *
import questions as q
from random import randint
from PIL import ImageTk, Image

#initializes the window and segments them in frame.
root = Tk()
root.title("GRE Frequent Word list, Made By - Sarvesh Bhatnagar")
root.geometry('720x520+0+0')
root.configure(background='black')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side =BOTTOM)
score = 0;
times = 10;

#packs required elements for the quiz , such as radiobuttons and submit button.
#forgets initial Entry and next button.
def packAll():
	global times;
	times = int(t.get())
	b.pack_forget()
	t.pack_forget()
	questionLabel.pack(fill=X)
	one.pack(anchor=W)
	two.pack(anchor=W)
	three.pack(anchor=W)
	four.pack(anchor=W)
	panel.pack(fill = "both", expand = "no")
	selectButton.pack()


#initialize various elements , can be packed and unpacked when needed.
#Entry t for initial screen with default value 10
t = Entry(root)
t.insert(0,10)
t.pack();
#button b which starts the program.
b = Button(bottomFrame,text="Next",width=50,height=10,command=packAll)
b.pack()

#maintains count of how many questions answered.
timescount = 0;

#question label
questionLabel = Label(topFrame,width=20,height=2,font=("Courier",44));

#variable to store selected Answer
selectedanswer = StringVar()


#Radio buttons...
one = Radiobutton(topFrame,variable=selectedanswer,value='rubbish0')
two = Radiobutton(topFrame,variable=selectedanswer,value='rubbish')
three = Radiobutton(topFrame,variable=selectedanswer,value='rubbish2')
four = Radiobutton(topFrame,variable=selectedanswer,value='rubbish3')

#panel where in image goes.
panel = Label(bottomFrame)

#A function called when reset button is pressed.
def reset():
	print("Reset")

#Reset button at the end of the program.
resetButton = Button(bottomFrame,text="Reset",height=2,width=10,command=reset)

# temp var to hold questions.
questionTemp = q.getRandomQuestion();

#Refreshes the radio button values which is set by answer.
def refreshOptions():
	one.config(value="rubbish")
	two.config(value="rubbish0")
	three.config(value="rubbish2")
	four.config(value="rubbish3")


#Main program, responsible for setting questions, Radio button and image.
def callback():
	a= randint(0,3);
	global questionTemp;
	questionTemp = q.getRandomQuestion();
	global selectedanswer;
	global img;
	try:
		path = './images/' + questionTemp[0] + '.jpg'
		img = ImageTk.PhotoImage(Image.open(path))
	except:
		path = './images/' + questionTemp[0] + '.png'
		img = ImageTk.PhotoImage(Image.open(path))
	finally:
		questionAnswers = q.getRandomAnswers(questionTemp[1]);
		questionLabel.config(text=questionTemp[0]);
		if a == 0:
			one.config(text=questionTemp[1],value=questionTemp[1])
			two.config(text=questionAnswers[0])
			three.config(text=questionAnswers[1])
			four.config(text=questionAnswers[2])
		elif a == 1:
			one.config(text=questionAnswers[0])
			two.config(text=questionTemp[1],value=questionTemp[1])
			three.config(text=questionAnswers[1])
			four.config(text=questionAnswers[2])
		elif a == 2:
			one.config(text=questionAnswers[0])
			two.config(text=questionAnswers[1])
			three.config(text=questionTemp[1],value=questionTemp[1])
			four.config(text=questionAnswers[2])
		else:
			one.config(text=questionAnswers[0])
			two.config(text=questionAnswers[1])
			three.config(text=questionAnswers[2])
			four.config(text=questionTemp[1],value=questionTemp[1])

		panel.config(image = img)


# called when timescount >= times to display the score.
def displayScore():
	one.pack_forget()
	two.pack_forget()
	three.pack_forget()
	four.pack_forget()
	panel.pack_forget()
	label.pack_forget()
	questionLabel.config(text="Score is "+str(score) + "/" + str(times))
	selectButton.pack_forget()
	resetButton.pack();



#For submit button, if the answer is wrong displays the right answer ...
#can be drastically improved.
def sel(event=None):
	global selectedanswer;
	global times;
	global timescount;
	if timescount<times:
		timescount += 1;
		if(questionTemp[1]==str(selectedanswer.get())):
		   	global score;
		   	score += 1;
		   	label.config(text = "Right answer")
		else:
		   	label.config(text=questionTemp[1] + "is the correct answer")
		refreshOptions()
		callback()
	else:
		displayScore()


#binding the enter key with sel function.
root.bind('<Return>',sel)


label = Label(bottomFrame);
label.pack(side=RIGHT);
selectButton = Button(bottomFrame,text="Submit",height=2,width=10,command=sel);
# selectButton.pack();

#can be placed at a better position. 
callback();


root.mainloop()
