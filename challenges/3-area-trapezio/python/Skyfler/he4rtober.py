baseMaior = float(input('Base maior : '))
baseMenor = float(input('Base menor : '))
altura = float(input('Altura : '))

def formula(basemenor,basemaior,altura):
    A = (basemaior + basemenor) * altura / 2
    return A

print(formula(baseMenor,baseMenor,altura))
