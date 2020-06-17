import requests
from tkinter import *

HEIGHT = 500
WIDTH = 600

def formatting(love):
	percentage = love['percentage']
	result = love['result']
	
	output = 'Love percentage \n %s \n %s' % (percentage, result)
	return output
def get_love():
	url = "https://love-calculator.p.rapidapi.com/getPercentage"

	querystring = {"fname":entry_a.get(),"sname":entry_b.get()}

	headers = {
		'x-rapidapi-host': "love-calculator.p.rapidapi.com",
		'x-rapidapi-key': "05f972929bmshb7a19c5df621e95p14b3d1jsnb983f39d4b82"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	love = response.json()
	label['text'] = formatting(love)
root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file='love.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#ff66ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_a = Entry(frame, font=40)
entry_a.place(relwidth=0.3, relheight=1)

entry_b = Entry(frame, font=40)
entry_b.place(relx = 0.7, relwidth=0.3, relheight=1)


button = Button(frame, text="Love meter", font=40, command=get_love)
button.place(relx=0.35, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#ff66ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame,font=("arial", 40))
label.place(relwidth=1, relheight=1)

root.mainloop()
root.mainloop()