def undo_numbering(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')

    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        words = text.split()
        del words[0]
        new_text = ' '.join(words)
        outfile.write(new_text+'\n')

    infile.close()
    outfile.close()

undo_numbering('copy.txt', 'no_number.txt')
