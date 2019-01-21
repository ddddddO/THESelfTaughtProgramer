#4
class Horse:
    def __init__(self, name, sex, rider):
        self.name = name
        self.sex = sex
        self.rider_name = rider.name
    
    def introduce(self):
        print("I am {}, horse. {} is rider.".format(self.name, self.rider_name))
    
class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("take yutaka")
horse = Horse("umagon", "male", rider)
horse.introduce()