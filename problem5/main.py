def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string_original = "Bruno"
print(f"String invertida de '{string_original}': '{inverter_string(string_original)}'")