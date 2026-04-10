class Human:
    def __init__(self,name,gender, balance=62000, age=38, height=175, strength=10, iq=100, intelligence=10, education_level=10, social_confidence=10, agility=10, endurance=10, perception=10 , ):
        if age > 78:
            print('this person is dead')
            self.dead = True
        else:
            self.name = name
            self.balance = balance
            self.age = age
            self.height = height
            self.strength = strength
            self.iq = iq
            self.intelligence = intelligence
            self.education_level = education_level
            self.social_confidence = social_confidence
            self.agility = agility
            self.endurance = endurance
            self.perception = perception
            self.gender = gender
            self.dead = False

    
    def buy(self, price):
        if self.dead:
            print('This person is dead')
        else:
            if self.balance > price:
                self.balance -= price
            else:
                print(f"{self.name}'s purchace failed")


