import datetime

class Nota:
    def __init__(self, memo, etiqueta):
        self.memo = memo
        self.etiqueta = etiqueta
        self.id = None
        self.timestamp = datetime.datetime.now().strftime("%Y/%m/%d")

    def asignar_id(self, nota_id):
        self.id = nota_id

    def casa(self, filtro):
        return filtro.lower() in self.memo.lower() or filtro.lower() in self.etiqueta.lower()


class Cuaderno:
    def __init__(self):
        self.notas = []

    def agregarNota(self, nota):
        nota = Nota(nota.memo, nota.etiqueta)
        nota.asignar_id(len(self.notas))
        self.notas.append(nota)

    def modifiqueMemo(self, notaId, memo):
        for nota in self.notas:
            if nota.id == notaId:
                nota.memo = memo
                break

    def modifiqueEtiqueta(self, notaId, etiqueta):
        for nota in self.notas:
            if nota.id == notaId:
                nota.etiqueta = etiqueta
                break

    def encuentreNota(self, id):
        for nota in self.notas:
            if nota.id == id:
                return nota
        print("Nota not found.")
        return None

    def imprimaNotas(self):
        for nota in self.notas:
            print(f"ID: {nota.id}, Memo: {nota.memo}, Etiqueta: {nota.etiqueta}, Created: {nota.timestamp}")

    def busque(self, filtro):
        resultados = []
        for nota in self.notas:
            if nota.casa(filtro):
                resultados.append(nota)
        if len(resultados) > 0:  # Verifica si hay resultados antes de retornar
            return resultados
        print("Nota not found.")
        return []  # Devuelve una lista vacía en lugar de None cuando no se encuentran resultados


