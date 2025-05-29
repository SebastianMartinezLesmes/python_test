def detectar_picos(valores):
    picos = []
    for i in range(1, len(valores)-1):
        if valores[i] > valores[i-1] and valores[i] > valores[i+1]:
            picos.append((i, valores[i]))
    return picos

valores = [1, 3, 7, 6, 2, 4, 6, 1]
print(detectar_picos(valores))
