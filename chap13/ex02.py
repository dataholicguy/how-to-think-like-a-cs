def filter_snake(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if 'snake' in text:
            outfile.write(text)
        else:
            continue
    infile.close()
    outfile.close()

filter_snake('snake.txt', 'filter_snake.txt')
