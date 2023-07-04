class Thanos:
    def __init__(self, planet):
        self._planet =  planet

    def x(self):
        print('get my planet')
        return self._planet

    def getPlanet(self):
        return self._planet

    def setPlanet(self, planet):
        print('conquer the planet')
        self._planet = planet

    def delPlanet(self):
        print('destroy planet')
        del self._planet

    planet = property(getPlanet, setPlanet, delPlanet, 'about planet attribute')

# methodneri mej karanq ognagorcenq _(taki gcik u mer attributi anun@ vor rekursia chlini)


supervillain = Thanos('Earth')
supervillain.planet = 'Mars'
print(supervillain.planet) # getPlanet
supervillain.planet = 'Black Hole' # setPlanet
del supervillain.planet # delPlanet
print(Thanos.planet.__doc__) # attribute documentation

# jarangvuma vonc vor sovorakan attribute
class Ultron(Thanos):
    pass

supervillain = Ultron('Earth')
print(supervillain.planet) # getPlanet