# Clases
Una clase es una plantilla para _crear_ objetos (una estructura de datos particual),
a la cual se le proporciona valores iniciales para el estado (variables miembro
o atributos), e implementaciones de comportamiento (funciones miembro o métodos).

Por ejemplo:

```
Clase Caballo:
  Atributos:
    Nombre
    Edad
    Tamaño
    Peso
  Métodos:
    relinchar()
```

# Objetos
Un objeto es una instancia de una clase. Una ejemplificación de la plantilla.

Por ejemplo:

```
Caballo rocinante:
  Atributos:
    Nombre="Rocinante"
    Edad=23
    Tamaño=1.5m
    Peso=200kg
  Métodos:
    relinchar(){
      Imprimir "¡Rocinante está relinchando!"
    }
```

# Constructor
El constructor es un método que incializa un objeto. En otras palabras, es el
método que se ejecuta cuando se instancia por primera vez un objeto.

# Interfaz
Una interfaz es un tipo de abstracción que no contiene datos o código, pero sí
define comportamiento como firmas de métodos. Una clase puede implementar los
métodos definidos en la interfaz formando un subtipo de esa interfaz. Además una
clase puede implementar varias interfaces y llegar a ser de diferentes subtipos.

Por ejemplo:

```
interfaz Stack:
  Métodos:
    pop()
    push(val)

Lista implementa Stack:
  pop(){
    ...
  }
  push(val){
    ...
  }
```

# Clase abstracta
PENDING
