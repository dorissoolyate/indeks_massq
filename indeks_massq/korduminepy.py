# while True:
#     vastus=input("tahan komme!")
#     if vastus.lower()=="komm":
#         break
#     else:
#         print("koik raagivad" + vastus)
 
# vastus=""       
# while vastus.lower()!="komm":
#     vastus=input("tahan komme!")
    
#range - promezutok 1 i=0 2 i=1.....10 i=9 (start,stop,step)
# for i in range (15):
#     print(i,"samm")
    
# for i in range(10):
#     n=input("nimi: ")
#     print("\tTere", n)
 
#1 1
1
k=0
mitu=0
while k<15:
    k+=1
    n=float(input("vvedi arv" +str(k)))
    if int(n)==float(n):
        mitu+=1
    
k=0
mitu=0
while True:
    k+=1
    n=float(input("vvedi arv" +str(k)))
    if int(n)==float(n):
        mitu+=1
        if k==15: break

# mitu=0
for k in range(1,16):
    n=float(input("vvedi" +str(k)+ ". arv"))
    if int(n)==float(n):
        mitu+=1
print("taiarvude kogus: ", mitu)

#2
count_integers = 0
for i in range(15):
    try:
        number = float(input(f"vvedi 4islo {i + 1}: "))
        if number.is_integer():
            count_integers += 1
    except ValueError:
        print("error, vvedi 4islo")
print(f"{count_integers} celqh 4isel")

#16 2
#1
n=9
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i ==j:
            print(i, end=" ")
        else:
            print("0", end=" ")
    print()
    
#2
n=9
i=1
while i<=n:
    j=1
    while j<=n:
        if i==j:
            print(i, end=" ")
        else:
            print("0", end=" ")
        j+=1    
    print()
    i+=1

#15 3
#1
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()    

#2
row=0
while row<10:
    digit=0
    while digit<10:
        print(digit, end=" ")
        digit+=1
    print()
    row+=1

#8 4
#1
print(" dujmq  sm")
for inches in range(1, 21):
    cm=inches*2.54
    print(f"{inches:<7} {cm:.2f}")

#2
inches=1
while inches<=20:
    centimeters=inches*2.54
    print(f"{inches} dujmov = {centimeters:.2f} sm")
    inches+=1

#10 5
#1
max_nr=[]
for _ in range(10):
    try:
         num1 = float(input("vvedi 4islo: "))
         num2 = float(input("vvedi 4islo: "))
         max_nr.append(max(num1, num2))
    except ValueError:
        print("error")
print("4islo bolshe:")
for result in max_nr:
    print(result)      

#2
for i in range(10):
    while True:
        try:
            num1 = float(input(f"vvedi 4iclo 1 {i + 1}: "))
            num2 = float(input(f"vvedi 4islo 2{i + 1}: "))
            if num1 > num2:
                print(f"bolshee 4islo {i + 1}: {num1}")
            elif num2 > num1:
                print(f"bolshee 4islo {i + 1}: {num2}")
            else:
                print(f"4isla {i + 1} ravnq.")
            break  
        except ValueError:
            print("error vvedi 4isla")

#29 6
#1
n=9
symbol="x"
for i in range(n):
    for j in range(n):
        if i == j:
            print(symbol, end=" ")
        else:
            print("0", end=" ")
    print()

#2
n=9
symbol="x"
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j:
            print(symbol, end=" ")
        else:
            print("0", end=" ")
        j += 1
    print()
    i += 1

#28 7
#1
import random
def mini_lot():
    secret_nr = random.randint(1, 10)
    popqtki=0
    ugadano=False
    print("ugadaj 4islo ot 1 do 10")
    while not ugadano:
        try:
           ugadaj=int(input("vvedi 4islo"))
           popqtki+=1
           if ugadaj==secret_nr:
               print("ura!")
           else:
               print("haha nepravilno")
        except Error:
            print("error")
if __name__ == "__main__":
    mini_lot()

#2
import random
secret_number = random.randint(1, 15) 
max_attempts = 10  
attempts = 0
print("davaj ugadqvaj 4islo ot 1 do 15")
for attempts in range(1, max_attempts + 1):
    try:
        guess = int(input(f"popqtka {attempts}: variant: "))
        if guess == secret_number:
            print(f"ura ugadali 4islo {secret_number} za {attempts} popqtok.")
            break
        elif guess < secret_number:
            print("bolshe.")
        else:
            print("menshe.")
    except ValueError:
        print("vvedi celoe 4islo")
  

#3 8
#1
product=1
for i in range(8):
    try:
        number = float(input(f" vvedi 4islo {i + 1}: "))
        if number>0:
            product*=number
    except ValueError:
        print("error veedi 4islo.")
print(f":proizvedenije ravno {product}")

#2
product = 1
count = 0
while count<8:
    try:
        number = float(input(f"vvedi 4islo {count + 1}: "))
        if number>0:
            product*=number
            count+=1
        else:
            print("polozhitelnoe 4islo.")
    except ValueError:
        print("error vvedi 4islo")
print(f"proizvedenie ravno {product}")

#20 9
#1
sum_numbers = 0
for number in range(1, 51):
    if number%5==0 or number%7==0:
        sum_numbers+=number
print(f"summa 4isel {sum_numbers}")

#2
sum_numbers =0
number =1
while number<=50:
    if number %5==0 or number%7==0:
        sum_numbers+=number
    number+=1
print(f"summa 4isel: {sum_numbers}")

#22 10
#1
sum_numbers =0
for number in range(100, 201):
    if number %17==0:
        sum_numbers+=number
print(f"summa 4isel {sum_numbers}")

#2
sum_numbers =0
number =100
while number<=200:
    if number%17==0:
        sum_numbers+=number
    number+=1
print(f"summa 4isel {sum_numbers}")