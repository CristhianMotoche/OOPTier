# Single Responsability Principle
## Definición
Una unidad de software solo debe tener una única razón para cambiar.

## ¿Por qué?
Si existen dos razones por las cuales una unidad de software vaya a cambiar, es
posible que dos o más personas trabajen en el mismo código por dos razones diferentes.
Solucionar conflictos posteriormente podría ser fastidioso.

## Audiencia / Actor o Role
Una responsabilidad es una familia de funciones que sirve a un actor particular.

## Fuente de cambio
Los actores pueden llegar a ser una fuente de cambio para la familia de funciones
que los sirven. A medida que sus necesidades cambian, esa familia específica de
funciones también debe cambiar para acomodarse a sus necesidades.


## Ejemplo
El ejemplo del libro obtenido del [blogpost sobre el SRP](https://code.tutsplus.com/tutorials/solid-part-1-the-single-responsibility-principle--net-36074)
muestra que es incorrecto que el libro tenga la responsabilidad de imprimir el
contenido de la página actual.

```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.authr = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def turn_page(self):
        self.page += 1

    def print_current_page(self):
        print("The content of the current page")
        print(self.page)
```

Razones:
- Existen dos razones por las cuales podría cambiar esta clase:
  - Aumentar atributos a la clase libro (e.g. la editorial).
  - Cambiar la forma en la cual se imprime el contenido de la página actual.
- El método `print_current_page` está desplegando el contenido y número de la
página actual. Si posteriormente se desea que se imprima también el nombre del
autor, existirá una razón de cambio para la clase `Book`. Si además también se
desea que en lugar de imprimir en consola se imprima en formato HTML, habrá otra
razón por la cual cambiar.

Mezclas la lógica de negocio con la presentación va encontra del SRP.
