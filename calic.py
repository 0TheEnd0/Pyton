import math
def fac(a,b = 1):
    for i in range(a):
        b = b * (i + 1)
    return(b)

a = 1
A = 0
С = 0
b = 0
func = ""
while(func != "exit"):
    print("что вы хотите сделать? :","\n","найти факториал n!(P) - 1","\n","найти размещение(A) - 2","\n","найти сочетание(C) - 3","\n","для выноса из под корня или возвездение в квадрат - 4","\n","для выхода пропишите exit")
    func = input()
    if (func == "exit"):
        break
    while(a != "exit") or (func != "exit"):
        try:
            if(int(func) == 1):
                print("Введите число для факториала n!(P), для выхода ведите back ")
                a = input()
                if(a == "back"):
                    break
                print("Ваш Факториал равен :",fac(int(a)) ,sep=" ")
            if(int(func) == 2):
                print("Введите число n и число m для размещения(A), для выхода введите back")
                a = input()
                if (a == "back"):
                    break
                b = int(input())
                A = fac(b) / fac((b - int(a)))
                print(A)
            if(int(func) == 3):
                print("Введите число n и m для сочетания(C), для выхода пропишите back")
                a = input()
                if(a == "back"):
                    break
                b = int(input())
                C = fac(b) / ((fac((b - int(a)))) * fac(int(a)))
                print(C)
            if(int(func) == 4):
                print("введите нужное число для выноса из под корня или возведение в квадрат, для выходв пропишите back")
                a = input()
                if (a == "back"):
                    break
                print("ваш корень",math.sqrt(int(a)))
                print("ваш квадрат", int(a) * int(a))
            if(int(func) == 5):
                a = input()
                if (a == "back"):
                    break
                b = int(input())
                print("у")
        except ValueError:
            print("ведите число,а не слово")
            a = "back"
        finally:
            print("Комбинарный калькулятор закончил работу")