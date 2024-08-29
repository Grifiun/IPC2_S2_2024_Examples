### 1. **Nombres de Clases**
   - **Recomendación:** En Python, se recomienda utilizar la convención **PascalCase** (también conocida como **CapWords**), donde cada palabra empieza con una letra mayúscula y no se utilizan guiones bajos.
   - **Ejemplo:**
     ```python
     class MiClaseEjemplo:
         pass
     
     class CalculadoraAvanzada:
         pass
     ```

### 2. **Nombres de Variables y Funciones**
   - **Recomendación:** Para las variables y funciones en Python, se utiliza la convención **snake_case**, que consiste en escribir todo en minúsculas y separar las palabras con guiones bajos.
   - **Ejemplo:**
     ```python
     def calcular_suma(numero1, numero2):
         resultado = numero1 + numero2
         return resultado
     
     nombre_usuario = "Juan"
     ```

### 3. **Constantes**
   - **Recomendación:** Las constantes se nombran en **ALL_CAPS**, utilizando mayúsculas y separando las palabras con guiones bajos.
   - **Ejemplo:**
     ```python
     PI = 3.14159
     MAX_INTENTOS = 5
     ```

### 4. **Módulos y Paquetes**
   - **Recomendación:** Los nombres de los archivos de módulos y paquetes deben seguir la convención **snake_case**.
   - **Ejemplo:**
     ```python
     # Nombre del archivo: mi_modulo.py
     # Nombre del paquete: mi_paquete
     
     # Contenido de mi_modulo.py
     def funcion_modulo():
         pass
     ```

### 5. **Métodos Privados y Variables Internas**
   - **Recomendación:** Para indicar que un método o variable es interno o privado dentro de una clase, se utiliza un guion bajo (`_`) al inicio del nombre.
   - **Ejemplo:**
     ```python
     class Ejemplo:
         def __init__(self, valor):
             self._valor_interno = valor
         
         def _metodo_privado(self):
             print("Este es un método privado")
     ```

### 6. **Métodos y Variables Fuertemente Privados**
   - **Recomendación:** Si deseas evitar conflictos de nombres en subclases, puedes utilizar dos guiones bajos (`__`) al inicio del nombre para activar el **name mangling**.
   - **Ejemplo:**
     ```python
     class Ejemplo:
         def __init__(self, valor):
             self.__valor_fuerte = valor
         
         def __metodo_fuerte_privado(self):
             print("Este es un método fuertemente privado")
     ```

### 7. **Nombres de Variables Globales en Módulos**
   - **Recomendación:** Aunque se recomienda minimizar el uso de variables globales, cuando se usan, es preferible nombrarlas en **ALL_CAPS**.
   - **Ejemplo:**
     ```python
     GLOBAL_VAR = 42
     
     def usar_global():
         global GLOBAL_VAR
         print(GLOBAL_VAR)
     ```

---

Este formato resume las convenciones de Python y proporciona ejemplos claros de cada una, permitiendo que las buenas prácticas sean fácilmente comprensibles y aplicables.