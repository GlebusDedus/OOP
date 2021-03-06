class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, 
              ", и сейчас я чувствую себя", self.mood, 'Я голоден на', self.hunger, 'единиц, и мне скучно на', self.boredom, 'единиц.')
        self.__pass_time()

    def eat(self, food=0):
        self.food=food
        food=int(input('Введите сколько еды вы хотите дать: '))
        print("ты серьёзна думаешь что я буду это есть?")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=0):
        self.fun=fun
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def pain(self, fun=0):
        self.fun=fun
        print("ай! не бей меня!")
        self.boredom += fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    
    def deid(self,boredom,hunger):
        if self.boredom > 10 or self.hunger>10:
            print('ты ужасный хозяин звирушка сдохла')
            choise=0

def main():
    import random
    crit1_name = input("Как вы назовете свою первую зверюшку?: ")
    crit2_name = input("Как вы назовете свою вторую зверюшку?: ")
    crit3_name = input("Как вы назовете свою третью зверюшку?: ")
    crit4_name = input("Как вы назовете свою четвёртую зверюшку?: ")
    crit1 = Critter(crit1_name, random.randint(1, 10), random.randint(1,10))
    crit2 = Critter(crit2_name, random.randint(1, 10), random.randint(1,10))
    crit3 = Critter(crit3_name, random.randint(1, 10), random.randint(1,10))
    crit4 = Critter(crit4_name, random.randint(1, 10), random.randint(1,10))
    animals=[crit1, crit2, crit3, crit4]

    choice = None  
    while choice != "0":
        print \
        ("""
        Мои зверюшки
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшек
        2 - Покормить зверюшек
        3 - Поиграть со зверюшками
        4 - спалить ферму
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            for i in animals:
                animal=i
                animal.talk()
        # кормление зверюшки
        elif choice == "2":
            for i in animals:
                animal=i
                animal.eat()
        # игра со зверюшкой
        elif choice == "3":
            d=int(input('1 - покормить зверушку   2 - ударить зверушку '))
            if d==1:
                for i in animals:
                    animal=i
                    animal.play()
                    animal.deid()
            if d==2:
                for i in animals:
                    animal=i
                    animal.pain()
                    animal.deid()
        # da
        elif choice=='4':
            print('горит ясно daa')
            
        # непонятный пользовательский ввод
        else:
            print("я хз, что ты хочешь от этой машины?", choice)
    

main()


