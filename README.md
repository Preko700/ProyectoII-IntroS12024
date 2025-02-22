# ProyectoII-IntroS1GR42024
Proyecto II de Introduccion a la Programacion del TEC del 2024 Grupo 4 a cargo del profesor Jason Leiton conformado por Adrian Monge Mairena y Jimena Castillo Campos
# Proyecto de Píxel Art en Python

## 1. Planificación y Diseño

### a. Requisitos y Funcionalidades
- **Funcionalidades específicas**: Detalla las herramientas de dibujo, opciones de colores, efectos, etc.
- **Requisitos de la interfaz gráfica**: Define botones, menús, área de dibujo, etc.

### b. Estructura del Proyecto
- **Módulos claros**: Divide el proyecto en interfaz gráfica, manejo de imágenes, algoritmos de manipulación de píxeles, etc.

## 2. Configuración del Entorno
- **Instalación de Python y bibliotecas necesarias**: Asegúrate de tener Python, tkinter para la interfaz gráfica y numpy para el manejo eficiente de matrices.

## 3. Desarrollo de la Interfaz Gráfica
- **Diseño de la Interfaz**: Usa tkinter para crear una ventana principal con una cuadrícula para el dibujo de píxeles.
- **Herramientas de Dibujo**: Añade botones y herramientas para seleccionar colores, dibujar, borrar, guardar, cargar, etc.

## 4. Representación y Manipulación de Imágenes

### a. Uso de Matrices
- **Representación de la imagen**: Representa la imagen de Píxel Art como una matriz de colores. Cada celda de la matriz puede almacenar un valor de color.
- **Manipulación eficiente**: Usa numpy para crear y manipular estas matrices de forma eficiente.

### b. Algoritmos de Manipulación
- **Funciones de manipulación**: Implementa funciones para cambiar colores, escalar y rotar imágenes. Estas funciones deben operar sobre la matriz de colores.
- **Ejemplo**: Para cambiar un color, recorre la matriz y reemplaza los valores correspondientes.

## 5. Programación Orientada a Objetos (POO)

### Clases Principales:
- **PixelArtApp**: Maneja la lógica de la aplicación.
- **Canvas**: Representa el área de dibujo, maneja la matriz de píxeles.
- **Tools**: Contiene herramientas para dibujar y editar.

### Modularización:
- **Responsabilidades claras**: Asegúrate de que cada clase tenga responsabilidades claras y bien definidas.

## 6. Implementación de Funcionalidades Avanzadas
- **Cambio de Color**: Implementa una función para cambiar el color de un píxel específico o de un área.
- **Escalado**: Usa algoritmos para aumentar o disminuir el tamaño de la imagen manteniendo la proporción.
- **Rotación**: Implementa rotación de la imagen, utilizando técnicas de transformación de matrices.

## 7. Pruebas y Depuración
- **Pruebas exhaustivas**: Realiza pruebas exhaustivas para asegurar que cada funcionalidad trabaja correctamente.
- **Depuración**: Depura cualquier problema que encuentres durante el desarrollo.

## 8. Documentación y Presentación
- **Documentación del código**: Documenta tu código y proporciona instrucciones claras para el uso del programa.
- **Presentación del proyecto**: Prepara una presentación del proyecto, destacando sus características y funcionalidades.