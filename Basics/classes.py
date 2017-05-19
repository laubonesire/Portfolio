# Basic usage of a class in Python


class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("The name of the team is {}".format(self.name))


ars = Team("Arsenal FC")
mun = Team("Manchester United")

ars.print_name()
mun.print_name()
