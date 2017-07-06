def convert(s):
    '''Conver to an integer'''
    try:
        x = int(s)
    except ValueError:
        x = -1
    return x


a=convert("hedohodo")
print(a)
b=type(a)
print(b)
