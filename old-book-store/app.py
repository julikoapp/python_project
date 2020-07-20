from tkinter import *
from data_func import Database

data_func = Database("bookstore.db")  # sorry too lazy to replace with something new ;)


class App:
    def __init__(self, window):
        self.window = window

        self.window.wm_title("Bookstore")
        tit = Label(window, text='Title')
        tit.grid(row=0, column=0)

        aut = Label(window, text='Author')
        aut.grid(row=0, column=2)

        yea = Label(window, text='Year')
        yea.grid(row=1, column=0)

        isb = Label(window, text='ISBN')
        isb.grid(row=1, column=2)

        self.title_text = StringVar()
        self.title = Entry(window, textvariable=self.title_text)
        self.title.grid(row=0, column=1)

        self.author_name = StringVar()
        self.author = Entry(window, textvariable=self.author_name)
        self.author.grid(row=0, column=3)

        self.year_tx = StringVar()
        self.year = Entry(window, textvariable=self.year_tx)
        self.year.grid(row=1, column=1)

        self.isbn_tx = StringVar()
        self.isbn = Entry(window, textvariable=self.isbn_tx)
        self.isbn.grid(row=1, column=3)

        self.list_1 = Listbox(window, height=6, width=35)
        self.list_1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list_1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list_1.yview)

        self.list_1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)
        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)
        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)
        b4 = Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)
        b5 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)
        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            index = self.list_1.curselection()[0]
            self.selected_tuple = self.list_1.get(index)
            self.title.delete(0, END)
            self.title.insert(END, self.selected_tuple[1])
            self.author.delete(0, END)
            self.author.insert(END, self.selected_tuple[2])
            self.year.delete(0, END)
            self.year.insert(END, self.selected_tuple[3])
            self.isbn.delete(0, END)
            self.isbn.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list_1.delete(0, END)
        for row in data_func.view_all_books():
            self.list_1.insert(END, row)

    def search_command(self):
        self.list_1.delete(0, END)
        for row in data_func.find_book(self.title_text.get(), self.author_name.get(), self.year_tx.get(),
                                       self.isbn_tx.get()):
            self.list_1.insert(END, row)

    def add_command(self):
        self.list_1.delete(0, END)
        data_func.add_book(self.title_text.get(), self.author_name.get(), self.year_tx.get(), self.isbn_tx.get())
        self.title.delete(0, END)
        self.author.delete(0, END)
        self.year.delete(0, END)
        self.isbn.delete(0, END)
        self.view_command()

    def delete_command(self):
        data_func.delete_book(self.selected_tuple[0])

    def update_command(self):
        data_func.update(self.selected_tuple[0], self.title_text.get(), self.author_name.get(), self.year_tx.get(),
                         self.isbn_tx.get())



window = Tk()
app_start = App(window)
window.mainloop()
