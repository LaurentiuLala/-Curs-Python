def convert_temperature(value, from_unit, to_unit):
    # Convertim intai valoarea in Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return "Unitate initiala necunoscuta!"

    # Convertim din Celsius in unitatea dorităa
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9/5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return "Unitate finala necunoscuta!"
print(convert_temperature(100, "C", "F"))   # 212.0
print(convert_temperature(212, "F", "K"))   # 373.15
print(convert_temperature(0, "K", "C"))     # -273.15