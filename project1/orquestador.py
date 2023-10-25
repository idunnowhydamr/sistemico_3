#%%
from cuaderno import Cuaderno, Nota
#%%
# Create a Cuaderno instance
mi_cuaderno = Cuaderno()
#%%
# Add some notes
nota1 = Nota("Buy groceries", "Shopping")
nota2 = Nota("Call John", "Work")
nota3 = Nota("Pick up dry cleaning", "Errands")
#%%
mi_cuaderno.agregarNota(nota1)
mi_cuaderno.agregarNota(nota2)
mi_cuaderno.agregarNota(nota3)
#%%
# Print all notes
mi_cuaderno.imprimaNotas()
#%%
# Search for notes containing "groceries"
resultados = mi_cuaderno.busque("groceries")
for nota in resultados:
    print(f"Matching Note - Memo: {nota.memo}, Etiqueta: {nota.etiqueta}")
#%%
# Find a note by ID
found_nota = mi_cuaderno.encuentreNota(1)  # Search for the note with ID 1
if found_nota:
    print(f"Found Note - Memo: {found_nota.memo}, Etiqueta: {found_nota.etiqueta}")
#%%

mi_cuaderno.modifiqueMemo(1, "hi world")
mi_cuaderno.modifiqueEtiqueta(2, "Juan")
mi_cuaderno.imprimaNotas()

