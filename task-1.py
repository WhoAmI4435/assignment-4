try:
    f = open("sample.txt", "r")
    a = f.readlines()
    s = 0
    for i in a:
        s = s+1
        if i[-1] == '\n':
            print("line", s, ':', i[:-1])
        else:
            print("line", s,':', i)
except FileNotFoundError:
    print("The file sample.txt was not found.")