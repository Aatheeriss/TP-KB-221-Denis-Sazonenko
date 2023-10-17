import tkinter as tk
from tkinter import ttk
import requests

#request for response from NBU API
res = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

def convert_currency():
    currency = currency_var.get()
    amount = float(entry_amount.get())
    for elem in res.json():
        if elem["cc"] == currency:
            rate = elem["rate"]
            break
            
    exchange_rates = {"EUR": rate, "USD": rate, "PLN": rate}  
    
    if currency in exchange_rates:
        result = amount * exchange_rates[currency]
        result_label.config(text=f"Result: {result:.2f} {"UAH"}")
    else:
        result_label.config(text="Choose currency")

root = tk.Tk()
root.title("Converter")

#styles 
style = ttk.Style()
style.configure("TButton", padding=(10, 5, 10, 5))
style.configure("TLabel", padding=(5, 5, 5, 5))

#var for currency type choice
currency_var = tk.StringVar()
currency_var.set("EUR")     #default value 

#frame
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

currency_label = ttk.Label(frame, text="Choose currency:")
currency_label.grid(row=0, column=0, padx=5, pady=5)

#creates option menu to choose currency, returns chosen currency to "currency_var"
currency_option_menu = ttk.Combobox(frame, textvariable=currency_var, values=["EUR", "USD", "PLN"])
currency_option_menu.grid(row=0, column=1, padx=5, pady=5)

amount_label = ttk.Label(frame, text="Enter value:")
amount_label.grid(row=1, column=0, padx=5, pady=5)

#creates field to enter amount of value to calculate
entry_amount = ttk.Entry(frame)
entry_amount.grid(row=1, column=1, padx=5, pady=5)

#creates button to proceed the action
convert_button = ttk.Button(frame, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
