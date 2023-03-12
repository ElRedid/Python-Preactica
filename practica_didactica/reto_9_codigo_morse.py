# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#  la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.

alfaveto = { "a" : ".-", "b" : "-...", "c" : "-.-.", "ch" : "----", "d" : "-..",
         "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---",
         "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "ñ" : "--.--", "o" : "---",
         "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-",
         "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..", "0" : "-----", "1" : ".----",
         "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...",
         "8" : "---..", "9" : "----.", "." : ".-.-.-", "," : "--..--", "?" : "..--..", "\"" : ".-..-.",
         "/" : "-..-.", " " : "/", "" : ""
    
}
texto_natural = list(alfaveto.keys())
morse = list(alfaveto.values())

entrada = input("Conversor de codigo morse:\n")
entrada = entrada.lower()
limpio = str()
for i in entrada:
    if i != "." and i != "-" and i != " " and i != "/":
        limpio += i
resultado = str()
traduccion = str()
if limpio:
    for i in entrada:
        resultado += alfaveto[i] + " "
else :
    desencriptado = str()
    for i in entrada + " ": 
        if i != " ":
            desencriptado += i
        else:
            resultado += texto_natural[morse.index(desencriptado)]
            desencriptado = str()
print(resultado)