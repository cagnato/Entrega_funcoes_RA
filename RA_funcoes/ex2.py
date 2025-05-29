def e_palindromo(texto):
    inverso = texto[::-1]
    if texto == inverso:
        return True
    
print(e_palindromo("bola"))