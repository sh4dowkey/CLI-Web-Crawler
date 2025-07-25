import tkinter as tk
from tkinter import messagebox
import subprocess

def run_crawler():
    url = url_entry.get()
    depth = depth_entry.get()
    cmd = ["python", "cli.py", url, "--depth", depth, "--verbose"]
    subprocess.run(cmd)

root = tk.Tk()
root.title("CLI Web Crawler GUI")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="URL:").grid(row=0, column=0)
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1)

tk.Label(frame, text="Depth:").grid(row=1, column=0)
depth_entry = tk.Entry(frame, width=40)
depth_entry.grid(row=1, column=1)

tk.Button(frame, text="Start Crawl", command=run_crawler).grid(row=2, columnspan=2, pady=10)

root.mainloop()

