def func(param):
    global nameList
    x = (nameList[0:-1])
    print(*x, sep=", ", end=' ')
    print('and', end=' ')
    print(nameList[-1])

nameList = ['Sox','Misty','Patches','Zulu','Homer','Lucky']

func(nameList)