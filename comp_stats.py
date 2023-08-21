import psutil
import time
import tkinter as tk


def get_disk_usage_percentage():
    disk_usage = psutil.disk_usage('/')
    usage_percentage = disk_usage.percent
    return usage_percentage


def get_ram_usage_percentage():
    ram_usage = psutil.virtual_memory()
    usage_percentage = ram_usage.percent
    return usage_percentage


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def update_label():
    current_time = time.strftime('%H:%M:%S')
    disk_percentage = get_disk_usage_percentage()
    ram_percentage = get_ram_usage_percentage()
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    battery_percentage = battery.percent
    power_plugged = battery.power_plugged
    network_stats = psutil.net_io_counters()
    info = (f"""
            Aktualny czas: {current_time}
            Procentowe użycie procesora: {cpu_usage_percent}%
            Procent zajęcia dysku twardego: {disk_percentage}%
            Procent zajęcia pamięci RAM: {ram_percentage}%\n
            {"=" * 30}\n
            Poziom baterii: {battery_percentage}%
            Czas pozostały do rozładowania baterii: {(secs2hours(battery.secsleft))}
            Czy podłączono do zasilania: {'Tak' if power_plugged else 'Nie'}
            {"=" * 30}\n
            Przesłane pakiety danych: {network_stats.packets_sent}
            Odebrane pakiety danych: {network_stats.packets_recv}
            """)
    label.config(text=info)
    label.after(500, update_label)


root = tk.Tk()
root.title("Statystyki komputera")

label = tk.Label(root)
label.pack()

update_label()

root.mainloop()
