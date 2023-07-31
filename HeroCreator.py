class Hero:

    listOfHeroes = {}
    classes = ['Druid', 'Mage', 'Warrior', 'Soldier', 'King']

    def __init__(self):
        heroName, heroClass = self.setUpHero()
        self.heroName = heroName
        self.heroClass = heroClass
        self.heroHealth = 100
        self.heroCharisma = 50
        Hero.listOfHeroes[self.heroName] = {"Class": self.heroClass}

    @classmethod
    def setUpHero(cls) -> list:
        heroName = input("Set up your hero name: ").title()
        while not heroName:
            print("\nHero without name.\n")
            heroName = input("Set up your hero name: ").title()
        print("Classes avaliable:\n")
        #for heroInformations in cls.listOfHeroes.values():
        #    if cls.classes in heroInformations["Class"]:
        #        print(f" - {heroInformations["Class"]} (Unvaliable)")
        #    else:
        #        print(f" - {heroInformations["Class"]}")
        heroClass = input(f"\n{heroName}, set up your hero class: ").title()
        if not heroClass:
            return heroName, 'Undefined'
        return heroName, heroClass

    def __call__(self):
        print(f"Hero name: {self.heroName}\nHero class: {self.heroClass}")

Hero()()
print(Hero.listOfHeroes)
Hero()()
print(Hero.listOfHeroes)
