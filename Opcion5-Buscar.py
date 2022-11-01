import re
def Buscar_libro_por_ISBN_o_título(input_user: str, data):
    ISBN = re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", input_user)

    titulo_list = input_user.split(" ")
        
    titulo = str.find("")

    if ISBN | :
        print("YES! We have a match!")
    else:
        print("No match")
Buscar_libro_por_ISBN_o_título('978-1-56619-909-4')