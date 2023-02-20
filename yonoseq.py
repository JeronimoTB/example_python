#SUMA
number1 = 16
number2 = 14
suma = number1 + number2
print("Este es el resultado de la suma: ",suma)

#RESTA
resta = number1 - number2
print("Este es el resultado de la resta: ",resta)

#MULTIPLICACION
multi = number1 * number2
print("Este es el resultado de la multiplicacion: ",multi)

#DIVISION
divi = number1 / number2
print("Este es el resultado de la division: ",divi)

"""
COMENTARIO GRANDE 
"""


print("CLASE 20/02/23")
#EJEMPLO CONVERSION DE ENTERO A FLOAT

variable = 5
variable_uno = float(variable)

#STRING
variable_dos = str(variable)

#ERROR SUMA ENTRE 2 DATOS DIFERENTES (int + str)
#suma = (variable + variable_dos)

print(variable , variable_uno, variable_dos)

#CONOCER EL TIPO DE DATO CON LA VARIABLE TYPE()
print(type(variable_dos))

#TIPOS DE DATOS
variable_str = "Hablalo" #STRING (str)
variable_int = 20             #ENTERO (int)
variable_float = 20.8         #DECIMAL (float)
variable_complex = 1j             #COMPLEX
variable_boolean = False      #LOGICO (bool)
varible_list = ["Cantar", "Jugar", "Estudiar"] #Lista = list
print(varible_list)
print("Esta variable es ", type(varible_list))

variable_tuble = ("Cantar", "Jugar", "Estudiar") #Tupla = tuble
print(variable_tuble)
print("Esta variable es ", type(variable_tuble))

carro = {"color": 'rojo', "velocidad": 300, "modelo": 'GTRR36'} #Diccionario = dict
print(carro)
print("Esta variable es ", type(carro))

print(variable_float)
print(type(variable_float))
