f = open('/home/clencyc/Dev/AWS/PythonScriting/some_file.txt', 'r')
# r resprents read only mode
file_data = f.read()
f.close()

print(file_data)

files = []
for i in range(10000):
    files.append(open('/home/clencyc/Dev/AWS/PythonScriting/some_file.txt', 'r'))
    print(i)

# if the file does not exist, python will throw an error
f = open('another_file.txt', 'r')
f.write('Hello world!')
f.close()