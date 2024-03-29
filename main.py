class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
            print(f"{self.name} ест")

    def sing(self):
        print(f"{self.name} поет - {self.voice}")


    def info(self):
        print(f"имя - {self.name}")
        print(f"голос - {self.voice}")
        print(f"цвет - {self.color}")

class Pigeon(Bird):
   def __init__(self, name, voice, color, favorite_food):
       super().__init__(name, voice, color)
       self.favorite_food = favorite_food

   def walk(self):
    print(f"{self.name} ходит")


bird1 = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")
bird2 = Bird("Маша", "Чирик", "Коричневый")


bird1.sing()

bird1.info()

bird1.walk()



