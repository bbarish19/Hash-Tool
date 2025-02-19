import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, Label, Text, Button
import hashlib

def calculate_hashes(file_path):
    try:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)
        
        return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None, None, None

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name_var.set(file_path)
        md5_hash, sha1_hash, sha256_hash = calculate_hashes(file_path)
        if md5_hash and sha1_hash and sha256_hash:
            md5_var.set(md5_hash)
            sha1_var.set(sha1_hash)
            sha256_var.set(sha256_hash)

def clear_hashes():
    md5_var.set("")
    sha1_var.set("")
    sha256_var.set("")
    file_name_var.set("")

def open_eula():
    eula_text = """End User License Agreement (EULA)

By using this software, you agree to the following terms and conditions:
1. You will use the software for personal and non-commercial use only.
2. You will not reverse engineer, decompile, or disassemble the software.
3. The developer is not responsible for any damage caused by using this software."""

    def accept_eula():
        mark_eula_signed()
        eula_window.destroy()  # Close the EULA window after accepting
        callback()

    eula_window = tk.Toplevel(root)
    eula_window.title("End User License Agreement (EULA)")
    
    title_label = tk.Label(eula_window, text="======================================================================\nWELCOME TO THE HASH CREATOR\n======================================================================", font=("Helvetica", 12), anchor='center')
    title_label.pack(pady=5)

    description_label = tk.Label(eula_window, text="""8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888P""    ""9888888888888888888888888888888888
8888888888888888888888P"88888P                    988888"9888888888888888888888888
88888888888888888888888    "9888                      888P"    8888888888888888888888888
8888888888888888888888888bo "9  d8o     o8b  P" od888888888888888888888888888
888888888888888888888888888bob 98"     "8P dod88888888888888888888888888888
888888888888888888888888888888       db       88888888888888888888888888888888
888888888888888888888888888888888      88888888888888888888888888888888888
88888888888888888888888888888P"9bo  odP"98888888888888888888888888888888
88888888888888888888888888P" od88888888bo "98888888888888888888888888888
8888888888888888888888888   d88888888888888b   888888888888888888888888888
888888888888888888888888oo88888888888888888oo88888888888888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888""", font=("Helvetica", 12), anchor='center')
    description_label.pack(pady=5)

    title_label = tk.Label(eula_window, text="======================================================================\nThis tool lets you create hashes!\nProgram created by: Benjamin Barish\n======================================================================", font=("Helvetica", 12), anchor='center')
    title_label.pack(pady=5)

    # The rest of the EULA text will be left-aligned
    eula_label = tk.Label(eula_window, text=eula_text, font=("Helvetica", 12), justify=tk.LEFT, anchor='w')  # Left justify most of the content
    eula_label.pack(padx=20, pady=20)

# Create main application window
root = tk.Tk()
root.title("File Hash Generator")
root.geometry("400x250")
root.configure(bg="#e6e6e6")

# File selection button and label
file_name_var = tk.StringVar()
file_frame = tk.Frame(root, bg="#e6e6e6")
file_frame.pack(pady=10, fill='x')

select_button = tk.Button(file_frame, text="Choose File", command=select_file, bg="#0275d8", fg="white")
select_button.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(file_frame, textvariable=file_name_var, width=40, state='readonly', bg="#ffffff", relief="solid")
entry.pack(side=tk.LEFT, padx=5, expand=True, fill='x')

# Hash output fields (centered)
md5_var = tk.StringVar()
sha1_var = tk.StringVar()
sha256_var = tk.StringVar()

# Container frame for hash fields (no fill so it centers by default)
hash_frame = tk.Frame(root, bg="#e6e6e6")
hash_frame.pack(pady=5)

# Fixed width for hash entry fields
hash_width = 50

# Create a centered frame for each hash field
for label_text, var in [("MD5 Hash:     ", md5_var), ("SHA-1 Hash:   ", sha1_var), ("SHA-256 Hash:", sha256_var)]:
    # Each frame is not forced to fill the parent width, so it can center itself
    field_frame = tk.Frame(hash_frame, bg="#ffffff", relief="solid", borderwidth=2)
    field_frame.pack(pady=2, padx=5, anchor="center")
    
    tk.Label(field_frame, text=label_text, bg="#ffffff").pack(side=tk.LEFT, padx=5)
    tk.Entry(field_frame, textvariable=var, width=hash_width, state='readonly', bg="#ffffff", relief="flat").pack(side=tk.LEFT, padx=5)

# Clear Hashes button
clear_button = tk.Button(root, text="Clear Hashes", command=clear_hashes, width=20, bg="#5bc0de", fg="white")
clear_button.pack(pady=10)

# EULA button
eula_button = tk.Button(root, text="EULA", command=open_eula, width=20, bg="#5cb85c", fg="white")
eula_button.pack(pady=10)

# Run the GUI
root.mainloop()
