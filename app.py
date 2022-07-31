text = input("Ingrese una operacion en texto: ")

def filtroTexto(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("uno", "1")
    text = text.replace("dos", "2")
    text = text.replace("tres", "3")
    text = text.replace("cuatro", "4")
    text = text.replace("cinco", "5")
    text = text.replace("seis", "6")
    text = text.replace("siete", "7")
    text = text.replace("ocho", "8")
    text = text.replace("nueve", "9")
    text = text.replace("cero", "0")
    text = text.replace("mas", "+")
    text = text.replace("menos", "-")
    text = text.replace("por", "*")
    text = text.replace("entre", "/")
    return text

def calculo(textoFiltrado):
    try:
        print(textoFiltrado)
        resultado = eval(textoFiltrado)
        print(resultado)
    except:
        print("Ingrese una operacion o numero valido")
    return resultado

textoFiltrado = filtroTexto(text)
resultado = calculo(textoFiltrado)
