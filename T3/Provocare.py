def convert_temperature(v, f, t):
    C = {'C': v, 'F': (v-32)*5/9, 'K': v-273.15}[f]
    return {'C': C, 'F': C*9/5+32, 'K': C+273.15}[t]
print(convert_temperature(100, "C", "F"))
print(convert_temperature(212, "F", "K"))
print(convert_temperature(0, "K", "C"))
