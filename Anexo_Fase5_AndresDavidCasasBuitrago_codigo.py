# Andres David Casas Buitrago
# 213022_723
# Ingenieria de Sistemas
# Codigo fuente: Autoria propia, Andres David Casas Buitrago
matriz=[
    ["Nombre del Recurso", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    [     "Directivos",        5,        5,         7,          4,        5],
    [     "Administrativos",   8,        8,         8,          8,        8],
    [     "Operativos",        10,       10,        7,          10,       7],
    [     "Técnicos",          7,        7,         6,          7,        7],         
    ]

# Funciones utilizadas
def umbral_de_horas(horas):
    if horas > 40: 
        return "Sobretiempo"
    elif horas <= 40: 
        return "Horario estándar"

def Calcular_suma_horas(fila):
    # Sumamos desde la columna 1 hasta el final de esa fila
    return sum(matriz[fila][1:])

# Solo necesitamos un ciclo para recorrer los datos (de la fila 1 a la 4)
for i in range(1, len(matriz)):
    recurso = matriz[i][0]
    horas_totales = Calcular_suma_horas(i)
    estado = umbral_de_horas(horas_totales)
    
    print(f"Para los {recurso}, las horas trabajadas son: {horas_totales} horas, por tanto el umbral es: {estado}")




