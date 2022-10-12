#OPENING THE FILE IN APPEND MODE.IF FILE NOT PRESENT IT WILL CREATE ONE
f = open("demofile.txt", "a")
#Writing to a file at the last.  
f.write("Now the file has some content!")
f.close()
#NOW READING TH FILE
f = open("demofile.txt","r")
print(f.read())
f.close()
#NOW OPENING THE FILE IN WRITE MODE.IT OVERWITE THE TEXT
f = open("demofile.txt", "w")
f.write(" we have overwrite the text")
f.close()
f = open("demofile.txt","r")
print(f.read())
f.close()
#DELETED ALL THE CONTENT OF TH FILE
f = open("demofile.txt", "w")
f.write("")
f.close()
