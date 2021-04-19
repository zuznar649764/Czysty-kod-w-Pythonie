import math

class circle:
    def radius(self):
        while 1:
            try:
                r = float(input("Podaj promień koła: "))
                #sprawdzenie czy koło o podanym promieniu może istnieć (czy jest liczbą wiekszą od 0)
                while r < 0:
                    print("Coś poszło nie tak :(")
                    r = float(input("Podaj promień koła: "))
                break
            except:
                print("Coś poszło nie tak :(")

        return(r)

    #Pole
    def area(self, r):
        return(math.pi*r*r)

    #Obwód
    def cir(self, r):
        return(2*math.pi*r)

class triangle:

    def a(self):
        while 1:
            try:
                a = float(input("Podaj długość pierwszego boku: "))
                while a < 0:
                    print("Coś poszło nie tak :(")
                    a = float(input("Podaj długość boku: "))
                break
            except:
                print("Coś poszło nie tak :(")

        return(a)

    def b(self):
        while 1:
            try:
                b = float(input("Podaj długość drugiego boku: "))
                while b < 0:
                    print("Coś poszło nie tak :(")
                    b = float(input("Podaj długość boku: "))
                break
            except:
                print("Coś poszło nie tak :(")
        return(b)

    def c(self):
        while 1:
            try:
                c = float(input("Podaj długość trzeciego boku: "))
                while c < 0:
                    print("Coś poszło nie tak :(")
                    c = float(input("Podaj długość boku: "))
                break
            except:
                print("Coś poszło nie tak :(")
        return(c)

    #funkcja sprawdzająca czy trójkąt o podanych bokach może istnieć
    def check(self, a, b, c):
        if (a + b > c) and (b + c > a) and (a + c > b):
            x = True
        else:
            x = False
            print("Z podanych boków nie można zbudować trójkąta")
        return(x)

    #Pole (wzór Herona)
    def area(self, a, b, c):
        p = (a + b + c) / 2
        return(math.sqrt(p*(p-a)*(p-b)*(p-c)))

    #Obwód
    def cir(self, a, b, c):
        return(a + b + c)


class square:
    def side(self):
        while 1:
            try:
                a = float(input("Podaj długość boku kwadratu: "))
                while a < 0:
                    print("Coś poszło nie tak :(")
                    a = float(input("Podaj długość boku: "))
                break
            except:
                print("Coś poszło nie tak :(")

        return(a)

    #Pole
    def area(self, a):
        return(a*a)

    #Obwód
    def cir(self, a):
        return(4*a)