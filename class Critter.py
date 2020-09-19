class Critter:
    total = 0

    @property
    def mood(self):
        unhappiness =self.hunger + self.boredom
        if unhappiness < 5:
            m = "briliant"
        elif 5<= unhappiness <=10:
            m="good"
        elif 11<= unhappiness <=15:
            m="not bad"
        else:
            m="bad"
        return m

    @staticmethod
    def status():
        print("общее число зверюшек",Critter.total)

    def __init__(self,name,hunger=0,boredom=0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total +=1
    def talk(self):
        print("меня зовут",self.name,
        ", и сейчас я чувстую себя", self.mood)
    def __str__(self):
        ans = 'Обьект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    def eat(self,food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

def main():
    print("доступ к атрибуту класса Critter.total:", end=" ")
    print(Critter.total)

    print("Сoздание зверюшек.")
    crit1 = Critter('зверюшек 1')
    crit2 = Critter('зверюшек 2')
    crit3 = Critter("зверюшек 3")
    Critter.status()

    print('доступ к атрибуту класса через сбьект:', crit1.mood)

main()