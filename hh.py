from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog

def show():
    # Отримати обрані значення з радіокнопок
    selected_radio = selected_option.get()

    # Отримати обране значення з комбінованого поля
    selected_combobox = color.get()

    # Отримати обрані значення зі списку
    selected_list = list.curselection()
    list_values = [list.get(idx) for idx in selected_list]

    # Отримати обране значення зі спінбоксу
    selected_spinbox = spinbox_var.get()

    # Отримати обрані значення з прапорців
    selected_checkboxes = []
    for index, var in enumerate(selected_option.get()):
        if var == '1':
            selected_checkboxes.append(options[index])

    # Отримати обрані значення з кнопок
    selected_buttons = [button.cget("text") for button in buttons]

    # Записати результати у відповідному форматі
    results = f"Результати тестування:\n"
    results += f"Обране значення з радіокнопок: {selected_radio}\n"
    results += f"Обране значення з комбінованого поля: {selected_combobox}\n"
    results += f"Обране значення зі списку: {list_values}\n"
    results += f"Обране значення зі спінбоксу: {selected_spinbox}\n"
    results += f"Обрані значення з прапорців: {selected_checkboxes}\n"
    results += f"Обрані значення з кнопок: {selected_buttons}\n"

    # Оновити етикетку з результатами
    label_rez.config(text=results)

    # Зберегти результати у текстовий файл
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(results)

root = Tk()
root.geometry('315x360')
root.title('Тестування')

notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)
style = ttk.Style()

style.configure('My.TFrame', background='#a6a6a6')
style_label = ttk.Style()
style_label.configure("Color.TLabel", font=("Brush Script MT", 15), background="#000000", foreground="#ffffff")
frame1 = ttk.Frame(notebook, style='My.TFrame')
frame2 = ttk.Frame(notebook, style='My.TFrame')
frame3 = ttk.Frame(notebook, style='My.TFrame')
frame4 = ttk.Frame(notebook, style='My.TFrame')
frame5 = ttk.Frame(notebook, style='My.TFrame')
frame6 = ttk.Frame(notebook, style='My.TFrame')
frame_rez = ttk.Frame(notebook, style='My.TFrame')

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
frame4.pack(fill=BOTH, expand=True)
frame5.pack(fill=BOTH, expand=True)
frame6.pack(fill=BOTH, expand=True)
frame_rez.pack(fill=BOTH, expand=True)

notebook.add(frame1, text="1")
notebook.add(frame2, text="2")
notebook.add(frame3, text="3")
notebook.add(frame4, text="4")
notebook.add(frame5, text="5")
notebook.add(frame6, text="6")
notebook.add(frame_rez, text="Результат")



label1 = ttk.Label(frame1, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label1.grid(row=0, column=4, padx=10, pady=10)

selected_option = StringVar()
selected_option.set("30.8")
options = ['30.8', '27.2', '28.4', '30.3']
for index, option in enumerate(options):
    rb = Radiobutton(frame1, text=option, variable=selected_option, value=option,width=8, font=('Brush Script MT', 12))
    rb.grid(row=index + 1, column=4, sticky=W, padx=10)

label2 = ttk.Label(frame2, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label2.grid(row=0, column=4, padx=10, pady=10)

color = StringVar()
color.set('30.8')

class_combobox = Combobox(frame2, textvariable=color, values=['30.8', '27.2', '28.4', '30.3'],width=40,font=('Brush Script MT', 11))
class_combobox.grid(row=3, column=4, padx=5, pady=5, sticky="w")
class_combobox.bind("<<ComboboxSelected>>")

label3 = ttk.Label(frame3, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label3.grid(row=0, column=0, padx=10, pady=10)

list = Listbox(frame3, width=40, height=4,font=('Brush Script MT', 12))
list.grid(row=2, column=0, padx=10, pady=20)

for i in ['30.8', '27.2', '28.4', '30.3']:
    list.insert(END, i)

label4 = ttk.Label(frame4, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label4.grid(row=0, column=0, padx=10, pady=10)

spinbox_var = StringVar()
spinbox_var.set('30.8')

spinbox = Spinbox(frame4, values=('30.8', '27.2', '28.4', '30.3'),width=40, font=('Brush Script MT', 12),textvariable=spinbox_var)
spinbox.grid(row=1, column=0)

label5 = ttk.Label(frame5, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label5.grid(row=0, column=0, padx=10, pady=10)

selected_option = StringVar()

def select_option(option):
    selected_option.set(option)

for index, option in enumerate(options):
    Checkbutton(frame5, text=option, width=10, font=('Brush Script MT', 12), variable=selected_option, onvalue=option, command=lambda option=option: select_option(option)).grid(row=index+1, column=0, sticky=W)
label6 = ttk.Label(frame6, text="Вкажіть результат операції:\nX=2+9*((3*12)-8)/10",style='Color.TLabel')
label6.grid(row=0, column=0, padx=10, pady=10)

buttons = []
for index, option in enumerate(options):
    b = Button(frame6, text=option,width=7, height=3)
    b.grid(row=index + 1, column=0, pady=5)
    buttons.append(b)

label_rez = ttk.Label(frame_rez, text="Результат ваших відповідів:")
label_rez.grid(row=0, column=0, padx=10, pady=10)

but = Button(frame_rez, text="Показати обрані значення", command=show)
but.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()