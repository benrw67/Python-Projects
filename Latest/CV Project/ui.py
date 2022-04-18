from tkinter import *
THEME_COLOR = "white"
FONT_NAME = "Arial"
NOHOURS = [
    '24',
    '48',
    '72',
    '120',
    '168'

]

class CvInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("CommVault")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.title_label = Label(text="CommVault", font=(FONT_NAME, 14), pady=20, padx=20, bg=THEME_COLOR, fg="black")
        self.title_label.grid(column=0, row=0, columnspan=2)
        #Commserve Hostname
        self.cs_label = Label(text="Commserve FQDN: ", font=(FONT_NAME, 12), fg="black", bg=THEME_COLOR)
        self.cs_label.grid(column=0, row=1)
        self.cs_input = Entry(width=20)
        self.cs_input.grid(column=1, row=1)

        #Number of hours
        self.no_hours_label = Label(text="Number of hours: ", font=(FONT_NAME, 12),bg=THEME_COLOR, fg="black", pady=10, padx=10)
        self.no_hours_label.grid(column=0, row=2)
        self.variable = IntVar(self.window)
        self.variable.set(NOHOURS[0])
        self.no_hours = OptionMenu(self.window, self.variable, *NOHOURS)
        self.no_hours.grid(column=1, row=2)

        #Download Location
        self.download_loca_label = Label(text=" Download Location: ", font=(FONT_NAME, 12), bg=THEME_COLOR, fg="black")
        self.download_loca_label.grid(column=0, row=3)
        self.download_loca = Entry(width=20)
        self.download_loca.grid(column=1, row=3)

        #Get Report button
        self.get_report = Button(text="Get Report", pady=20, padx=20)
        self.get_report.grid(column=1, row=7, columnspan=2, command=getcvreport)

        #Domain
        self.domain_label = Label(text=" Domain: ", font=(FONT_NAME, 12), bg=THEME_COLOR, fg="black")
        self.domain_label.grid(column=0, row=4)
        self.domain = Entry(width=20)
        self.domain.grid(column=1, row=4)

        #Username
        self.username_label = Label(text=" Username: ", font=(FONT_NAME, 12), bg=THEME_COLOR, fg="black")
        self.username_label.grid(column=0, row=5)
        self.username = Entry(width=20)
        self.username.grid(column=1, row=5)

        #Password
        self.password_label = Label(text=" Password: ", font=(FONT_NAME, 12), bg=THEME_COLOR, fg="black")
        self.password_label.grid(column=0, row=6)
        self.password = Entry(width=20)
        self.password.grid(column=1, row=6)

        self.window.mainloop()

    def getcvreport(self):
        print(self.username)
        print(self.password)
        print(self.domain)
        print(self.download_loca)

        
