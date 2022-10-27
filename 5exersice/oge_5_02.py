for b in range (2, 1000):
    R=4+2+2+2
    R=R*b+2
    if (R==72):
        print(str(b)+ " - " + str(R))
    else:
        print("не найдено")