# example read  write file

f = open('text.txt', 'r')  # open file
print(f.read())  # read file
f.close()

f = open('text.txt', 'r')  # open file
print(f.read(1))  # read  first symbol
f.close()

f = open('text.txt', 'r')  # open file
for line in f:
    print(line)
f.close()

f = open('text.txt', 'a')  # open file for write
f.write('new text  ')  # write in file
f.close()

f = open('text.txt', 'r')  # open file
for line in f:
    print(line)
f.close()
