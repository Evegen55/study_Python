# for python ver 2.7
import glob

import sys

list = glob.glob("../../data/letters/sent/1/*.eml")
count = 0
f1 = open('../../data/letters/sent/1/outputfile', 'w+')
sys.stdout = f1
s = set()
for filePath in list:
    fh = open(filePath)
    for line in fh:
        splt = line.split()
        if len(splt) == 0: continue
        if splt[0] != 'User': continue
        count = count + 1
        try:
            oathid = splt[3].strip().split('=')[1].strip()
            oathid = oathid[:-1]
            if (oathid not in s and not s.add(oathid)):
                s.add(oathid)
                # print oathid
                print splt[1].strip(), splt[2].strip(), \
                    splt[3].strip(), \
                    splt[4].strip(), splt[5].strip(), splt[6].strip(), \
                    splt[7].strip(), splt[8].strip(), splt[9].strip(), splt[10].strip(), splt[11].strip()
        except:
            #print
            continue


