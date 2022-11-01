import re
def Buscar_libro_por_ISBN_o_título(input_data: str):
    x = re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", input_data)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")
Buscar_libro_por_ISBN_o_título('978-1-56619-909-4')