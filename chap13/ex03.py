def copy_file(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')

    i = 1
    layout = '{0:04d} {1}'
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        line = layout.format(i, text)
        outfile.write(line)
        i += 1
    infile.close()
    outfile.close()


copy_file('input.txt', 'copy.txt')
