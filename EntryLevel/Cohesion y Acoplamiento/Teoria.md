# Introducción
El acoplamiento y la cohesión juegan un rol central en el diseño de software.
El diseño minimiza los costos. Los costos se generan en la siguiente cadena:

Costos del software -> Costos de mantimiento -> Costos del cambio

(La flecha (->) se puede leer como "generan")

Un diseño de software efectivo minimiza la probabilidad de que se propaguen los cambios.
Los cambios que involucran a un único elemento son menos costosos y más predecibles
que los cambios a un elemento que requieren cambiar dos más.

## Acoplamiento
El acoplamiento involucra el cambio en un módulo debido al cambio en otro. Por ejemplo,
el módulo A está acoplado con el módulo B, cuando al cambiar el módulo B tiene
que cambiar el módulo A. El acoplamiento entre los elementos es un conductor de cambios.

El acoplamiento es una propiedad estática: dos elementos están temporalmente acoplados si,
por ejemplo, la secuencia invocante entre ellos está restringida. Las propiedades
estáticas son solo costo potencial: si no ocurre ningún evento que dispare el acoplamiento,
el costo nunca ocurre.

El concepto fundamental es que los elementos en un diseño no deben estar acoplados
con respecto a los cambios que realmente van a ocurrir. Esto mantiene contenido al
costo de los cambios.

Cuando dos unidades de software son absolutamente independientes (cada una puede
hacer su trabajo sin contar para nada con la otra), encontramos el grado más bajo
de acoplamiento, y decimos que ambas unidades están totalmente desacopladas.

Existen diferentes tipos de acoplamiento entre unidades de software:

- Unidades completamente desacopladas
- Acoplamiento normal (una unidad necesita del trabajo que hace la otra)
- Acoplamiento de datos (dos o más unidades de software dependen de los mismos datos)
- Acoplamiento temporal (dependendencia de ejecución de algo previo)
- Acoplamiento de control (ejecución según el valor de un parámetro)
- Acoplamiento global (dependencia de una variable global)

La lista anterior va de menor a mayor acoplamiento.

## Cohesión
La cohesión tiene que ver con la forma en la que agrupamos unidades de software
en una unidad mayor. Por ejemplo, la forma en la que agrupamos funciones en una
librería, o la forma en la que agrupamos métodos en una clase, o la forma en la
que agrupamos clases en una librería, etc.

Se suele decir que cuanto más cohesionados estén los elementos agrupados, mejor.
El criterio por el cual se agrupan es la cohesión.

Existen diferentes niveles de cohesión:

- Cohesión funcional (todas las unidades de sw contribuyen a realizar el mismo fin)
- Cohesión secuencial (los resultado de unas unidades de sw se utilizan para continuar trabajando)
- Cohesión de datos (las unidades trabajan sobre los mismos datos)
- Cohesión lógica (las unidades realizan trabajo en una misma categoía pero no tienen relación entre ellas)
- Cohesión temporal (se las une simplemente por tener que ejecutarse al mismo momento)
- Cohesión casual (sin criterio alguno para agrupar las unidades)

La lista anterior va de mayor a menor cohesión.

## Conclusión
Tener unos buenos criterios para agrupar unidades de software (alta cohesión),
y mantener esas unidades lo más independientes posible (bajo acoplamiento)
garantiza la modularidad, facilitando la reutilización del software y gran parte
de las tareas del desarrollo del software.

- [1] [Acoplamiento y cohesión](https://dosideas.com/noticias/java/502-acoplamiento-y-cohesion)
- [2] [Acoplamiento y cohesión. Taxonomía](http://latecladeescape.com/h/2015/07/acoplamiento-y-cohesion<Paste>)
