# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:28:07 2022

@author: Admin
"""

import pyperclip
import pyshorteners
from tkinter import *
root = Tk()
root.geometry ("400x400")
root.title("URL Shortner")
root.configure(bg="#EAB1A5")
url = StringVar()
url_address = StringVar()

def urlshortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="Enter URL to be shortened ", font="poppins").pack (pady=8)
Entry (root, textvariable=url).pack(pady=5)
Button (root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button (root, text="Copy URL",command = copyurl).pack(pady=5)

root.mainloop()