import tkinter as tk
from tkinter import CENTER, END, ttk
from function import DatabaseConnector as DB
import random

# Function
# ====== This are the function section of the Hotel Management System

# This Method create a table if not exits
DB.create_table()

# This Function check in a guest
def check_in():

    random_room_number = random.randint(1, 99) # getting a random number
    name = name_entry.get().title() # getting guest name
    email = email_entry.get() # getting guest email
    number = number_entry.get() # getting guest number
    address = address_entry.get().lower() # getting guest address
    room_no = len(name) + random_room_number # getting random room number

    # Calling Method from DatabaseConnector Class to submit guest details
    DB.submit(name, email, number, address, room_no)

    # Automatically Calling display Function to display list of available guest after a new guest has been checked in
    display_all_guest()

    # Emptying guest entries 
    name_entry.delete(first=0, last=END)
    email_entry.delete(first=0, last=END)
    number_entry.delete(first=0, last=END)
    address_entry.delete(first=0, last=END)

# This Function display a guest record
def display_guest():
    room_no = room_no_entry.get() # getting room number of guest

    # Calling Method from DatabaseConnector Class and store the record in a variable
    records = DB.display_guest((room_no,)) # This is been return as a list

    if records != []: # if list is not empty
        for record in records: # iterate through the list of records to access the individual item         

            # After iterating through the list of displays them in a Frame
            name = tk.Label(display_guest_frame, text="Name: ", bg="white")
            name.grid(row=0, column=0, sticky='w', padx=2)

            name_select = tk.Label(display_guest_frame, text=record[1], bg="white")
            name_select.grid(row=0, column=1, sticky='e', padx=10)

            email = tk.Label(display_guest_frame, text="Email: ", bg="white")
            email.grid(row=1, column=0, sticky='w', padx=2)

            email_select = tk.Label(display_guest_frame, text=record[2], bg="white")
            email_select.grid(row=1, column=1, sticky='e', padx=10)

            address = tk.Label(display_guest_frame, text="Address: ", bg="white")
            address.grid(row=2, column=0, sticky='w', padx=2)

            address_select = tk.Label(display_guest_frame, text=record[4], bg="white")
            address_select.grid(row=2, column=1, sticky='e', padx=10)

            number = tk.Label(display_guest_frame, text="Email: ", bg="white")
            number.grid(row=3, column=0, sticky='w', padx=2)

            number_select = tk.Label(display_guest_frame, text=record[3], bg="white")
            number_select.grid(row=3, column=1, sticky='e', padx=10)

            # Commit the query in order to run the code
            DB.commit_connection()

        # Emptying room number entry 
        room_no_entry.delete(first=0, last=END)
    else: # if list is empty
        # Display a message to the user
        name = tk.Label(display_guest_frame, text="No Record Found", fg="red", bg="white")
        name.grid(row=0, column=0, sticky='w', padx=2, columnspan=2)

# This Function display all available guest Note (it displays their names and room numbers)
def display_all_guest():
    row = 1 # This is been use to increase the row base on the number of records returned

    # Calling Method from DatabaseConnector Class and store the record in a variable
    results = DB.display_all_guest() # This is been return as a list of tuples
    if results != []: # if list of tuples is not empty
        for result in results: # iterate through the list of tuples to access the individual tuple

            # After iterating through the list of tuples displays them in a Frame
            name = tk.Label(room_details, text=result[0], bg="white")
            name.grid(row=row, column=0, sticky='w', padx=2, pady=2)

            room_no = tk.Label(room_details, text=result[1], bg="white")
            room_no.grid(row=row, column=1, sticky='e', padx=10, pady=2)

            row += 1 # increase the number of row by 1
    else: # if list is empty
        # Display a message to the user
        error = tk.Label(room_details, text="No Record Found", fg="red", bg="white")
        error.grid(row=1, column=0, sticky='w', padx=2, columnspan=2)

    # Commit the query in order to run the code
    DB.commit_connection()

# This Function checks out guest base on room number
def check_out():
    room_no = room_no_entry_check_out.get() # getting room number of guest
    # Calling Method from DatabaseConnector Class to check out guest
    DB.check_out(room_no) # This delete the guest record from the users table

    # Emptying room number entry 
    room_no_entry_check_out.delete(first=0, last=END)

# ====== End of function


# Creating Window
window = tk.Tk()
window.title("Hotel Management System") # Adding title
window.geometry("1200x600") # Creating a default width and height 
window.config(bg="skyblue") # Creating default background color

# Creating first Label as Title
label_title = tk.Label(window, text="Hotel Management System", font=("Courier", 50, "bold"), bg="skyblue")
label_title.grid(row=0, column=0, columnspan=4, padx=40, pady=20)

# Creating Frames
frame_1 = tk.Frame(window, borderwidth="2", bg="white")
frame_1.grid(row=1, column=0, sticky="w", padx=5)

frame_2 = tk.Frame(window, borderwidth="2", bg="white")
frame_2.grid(row=1, column=1, sticky="w", padx=5)

frame_3 = tk.Frame(window, borderwidth="2", bg="white")
frame_3.grid(row=1, column=2, sticky="w", padx=5)

frame_4 = tk.Frame(window, borderwidth="2", bg="white")
frame_4.grid(row=1, column=3, sticky="w", padx=5)

# Frame 1 Details
# Frame 1 Labels
checking_in_details = tk.Label(frame_1, text="Checking In Details", font=(20), bg="white")
checking_in_details.grid(row=0, column=0, columnspan=2, padx=80, pady=10)

name = tk.Label(frame_1, text="Customer Name :", bg="white")
name.grid(row=1, column=0, sticky='w', pady=10, ipadx=10,ipady=10)

email = tk.Label(frame_1, text="Email Address :", bg="white")
email.grid(row=2, column=0, sticky='w', pady=10, ipadx=10,ipady=10)

number = tk.Label(frame_1, text="Mobile Number :", bg="white")
number.grid(row=3, column=0, sticky='w', pady=10, ipadx=10,ipady=10)

address= tk.Label(frame_1, text="Customer Address :", bg="white")
address.grid(row=4, column=0, sticky='w', pady=10, ipadx=10,ipady=10)

# Frame 1 Entries
name_entry = tk.Entry(frame_1)
name_entry.grid(row=1, column=1, sticky='w', pady=10, ipadx=10, ipady=10)

email_entry = tk.Entry(frame_1)
email_entry.grid(row=2, column=1, sticky='w', pady=10, ipadx=10, ipady=10)

number_entry = tk.Entry(frame_1)
number_entry.grid(row=3, column=1, sticky='w', pady=10, ipadx=10, ipady=10)

address_entry= tk.Entry(frame_1)
address_entry.grid(row=4, column=1, sticky='w', pady=10, ipadx=10, ipady=10)

# Frame 1 Button
frame_1_button = tk.Button(frame_1, text="Submit Details", command=check_in)
frame_1_button.grid(row=5, column=0, columnspan=2, pady=10, ipadx=10,ipady=10)

# Frame 2 Details
# Frame 2 Label
checking_out_details = tk.Label(frame_2, text="Checking Out Details", font=(20), bg="white")
checking_out_details.grid(row=0, column=0, columnspan=2, padx=80, pady=10)

room_no = tk.Label(frame_2, text="Enter Room No : ", bg="white")
room_no.grid(row=1, column=0, sticky='w', pady=10, ipadx=10,ipady=10)

# Frame 2 Entry
room_no_entry_check_out = tk.Entry(frame_2,)
room_no_entry_check_out.grid(row=1, column=1, sticky='w', pady=10, ipadx=10, ipady=10)

# # Frame 2 Button
frame_2_button = tk.Button(frame_2, text="Checking Out", command=check_out)
frame_2_button.grid(row=2, column=0, columnspan=2, pady=10, ipadx=10, ipady=10)

# Frame 3 Details
# Frame 3 Label

show_guest_list = tk.Label(frame_3, text="Show Guest List", font=(20), bg="white")
show_guest_list.grid(row=0, column=0, columnspan=2, padx=80, pady=10)

# Creating a Frame to Display Room Details
room_details = tk.Frame(frame_3, bg="white", borderwidth="2",)
room_details.grid(row=1, column=0, columnspan=2)

names = tk.Label(room_details, text="Names", font=(20), bg="white")
names.grid(row=0, column=0, padx=50, pady=10)

rooms = tk.Label(room_details, text="Room No", font=(20), bg="white")
rooms.grid(row=0, column=1, padx=50, pady=10)

# Frame 3 Button
frame_3_button = tk.Button(frame_3, text="Refresh", command=display_all_guest())
frame_3_button.grid(row=2, column=0, columnspan=2, pady=10, ipadx=10,ipady=10)

# Frame 4 Details
# Frame 4 Label
checking_out_details = tk.Label(frame_4, text="Get Info of any Guest", font=(20), bg="white")
checking_out_details.grid(row=0, column=0, columnspan=2, padx=80, pady=10)

room_no = tk.Label(frame_4, text="Enter Room No : ", bg="white")
room_no.grid(row=1, column=0, sticky='w', pady=10, ipadx=10, ipady=10)

# Frame 4 Entry
room_no_entry = tk.Entry(frame_4)
room_no_entry.grid(row=1, column=1, sticky='w', pady=10, ipadx=10,ipady=10)

display_guest_frame = tk.Frame(frame_4, bg="white")
display_guest_frame.grid(row=3, column=0, padx=1)

# Frame 4 Button
frame_4_button = tk.Button(frame_4, text="Check Details", command=display_guest)
frame_4_button.grid(row=2, column=0, columnspan=2, pady=10, ipadx=10,ipady=10)

# Keeping the window running till father notice :)
window.mainloop()

