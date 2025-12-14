notes = input().split()
if notes[0]<notes[1]<notes[2]<notes[3]<notes[4]<notes[5]<notes[6]<notes[7]:
    print("ascending")
elif notes[0]>notes[1]>notes[2]>notes[3]>notes[4]>notes[5]>notes[6]>notes[7]:
    print("descending")
else:
    print("mixed")