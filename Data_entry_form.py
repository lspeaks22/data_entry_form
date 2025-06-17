import tkinter
from tkinter import ttk
from tkinter import messagebox

import csv
import os


def enter_data():
    # User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    gender = gender_combobox.get()
    
    # Address info
    address = address_entry.get()
    county = county_entry.get()
    state = state_combobox.get()
    zipcode = zip_code_entry.get()

    if firstname and lastname:
        data = [firstname, lastname, title, age, gender, nationality, address, county, state, zipcode]

        file_exists = os.path.isfile('form_data.csv') #path of where to save csv file
        
        with open('form_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write header if file doesn't exist
                writer.writerow(["First Name", "Last Name", "Title", "Age", "Gender", "Nationality",
                                 "Address", "County", "State", "Zip Code"])
            writer.writerow(data)

        messagebox.showinfo("Success", "Data saved successfully.")
        print("Data saved to form_data.csv")
        print("-" * 50)
    else:
        messagebox.showwarning(title="Error", message="First name and last name are required.")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Miss", "Dr."])
title_combobox.current(0)
title_combobox.grid(row=1, column=2)
title_label.grid(row=0, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=120)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, values=["Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Antiguan",
    "Argentine", "Armenian", "Australian", "Austrian", "Azerbaijani", "Bahamian", "Bahraini",
    "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese", "Bhutanese",
    "Bolivian", "Bosnian", "Botswanan", "Brazilian", "British", "Bruneian", "Bulgarian",
    "Burkinabé", "Burmese", "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean",
    "Central African", "Chadian", "Chilean", "Chinese", "Colombian", "Comoran", "Congolese",
    "Costa Rican", "Croatian", "Cuban", "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican",
    "Dutch", "East Timorese", "Ecuadorian", "Egyptian", "Emirati", "Equatorial Guinean",
    "Eritrean", "Estonian", "Ethiopian", "Fijian", "Finnish", "French", "Gabonese", "Gambian",
    "Georgian", "German", "Ghanaian", "Greek", "Grenadian", "Guatemalan", "Guinean",
    "Guinean-Bissauan", "Guyanese", "Haitian", "Honduran", "Hungarian", "Icelander", "Indian",
    "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican",
    "Japanese", "Jordanian", "Kazakhstani", "Kenyan", "Kiribati", "Korean", "Kosovar", "Kuwaiti",
    "Kyrgyz", "Laotian", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtensteiner",
    "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malawian", "Malaysian",
    "Maldivian", "Malian", "Maltese", "Marshallese", "Mauritanian", "Mauritian", "Mexican",
    "Micronesian", "Moldovan", "Monegasque", "Mongolian", "Montenegrin", "Moroccan",
    "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerien",
    "Nigerian", "North Korean", "North Macedonian", "Norwegian", "Omani", "Pakistani", "Palauan",
    "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Philippine",
    "Polish", "Portuguese", "Qatari", "Romanian", "Russian", "Rwandan", "Saint Lucian",
    "Salvadoran", "Samoan", "San Marinese", "São Toméan", "Saudi", "Scottish", "Senegalese",
    "Serbian", "Seychellois", "Sierra Leonean", "Singaporean", "Slovak", "Slovenian",
    "Solomon Islander", "Somali", "South African", "South Korean", "South Sudanese", "Spanish",
    "Sri Lankan", "Sudanese", "Surinamese", "Swazi", "Swedish", "Swiss", "Syrian", "Taiwanese",
    "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian", "Tunisian", "Turkish",
    "Turkmen", "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbek", "Vanuatuan",
    "Venezuelan", "Vietnamese", "Welsh", "Yemeni", "Zambian", "Zimbabwean",""])
nationality_combobox.grid(row=3, column=1)

gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_label.grid(row=2, column=2)
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Prefer not to say"])
gender_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Address Info
address_frame = tkinter.LabelFrame(frame, text="Address Information")
address_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

address_label = tkinter.Label(address_frame, text="Address")
address_label.grid(row=0, column=0)
address_entry = tkinter.Entry(address_frame)
address_entry.grid(row=1, column=0)

county_label = tkinter.Label(address_frame, text="County")
county_label.grid(row=0, column=1)
county_entry = tkinter.Entry(address_frame)
county_entry.grid(row=1, column=1)

state_label = tkinter.Label(address_frame, text="State")
state_label.grid(row=2, column=0)
state_combobox = ttk.Combobox(address_frame, values=[
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
    "Wisconsin", "Wyoming"
])
state_combobox.grid(row=3, column=0)

zip_code_label = tkinter.Label(address_frame, text="Zip Code")
zip_code_label.grid(row=2, column=1)
zip_code_entry = tkinter.Entry(address_frame)
zip_code_entry.grid(row=3, column=1)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Submit Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
