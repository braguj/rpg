class Hero:

    listOfHeroes = {}
    classes = ['Druid', 'Mage', 'Warrior', 'Soldier', 'King', 'Human']

    def __init__(self):
        heroName, heroClass = self.setUpHero()
        self._heroName = heroName
        self._heroClass = heroClass
        self.__heroHealth = 100
        self.__heroCharisma = 50
        Hero.listOfHeroes[self._heroName] = {"Class": self._heroClass}

    @classmethod
    def setUpHero(cls) -> list:
        heroName = input("Set up your hero name: ").title()
        while not heroName:
            print("\nHero without name.\n")
            heroName = input("Set up your hero name: ").title()
        print("Classes avaliable:\n")
        for classes in cls.classes:
            print(f" - {classes}")
        heroClass = input(f"\n{heroName}, set up your hero class: ").title()
        if heroClass == 'Human':
            return heroName, heroClass
        elif not heroClass:
            return heroName, 'Human'
        elif heroClass != 'Human':
            cls.classes.remove(heroClass)
            return heroName, heroClass
        else:
            return heroName, 'Human'

p1 = Hero()
p1.__heroClass = 'Druid'
print(p1.__heroClass)
