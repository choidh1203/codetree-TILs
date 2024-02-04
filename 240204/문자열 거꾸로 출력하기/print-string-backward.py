notEnd = True

while notEnd:
    string = input()
    if string =="END":
        notEnd = False
        continue
    string = list(string)
    string.reverse()
    print("".join(string))