def mostrar_matriz(matriz: list[list]):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = matriz[fila][columna]
            print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')


def suma_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:
    matriz_3 = []

    for fila in range(len(matriz_1)):
        fila_de_suma = []
        for columna in range(len(matriz_1[fila])):
            suma = matriz_1[fila][columna] + matriz_2[fila][columna]
            fila_de_suma.append(suma)
        matriz_3.append(fila_de_suma)
    return matriz_3


def multiplicar_matriz_escalar(matriz: list[list], escalar: int) -> list[list]:
    """_summary_ Que hace

    Args:
        matriz (list[list]): _description_ Que recibe
        escalar (int): _description_ Que recibe

    Returns:
        list[list]: _description_ Que devuelve
    """
    matriz_3 = []
    for fila in range(len(matriz)):
        lista_mult = []
        for columna in range(len(matriz[fila])):
            resultado = matriz[fila][columna] * escalar
            lista_mult.append(resultado)
        matriz_3.append(lista_mult)
    return matriz_3


matriz_1 = [
    [5, 4, 6, 1, 9],
    [10, 15, 4],
    [70, 30, 25, 35, 10]
]

matrix_3 = multiplicar_matriz_escalar(matriz_1, 3)
mostrar_matriz(matrix_3)


def multiplicar_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:
    """_summary_ Multiplica 2 matrices 

    Args:
        matriz_1 (list[list]): _description_ Parámetro de entrada, mat. A
        matriz_2 (list[list]): _description_ Parámetro de entrada, mat B 

    Returns:
        list[list]: _description_ Devuelve matriz C
    """
    matriz_3 = []
    for fila in range(len(matriz_1)):
        lista_mult = []
        for columna in range(len(matriz_1[fila])):
            suma = 0
            for i in range(len(matriz_1[fila])):
                suma += (matriz_1[fila][i] * matriz_2[i][columna])
            lista_mult.append(suma)
        matriz_3.append(lista_mult)
    return matriz_3


# Test case for multiplicar_matrices
def test_multiplicar_matrices():
    matriz_1 = [
        [1, 2],
        [3, 4]
    ]

    matriz_2 = [
        [5, 6],
        [7, 8]
    ]

    expected_result = [
        [19, 22],
        [43, 50]
    ]
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    result = multiplicar_matrices(matriz_1, matriz_2)

    if result == expected_result:
        print(f"Test {GREEN}PASSED{RESET}")
    else:
        print(f"Test {RED}FAILED:{RESET} Expected {expected_result}, but got {result}")



if __name__ == "__main__":
    test_multiplicar_matrices()
