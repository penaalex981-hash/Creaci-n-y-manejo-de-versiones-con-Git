
#Los operadores lógicos se utilizan para combinar expresiones booleanas.
#Ejemplos de operadores lógicos en Python incluyen AND, OR y NOT.


#AND devuelve True solo si ambas expresiones son verdaderas.
# AND
Result1 = True and True # True
Result2 = True and False # False
Result3 = False and True # False
Result4 = False and False # False


#OR devuelve True si al menos una de las expresiones es verdadera.
#OR
Result5 = True or True # True
Result6 = True or False # True
Result7 = False or True # True
Result8 = False or False # False


#NOT
# NOT invierte el valor de una expresión booleana.
Result9 = not True # False
Result10 = not False # True
  

#Ejercicio de práctica:
#Crea una expresión que utilice los operadores lógicos AND, OR y NOT para evaluar


tiene_permiso_padres = True or False
entrego_tarea = True or True
esta_castigado = not False
puede_salir = tiene_permiso_padres and entrego_tarea or not esta_castigado
print("¿Puede salir el estudiante?", puede_salir)  # Debería imprimir: ¿Puede salir el estudiante? True

# Type your code below
var = 5

# Don't change the line below
print(f'var = {var}')

