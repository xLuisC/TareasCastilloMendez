def separa_letras(cadena):
    """
    La funci�n se encarga de separar un string en un string que contiene
    solo las may�sculas y otro que contiene solo las min�sculas separados.
    Asimismo, verifica que sea un string v�lido y si no lo es, brinda un
    c�digo de error �nico.
    Input: cadena (str)
    Output: c�digo de error (int), upper (str), lower (str)
    """

    # Strings con las may�sculas y min�sculas resultantes
    upper = ""
    lower = ""

    # Si la cadena est� vac�a se detiene el programa
    # con el c�digo de error '-300'
    if cadena == '':
        return -300, None, None

    # Si la cadena no es un string, se detiene el programa
    # con el c�digo de error '-100'
    if not isinstance(cadena, str):
        return -100, None, None

    # Si la cadena contiene otros caracteres que no son alfab�ticos,
    # el programa se detiene con un c�digo de error de -200
    if not cadena.isalpha():
        return -200, None, None

    # Se recorre la cadena para comprobar si el caracter es may�scula
    # o min�scula y los va agrgando a su respectivo string
    for i in cadena:
        if i.isupper():
            upper += i
        else:
            lower += i

    return 0, upper, lower


# Funci�n potencia, recibe la base y el exponente (potencia).

def potencia_manual(base, potencia):

    # Variables creadas para almacenar resultados intermedios y finales.
    result = 0
    mid_result = 0

    # que determina si las entradas son strings.
    # el caso de que así sea, devuelve el codigo de error �nico
    # y un none como resultado.
    if type(base) is str or type(potencia) is str:
        return -400, None

    # Condici�n que en caso de que ambas entradas sean enteros,
    # calcula la potencia ingresada.
    else:
        result = base  # Se asigna a la variable resutado el valor de la base.
        for i in range(1, potencia):  # ciclo for que se va a ejecutar n-1
            # veces siendo n el valor de la potencia.

            for j in range(base):  # ciclo fo que se va a ejecutar n veces
                # siendo n el valor de la base.
                mid_result = mid_result+result  # asigna a el resiltado
                # intermedio el valor de si mismo m�s el valor del resultado.
            result = mid_result  # Se asigna al resultado el valor del
            # resultado medio al final del ciclo del for interno.
            mid_result = 0  # Se asigna el resultado medio como cero para pasar
            # nuevamente con la suma en caso de que la potencia sea mayor a 2.

        # ejemplo de ciclo de 3^3: primer ciclo de for i, ciclo for de j 3
        # veces: 0+3,3+3,6+3, segundo ciclo for de i: result = 9,
        # ciclo for de j 3 veces: 0+9,9+9,18+9, Fin de ciclos for,
        # resultado final = 27.
        return 0, result
