#wordly
"""import string
newlist2 = []
txt_file = open("src\dictionary.txt", "r") #whole dictionart
file_content = txt_file.read()

content_list = file_content.split('\n')
txt_file.close()

textfile = open("asdada.txt", "w")

#only 5 letters words with only lower cases

for val in content_list:
  if len(val) == 5 and val.islower() == True : 
    newlist2.append(val)

for element in newlist2:
    textfile.write(element + "\n")
textfile.close()"""

file = open("src\words.txt", "r")

words = []

for item in file:
  y = item.strip()
  x = y.split()
  words.append(x)
