#ejercicio para consultar tu edad

#clase solution
class Solution:
    #funcion donde espera como argumentos age_birthday y age_now para hacer la resta
    def edad(self, age_birthday: int, age_now: int):
        age = age_now - age_birthday
        return f"Tu edad es {age} años."

solution = Solution()
#pide la fecha a los usuarios
age_now = int(input("tu age de nacimiento: "))
age_birthday = int(input("ingresa la fecha actual: "))

#muestra el resultado
print(solution.edad(age_now, age_birthday))
        