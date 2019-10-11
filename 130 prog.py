class fraction:
    #gcd=0
    print("enter numerator")
    __n=int(input())
    print("enter denominator")
    __d=int(input())
    __den=__d
    __num=__n
    
    def display(self):
        self.__gcd()
        self.__simplify()

    def __gcd(self):
        while self.__den!=0:
            gcd=self.__den
            self.__den=self.__num%self.__den
            self.__num=gcd
        print("gcd is:",gcd)
        print("siplified numenator fraction:",self.__n//gcd)
        print("simplified denominator fraction:",self.__d//gcd)


    def __simplify(self):
       print("numerator is:",self.__n)
       print("denominator is:",self.__d)

    
obj1=fraction()
obj1.display()
        
