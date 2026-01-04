class Solution:
    def margeTwoSorted(self, lista1, lista2) -> None:
        resultado = []
        lista_1_index = 0
        lista_2_index = 0

        # Recorremos ambas listas y comparamos los elementos
        while lista_1_index < len(lista1) and lista_2_index < len(lista2):
            if lista1[lista_1_index] < lista2[lista_2_index]:
                resultado.append(lista1[lista_1_index])
                lista_1_index += 1
            else:
                resultado.append(lista2[lista_2_index])
                lista_2_index += 1

            # agregamos elementos restantes de la lista 1
            resultado.extend(lista1[lista_1_index:])
            # agregamos elementos restantes de la lista 2
            resultado.extend(lista2[lista_2_index:])
        return resultado
    
Sol = Solution()
lista1 = [1,2,4]
lista2 = [1,3,4]
print(Sol.margeTwoSorted(lista1, lista2))
     
