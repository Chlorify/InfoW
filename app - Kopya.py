import GPUtil
import tkinter as tk
import psutil
from cpuinfo import get_cpu_info
import os
import wmi

#current_process = psutil.Process()
#current_process.cpu_affinity([1])
cpuinfo1 = get_cpu_info()['brand_raw']
cpuinfo2 = get_cpu_info()['count']
battery = psutil.sensors_battery()
ram = psutil.virtual_memory()

def get_gpu_temperature():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_temperature = gpus[0].temperature
            return gpu_temperature
            
        else:
            return "No GPU Found"
    except Exception as e:
        return str(e)
    
def get_gpu_name1():
    try:
        global gpu_name1
        gpu_name1 = wmi.WMI().Win32_VideoController()[0].name
        return gpu_name1
    except IndexError:
        return "GPU Not Found"
    
def get_gpu_name2():
    try:
        global gpu_name2
        gpu_name2 = wmi.WMI().Win32_VideoController()[1].name
        return gpu_name2
    except IndexError:
        return "GPU Not Found"
   
gpu1 = get_gpu_name1()
gpu2 = get_gpu_name2()  

def update_temperature_label():
    temperature = get_gpu_temperature()
    temperature_var.set(f"{temperature} °C")
    root.after(1000, update_temperature_label)

def update_battery_label():
    battery = psutil.sensors_battery()
    battery_var.set(f"{battery.percent} %")
    root.after(1000, update_battery_label)

def update_ram_label():
    ram = psutil.virtual_memory()
    ram_var.set(f"{ram.percent} %")
    root.after(1000, update_ram_label)

def update_ram_label2():
    ram = psutil.virtual_memory()
    ram_in_mb = ram.available / 1024 / 1024 
    formatted_ram = int(round(ram_in_mb))   # Round and convert to integer
    ram_var1.set(f"{formatted_ram} MB")
    root.after(1000, update_ram_label2)

def update_ram_label3():
    ram = psutil.virtual_memory()
    ram_in_mb = ram.used / 1024 / 1024  # Convert RAM to megabytes
    formatted_ram = int(round(ram_in_mb))   # Round and convert to integer
    ram_var2.set(f"{formatted_ram} MB")
    root.after(1000, update_ram_label3)

#def update_cpuper_label():
    #cpu_usage = psutil.cpu_percent(interval=1)
    #cpuper_var.set(f"{cpu_usage} %")
    #root.after(1000, update_cpuper_label)
          

bgcolor = "#333333"
fgcolor = "#FFFFFF"

root = tk.Tk()
root.geometry("600x500")
root.title("InfoW")

icon_path = "logo5.png"  # Replace with your icon file's name and path
if os.path.exists(icon_path):
    root.iconphoto(True, tk.PhotoImage(file=icon_path))
else:
    print("Icon file not found.")
    

frame = tk.Frame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=True)
frame.configure(bg=bgcolor)


#CPU label
label = tk.Label(master=frame, text="CPU: " + cpuinfo1, font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)

label = tk.Label(master=frame, text=f"Threads: {cpuinfo2}", font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)

#Gpu 1
label = tk.Label(master=frame, text="GPU1: " + gpu1, font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)
#Gpu 2
label = tk.Label(master=frame, text="GPU2: " + gpu2, font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)
#Gpu 2 Temperature
label = tk.Label(master=frame, text="GPU2 Temperature:", font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)
temperature_var = tk.StringVar()
label = tk.Label(master=frame, textvariable=temperature_var, font=("Arial", 25))
label.pack(pady=0, padx=10)
label.configure(bg="#555556", fg=fgcolor)
#Cpu Temperature(coming soon sory)
label = tk.Label(master=frame, text="Cpu Temperature:(not available)", font=("Arial", 10))
label.pack(pady=10, padx=10)
label.configure(bg=bgcolor, fg=fgcolor)
cputemperature_var = tk.StringVar()
label = tk.Label(master=frame, textvariable=cputemperature_var, font=("Arial", 25))
label.pack(pady=0, padx=10)
label.configure(bg="#555556", fg=fgcolor)

#label = tk.Label(master=frame, text="Cpu Temperature:", font=("Arial", 10))
#label.pack(pady=10, padx=10)
#label.configure(bg=bgcolor, fg=fgcolor)

#cpuper_var = tk.StringVar()
#label = tk.Label(master=frame, textvariable=cpuper_var, font=("Arial", 25))
#label.pack(pady=0, padx=10)
#label.configure(bg="#555556", fg=fgcolor)

#ram usage
label = tk.Label(master=frame, text="Ram Usage:", font=("Arial", 10))
label.place(x=5, y=10)
label.configure(bg=bgcolor, fg=fgcolor)
ram_var = tk.StringVar()
label = tk.Label(master=frame, textvariable=ram_var, font=("Arial", 15))
label.place(x=10, y=40)
label.configure(bg="#555556", fg=fgcolor)
#Free ram variable
label = tk.Label(master=frame, text="Free Ram:", font=("Arial", 10))
label.place(x=5, y=80)
label.configure(bg=bgcolor, fg=fgcolor)
ram_var1 = tk.StringVar()
label = tk.Label(master=frame, textvariable=ram_var1, font=("Arial", 15))
label.place(x=10, y=110)
label.configure(bg="#555556", fg=fgcolor)
#Used ram variable
label = tk.Label(master=frame, text="Used Ram:", font=("Arial", 10))
label.place(x=5, y=150)
label.configure(bg=bgcolor, fg=fgcolor)
ram_var2 = tk.StringVar()
label = tk.Label(master=frame, textvariable=ram_var2, font=("Arial", 15))
label.place(x=10, y=170)
label.configure(bg="#555556", fg=fgcolor)
#battery percentage for laptops
label = tk.Label(master=frame, text="Battery:", font=("Arial", 10))
label.place(x=5, y=210)
label.configure(bg=bgcolor, fg=fgcolor)
battery_var = tk.StringVar()
label = tk.Label(master=frame, textvariable=battery_var, font=("Arial", 15))
label.place(x=10, y=240)
label.configure(bg="#555556", fg=fgcolor)

#update_cpuper_label()
update_ram_label3()
update_ram_label2()
update_ram_label()
update_battery_label()
update_temperature_label()  # Start the automatic updating

root.mainloop()