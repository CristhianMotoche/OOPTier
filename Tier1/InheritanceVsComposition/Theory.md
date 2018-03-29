# Herencia
Hacer que una clase herede (obtenga) los atributos y métodos de una clase base.
Por lo general, sigue la convención `ES UN`, por ejemplo: `Carro ES UN Vehiculo`.

```python
class Vehiculo(object):
  pass

class Carro(Vehiculo)
  pass
```

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
