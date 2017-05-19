# Using classes and Object Oriented Programming in Python


# Class Person describes a normal person, who has a name
class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}".format(self.name))


bob = Person("Bob")
bob.reveal_identity()


# Class "SuperHero" has an identity (Person object), and a Hero name
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))


bruce = SuperHero("Bruce Wayne", "Batman")
bruce.reveal_identity()
