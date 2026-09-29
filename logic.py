class Test():
    def __init__(self, age, p1, p2, p3):
        self.age = int(age) if age else 0
        self.p1 = int(p1) if p1 else 0
        self.p2 = int(p2) if p2 else 0
        self.p3 = int(p3) if p3 else 0

def ruffier_index(p1, p2, p3):
    """Calcula el índice de Ruffier."""
    return (4 * (p1 + p2 + p3) - 200) / 10

def ruffier_result(r_index, age):
    """Evalúa el nivel de rendimiento cardíaco según la edad."""
    if age < 7:
        return "No hay datos para esta edad"

    # Determinar el nivel de partida según la edad
    if age in (7, 8):
        norm = 16.5
    elif age in (9, 10):
        norm = 15.0
    elif age in (11, 12):
        norm = 13.5
    elif age in (13, 14):
        norm = 12.0
    else:  # 15 años o más
        norm = 10.5

    # Evaluar el índice de acuerdo con el umbral correspondiente
    if r_index >= norm:
        return "Bajo"
    elif r_index >= norm - 4:
        return "Satisfactorio"
    elif r_index >= norm - 9:
        return "Bueno"
    elif r_index >= norm - 14.5:
        return "Muy bueno"
    else:
        return "Excelente"





from time import sleep
def set_timer(num):
    for i in range(num, 0):
        print(i)
        sleep(1)

set_timer(10)
