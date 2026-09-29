# Simulador_Dados
# 🎲 Simulador de Dados

Este repositorio contiene el proyecto **Simulador de Dados**, desarrollado en Python para practicar los contenidos de programación y gestión de proyectos de la asignatura.

El programa permite seleccionar diferentes tipos de dados, realizar lanzamientos con una animación visual y consultar los resultados obtenidos.

## 👤 Autor

**Nathalia piñera Molina**

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje utilizado para desarrollar la lógica del programa.
- **Rich:** librería utilizada para mejorar la presentación visual en consola, mostrar paneles, colores y animaciones.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## 🎯 Funcionalidades

1. **Menú principal:** permite acceder al lanzamiento de dados, a la opción de analítica y salir del programa.
2. **Selección de dados:** permite elegir entre D4, D6, D8, D10, D12 y D20.
3. **Validación de datos:** comprueba que la cantidad introducida sea un número entero positivo.
4. **Animación de lanzamiento:** muestra una animación visual del dado utilizando la librería Rich.
5. **Resultados por colores:**
   - 🔴 Rojo: resultado mínimo (1).
   - 🟢 Verde: resultado máximo del dado.
   - 🟡 Amarillo: cualquier otro resultado.
6. **Cálculo de resultados:** muestra el total y el promedio de los dados lanzados.

## 📂 Estructura del proyecto

```text
Simulador_Dados/
│
├── .venv/                 # Entorno virtual de Python
├── Simulator.py           # Código principal del programa
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
└── .gitignore             # Archivos excluidos del control de versiones
