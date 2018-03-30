# Herencia
Hacer que una clase herede (obtenga) los atributos y métodos de una clase base.
Por lo general, sigue la convención `ES UN`, por ejemplo: `Carro ES UN Vehiculo`.

```python
class Vehiculo(object):
  pass

class Carro(Vehiculo)
  pass
```

La herencia tiene dos propósitos: semántica y mecánica.

### Semántica:
Captura el significado en una taxonomía. La clase derivada se acopla a la clase base
tanto en atributos y métodos como en significado.

### Mecánica:
Atributos y métodos de una clase base son heredados por una clase derivada. La clase
derivada puede extender sus atributos y comportamientos.


La reutilización de código no es el principal propósito de la herencia.

## Advantages

* Las clases derivadas adquiren el comportamiento (o pueden extenderlo) de su clase
base.

## Disadvantages

* Sobrescritura de atributos/métodos.

# Composition
Componer a una clase de otras (agregrando instancias de ellas como atributos).
Por lo general, sigue la convención `TIENE UN`, por ejemplo: `UN Carro TIENE LLANTAS`.

```python
class Carro(object):
  llantas = Llantas()

class Llantas(object)
  pass
```

## Advantages

* No existe colisiones de nombres. Cada atributo que es un objeto compuesto tiene
su propio namespace.
* No crea una relación jerarquica.
* La clase que compone los elementos puede cambiar sin afectar a sus clases compuestas.

## Disadvantages
