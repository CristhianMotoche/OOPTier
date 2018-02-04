# Encapsulation

El encapsulamiento tiene 2 objetivos importantes relacionados con modularidad
y abstracción:

## Esconder complejidad
En ocasiones no es importante conocer como funcionan internamente ciertos componentes
y simplemente abstraer su complejidad para utilizarlos sin preocuparnos por detalles
internos. Solamente necesitamos saber:

- Su funcionamiento en rasgos generales
- Cómo utilizarlo
- Cómo interactuar con él

Y como se menciona en [1], las partes visibles de nuestros módulos/clases constituyen
su _interfaz pública_, y esto está expuesto al mundo exterior, el resto debe estar
oculto a simple vista.

## Ocultar la fuente de cambio
El encapsulamiento permite que los cambios se realicen de forma segura sin afectar
la interfaz pública.

Interesting links:
- [1] [Why encapsulation matters?](https://dzone.com/articles/why-encapsulation-matters)
