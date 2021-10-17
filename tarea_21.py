# Titulo: Tarea 21 - Empezar con los algorítmos
# Autor: Alejandro Renedo
# Fecha creación: 20/09/2021
# Fecha última revisión: -

# Referencias: -

# Tarea: Programa que dado un número decimal comprendido entre el 0.0001 y el 0.9999, 
# obtenga y muestre la correspondiente fracción irreducible.

#Iniciar variables para entrar al bucle While

float_value =10.0;
int_intentos = 0;

#Bucle para que el usuario introduzca un número correcto. Le damos 5 intentos.

while (int_intentos < 5 and (float_value < 0.0001 or float_value > 0.9999)):
    
    input_value = input("Por favor, introduce un número decimal entre el 0,0001 y el 0,9999: ");
    float_value = float(input_value);
    int_intentos = int_intentos + 1;
    if float_value < 0.0001 and float_value > 0.9999:
        print ("Dispone de " + str(5 - int_intentos) + " intentos" );

#Si el número es correcto, se calcula la fracción irreducible.

if float_value > 0.0001 and float_value < 0.9999:
    print("Valor correcto. Calculando la fracción irreducible...");
    int_numerador = int(float_value * 10000);
    int_denominador = 10000;
    
    int_divisor =  int_numerador;
    
# while int_divisor <= int_numerador or int_divisor <= int_denominador:
    while int_divisor > 1:
        
        if not (int_numerador % int_divisor) and not (int_denominador % int_divisor):
                int_numerador = int_numerador // int_divisor;
                int_denominador = int_denominador // int_divisor;
        
        int_divisor= int_divisor - 1;

    print(str(int_numerador) + "/" + str(int_denominador));

#Si el número NO es correcto, se finaliza el programa.
else:
    print("Fin del progrma. No le quedan intentos");

        
    
    
    
    
    

