from asyncore import read


file = open ("file1.txt","r")
array_from_file = file.readlines()
file.close()

print(array_from_file[0])
userAnswer = input()

if userAnswer == array_from_file[1].rstrip():
    print("Good job, you won " + array_from_file[2].rstrip() + "  points")
else:
    print("Wrong, pay me 500000000$")

