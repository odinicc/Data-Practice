file_name = "dd.py"
file_out = "gg.py"

inf = open(file_name, 'r')
outf = open(file_out, "w")
Lines = inf.readlines()
for row in range(len(Lines)):
    #print(Lines[row],Lines[row][0])
    if Lines[row][0] != "#":
        outf.write(Lines[row])

inf.close()
outf.close()