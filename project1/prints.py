from cuaderno import Cuaderno, Nota
if __name__ == '__main__':
    cuaderno = Cuaderno()
    cuaderno.agregarNota(Nota('Hello World', ''))
    cuaderno.agregarNota(Nota('Hello World again', ''))

    print('Printing all addresses of notes in the notebook:')
    for nota in cuaderno.notas:
        print(nota)

    print('\nnotebook.notas[0].id: {}'.format(cuaderno.notas[0].id))
    print('notebook.notas[1].id: {}'.format(cuaderno.notas[1].id))
    print('notebook.notas[0].memo: {}'.format(cuaderno.notas[0].memo))

    print('\nExecuting cuaderno.busque(\'Hello\'):')
    print('Printing all addresses of notes in the notebook with the string \'Hello\' in memo or etiqueta:')
    resultados = cuaderno.busque('Hello')
    for nota1 in resultados:
        print(nota1)

    print("\nExecuting cuaderno.modifiqueMemo(1, 'Hi World')")
    cuaderno.modifiqueMemo(1, 'Hi World')
    print('notebook.notas[1].memo: {}'.format(cuaderno.notas[1].memo))

    print("\nExecuting cuaderno.agregarNota('With tag', 'Peter')")
    cuaderno.agregarNota(Nota('With tag', 'Peter'))
    print('Printing all addresses of notes in the notebook:')
    for nota in cuaderno.notas:
        print(nota)

    print("\nExecuting vars(cuaderno.notas[0])")
    print(vars(cuaderno.notas[0]))

    print("\nExecuting print(cuaderno.notas[2].etiqueta)")
    print(cuaderno.notas[2].etiqueta)

    print("\nExecuting cuaderno.encuentreNota(3)")
    nota1 = cuaderno.encuentreNota(3)
    print(nota1)

    print("\nExecuting cuaderno.encuentreNota(2)")
    nota2 = cuaderno.encuentreNota(2)
    print(vars(nota2))

    print("\nExecuting cuaderno.modifiqueEtiqueta(2, 'John')")
    cuaderno.modifiqueEtiqueta(2, 'John')
    print("Executing print(cuaderno.notas[2].etiqueta)")
    print(cuaderno.notas[2].etiqueta)

    print('\nPrinting all addresses of notes in the notebook:')
    for nota in cuaderno.notas:
        print(nota)

    print("\nPrinting all notes iterating over the notebook and using vars() for each note:")
    for nota in cuaderno.notas:
        print(vars(nota))

    print('\nPrinting all notes using imprimaNotas() method:')
    cuaderno.imprimaNotas()
