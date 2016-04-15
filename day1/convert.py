count = 0
name='No'
with open('cities.txt','w',encoding='utf-8') as f,open('abc.txt','r',encoding='utf-8') as g:
    for line in g.readlines():
        l_line = line.split()
        # if count >= 13:break
        # print(count,":",l_line[1])
        try:
            l_line[1]=int(l_line[1])
            if type(l_line[1]) is int:
                name = l_line[0]
                l_line.pop(1)
                line="||".join(l_line)
                print(line)
                f.write(line)
                f.write("\n")
                count += 1
                continue
        except ValueError:
            pass
            # print("Error1")

        try:
            l_line[0]=int(l_line[0])
            if type(l_line[0]) is int:
                l_line.pop(0)
                l_line.insert(0,name)
                line="||".join(l_line)
                print(line)
                f.write(line)
                f.write("\n")
                count += 1
                continue
        except(ValueError):
            pass
            # print("Error2")



