
class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry


class Building:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.stages = {}

    def __len__(self):
        return len(self.stages)

    def __setitem__(self, key, value):
        self.stages[key] = value

    def __getitem__(self, item):
        return self.stages[item]


building1 = Building('Atower', 'Bronks')
print(type(len(building1)))
ibm = Company('IBM', 'IT')
boeing = Company('Boeing', 'defence')
building1[ibm.name] = ibm
building1[boeing.name] = boeing
print(len(building1))
print(building1['IBM'])