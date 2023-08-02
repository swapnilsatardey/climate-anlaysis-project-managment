# Todo: Code is a bit unclear

def Fc(x):
    celsius = (x - 32) * (5 / 9)
    return celsius

def FK(x):
    y = Fc(x)
    z = y + 273.15
    return z
