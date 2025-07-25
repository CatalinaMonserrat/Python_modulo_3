🐍 Python — Módulo 3 del Bootcamp

Este repositorio contiene los ejercicios realizados durante el Módulo 3 del bootcamp de desarrollo con Python. En esta etapa del aprendizaje se trabaja con estructuras intermedias, condicionales y creación de funciones propias, fortaleciendo la lógica y resolución de problemas mediante programación.

---

## Objetivos del Módulo
- Aplicar estructuras condicionales (`if`, `elif`, `else`) para tomar decisiones.
- Implementar estructuras de datos como listas y diccionarios.
- Desarrollar funciones definidas por el usuario.
- Utilizar buenas prácticas para organizar y comentar código.

---

## Estructura del Repositorio
Python_modulo_3/
├── Funciones_intermedias_1/ ← Ejercicios prácticos de funciones
├── Estructuras_intermedias/ ← Ejercicios con estructuras como listas y diccionarios
├── Ejercicio_condicionales/ ← Prácticas con condicionales
├── Print_HolaMundo/ ← Primer script de prueba
└── README.md

---

## 🛠 Tecnologías utilizadas
- Python
- Git y GitHub

---

## Ejemplo de código

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingresa un número: "))
if es_par(numero):
    print("Es par.")
else:
    print("Es impar.")

## Contenidos abordados
- Estructuras condicionales (if, else, elif)
- Funciones definidas por el usuario (def)
- Ciclos y estructuras de repetición (introducción)
- Listas y diccionarios (estructuras intermedias)
- Inputs desde consola
- Pruebas simples por consola


## Cómo ejecutar los archivos
1. Clona este repositorio:
   ```bash
   git clone https://github.com/CatalinaMonserrat/Python_modulo_3.git
2. Abre la carpeta en tu editor favorito.
3. Ejecuta los archivos .py en la terminal con: python ruta/del/archivo.py

Autor
Catalina Monserrat
Bootcamp Desarrollo Web con Python/Django
GitHub: @CatalinaMonserrat