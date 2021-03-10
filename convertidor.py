class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def description(self):
        return 'convertir ' + self.units_from + ' en ' + self.units_to

    def convert(self, value):
        return value * self.factor
    

c1 = ScaleConverter('pulgadas', 'mm', 25)
print (c1.description())
print ('convirtiendo 2 pulgadas')
print(str(c1.convert(2)) + c1.units_to)
