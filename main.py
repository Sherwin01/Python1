class Clubmembers:
    def __init__(self, name, birthday, age, favoritefood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoritefood = favoritefood
        self.goal = goal

    def dp1(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food:", self.favoritefood)
        print("Goal:", self.goal)


class Clubofficers(Clubmembers):

    def __init__(self, name, birthday, age, favoritefood, goal, position):
        self.position = position
        Clubmembers.__init__(self, name, birthday, age, favoritefood, goal)

    def dp2(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food:", self.favoritefood)
        print("Goal:", self.goal)
        print("Position:", self.position)


m_1 = Clubmembers("Tom", "January 16", 14, "Ice Cream", "To be happy")
o_4 = Clubofficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.dp1()
o_4.dp2()







