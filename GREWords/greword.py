from tkinter import *
import questions as q
from random import randint
from PIL import ImageTk, Image


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

t = Entry(root)
t.insert(0,10)
t.pack();
b = Button(bottomFrame,text="Next",width=50,height=10,command=packAll)
b.pack()


timescount = 0;

questionLabel = Label(topFrame,width=20,height=2,font=("Courier",44));
# questionLabel.pack(fill=X);

selectedanswer = StringVar()

one = Radiobutton(topFrame,variable=selectedanswer,value='rubbish0')
# one.pack(anchor=W)
two = Radiobutton(topFrame,variable=selectedanswer,value='rubbish')
# two.pack(anchor=W)
three = Radiobutton(topFrame,variable=selectedanswer,value='rubbish2')
# three.pack(anchor=W)
four = Radiobutton(topFrame,variable=selectedanswer,value='rubbish3')
# four.pack(anchor=W)

panel = Label(bottomFrame)
# panel.pack(fill = "both", expand = "no")


questionTemp = q.getRandomQuestion();
def refreshOptions():
	one.config(value="rubbish")
	two.config(value="rubbish0")
	three.config(value="rubbish2")
	four.config(value="rubbish3")

def callback():
	a= randint(0,3);
	global questionTemp;
	questionTemp = q.getRandomQuestion();
	global selectedanswer;
	global img;
	path = './images/' + questionTemp[0] + '.jpg'
	img = ImageTk.PhotoImage(Image.open(path))
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


def displayScore():
	one.pack_forget()
	two.pack_forget()
	three.pack_forget()
	four.pack_forget()
	panel.pack_forget()
	label.pack_forget()
	questionLabel.config(text="Score is "+str(score) + "/" + str(times))


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
		
root.bind('<Return>',sel)


label = Label(bottomFrame);
label.pack(side=RIGHT);
selectButton = Button(bottomFrame,text="Submit",height=2,width=10,command=sel);
# selectButton.pack();


callback();


root.mainloop()
