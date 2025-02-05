# if the file does not exist, python will throw an error
f = open('another_file.txt', 'w')
f.write('Hello world!')
f.close()