#https://www.youtube.com/watch?v=M3G1ZgOMFxo
#Shaun Halverson

#https://www.youtube.com/watch?v=dK6gJw4-NCo
#Code Coach

N = -5

if N < 0:
    print ("negative")
elif N > 0:
    print ("positive")

#----------------------------------------------------------------
n = 3

if n % 2 == 0:
    print ("Even numba")
else:
    print ("Odd numba")
#----------------------------------------------------------------
N = input("here: ")

def Palindrome(N):
    return N == N[::-1]

if Palindrome(N):
    print ("Palindrome")
else:
    print("Not a")
#----------------------------------------------------------------
S = int(input("temp: "))


Farenheit = S * 9/5 + 32 

print (Farenheit)
#----------------------------------------------------------------
for N in range (0,101):
    print (N)
#----------------------------------------------------------------
for N in range (0,11):
    print (N)
#----------------------------------------------------------------
for N in range (0,11):
     S = N * 5
     print (S)
#----------------------------------------------------------------
N = 4

if N % 2 == 0:
    print ("true") 
else:
    print ("false")
#----------------------------------------------------------------
Height = input("Height: ")
Base = input("Base: ")

Area = int(Height) * 2 + int(Base) * 2
print (Area)
#----------------------------------------------------------------
Upper = "hi broski"
print (Upper.upper())
#----------------------------------------------------------------
N = (1,2,3,4,5)

print (N[::-1])
#----------------------------------------------------------------
def listoo(S):
    List = []
    for N in S:
        if N not in List:
            List.append(N)
    return List
S = [2, 4, 10, 20, 5, 2, 20, 4]
print (listoo(S))
#----------------------------------------------------------------
lista = [8, 9, 10]
Resul = sum(lista) / len(lista)

print (Resul)
#----------------------------------------------------------------
list = [3,8,2,9]

current_max_number = list[0]
for number in list:
    if number<current_max_number:
        current_max_number = number

print (current_max_number)
#----------------------------------------------------------------
day = 86400
hour = 3600
vr = 10476
t = 60

if vr > 3600:
        H = vr / hour
if H < 3600:
        M = vr / t % 60

time = (int(H), ":",int (M))

print (time)
#-----------------------------------------------------------------v
day = 86400
hour = 3600
vr = 70447
t = 60

if vr > 3600:
        H = vr / hour
if H < 3600:
        M = vr / t % 60
        


time = (int(H), ":",int (M))

if H < 24:
        print (time)
else:
        print ("go to sleep")
#-----------------------------------------------------------------v
 
smile: 1

def face (smile):
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░█░░░░░░░░░░░░░░░░░█░░░░░░")
    print("░░░░░░░░██░░░░░░░░░░░░░░░██░░░░░░")
    print("░░░░░░░░███░░░░░░░░░░░░██░░░░░░░░")
    print("░░░░░░░░░░███░░░░░░░░███░░░░░░░░░")
    print("░░░░░░░░░░░░░██████████░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

print (smile)
