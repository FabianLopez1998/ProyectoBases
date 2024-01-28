
import re
class validar:

    def validarCedulaRuc(self, cedula):
        validacionCedula = lambda id: sum([int(id[i]) if i%2 != 0 else int(id[i])*2 if int(id[i])*2<9 else int(id[i])*2-9 for i in range(10)])%10 ==0
        #Validar ruc
        verificador = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
        verificadorPublicos = [3, 2, 7, 6, 5, 4, 3, 2, 1]
        validacionRucSinCedula= lambda id: sum([int(id[i])*verificador[i] for i in range(10)])%11 ==0 and len(id)==13
        validacionRucPublicos= lambda id: sum([int(id[i])*verificadorPublicos[i] for i in range(9)])%11 ==0 and len(id)==13

        if cedula.isdigit and len(cedula)>=10:
            if len(cedula)==10: return validacionCedula(cedula)
            elif int(cedula[2])>=0 and int(cedula[2])<=5 and len(cedula)==13: return validacionCedula(cedula)
            elif int(cedula[2])==6: return validacionRucPublicos(cedula)
            elif int(cedula[2])==9 : return validacionRucSinCedula(cedula)      ##Persona juridica y extranjeros sin cedula de identidad
            else: return False
        else: return False


    def es_correo_valido(self, correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, correo) is not None

    def validarVacios(self, cedula, nombre, direccion, telefono, correo):
        if cedula=="" or nombre ==""  or direccion =="" or telefono =="" or correo=="":
            return False
        else:
            return True

    def ValidaSoloLetras(self, texto):
        for i in range(len(texto)):
            if texto[i].isdigit() == True:
                return False
        return True

    def ValidaPrecio(self,precio):
        for i in range(len(precio)):
            if precio[i].isdigit()!=True and precio[i] != ".":
                return False
        precio.isdigit()
        return True

    def ValidaISBN(self, isbn):
        if isbn.isdigit() and len(isbn)==13: return True
        else: return False