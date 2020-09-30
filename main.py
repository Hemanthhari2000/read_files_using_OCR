
from speak import speak

content = ""

with open('./files/file2.txt', 'r') as f:
	content = f.read()

print(content)
speak(content)
