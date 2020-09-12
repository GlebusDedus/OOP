class Critter:
    total = 0

    @staticmethod
    def status():
        print("общее число зверюшек",Critter.total)

    def __init__(self,name,hunger=0,boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total +=1
    def talk(self):
        print("меня зовут",self.name)
    def __str__(self):
        ans = 'Обьект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

def main():
    print("доступ к атрибуту класса Critter.total:", end=" ")
    print(Critter.total)

    print("Сoздание зверюшек.")
    crit1 = Critter('зверюшек 1')
    crit2 = Critter('зверюшек 2')
    crit3 = Critter("зверюшек 3")
    Critter.status()

    print('доступ к атрибуту класса через сбьект:', end='')
    print(crit1.total)

main()