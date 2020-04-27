# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    str = line[pos+1:]
    fval = float(str)
    s = s + fval
    count = count + 1
    #print(fval)

if count > 0:
    ASC = s / count
    print('Average spam confidence:', ASC)

else :
    print("there is no appropriate data!")
