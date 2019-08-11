# Write a program that reads a file and writes out a new file with the lines in reversed order
# i.e. the first line in the old file becomes the last one in the new file.

f = open('input.txt', 'r')
xs = f.readlines()
f.close()

xs.reverse()

g = open('reversed.txt', 'w')
for v in xs:
    g.write(v)
g.close()
