# Liskov substitution principle
Barbara Liskov estableció:

_Si q(x) es una propiedad probable sobre los objetos x de un tipo T. Entonces q(y)
debería ser probable para los objetos de tipo S, tal que S es un subtipo de T._

Y Robert C. Martin dijo:

_Los subtipos deben poder ser sustituibles por sus clases base._

## ES UN/UNA
Por lo general, en la POO se dice que una clase debería ser subclase de otra si
cumple con la restricción "ES UN/UNA". Por ejemplo:

Un Auto "ES UN" Vehículo.

Bajo esa premisa, un Auto debería ser una subclase de un Vehículo.
Esta regla puede llevar a problemas en la práctica. Por ejemplo:

Un Cuadrado "ES UN" Rectángulo.

¿Es correcto afirmar que un Cuadrado es un Rectángulo?_

Existen operaciones en Rectángulo que no coinciden con las del Cuadrado.
`setWidth` y `setHeight` se comportande forma diferente en la clase Cuadrado y
Rectángulo. Por lo tanto, no podría substituirse Cuadrado por Rectángulo en
alguna función.

## La validez no es intrínseca
Un objeto visto aisladamente no puede ser evaluado significativamente. La validez
de un modelo solo puede ser expresada en términos de sus clientes.

En el caso del Cuadrado y el Rectángulo, se puede notar que aisladamente ambos
se comportan de forma esperada. Sin embargo, al ser analizados al mismo tiempo
que el uno no debería ser subclase del otro, ya que el **comportamiento** de ambos
es diferente y aquí nos referimos a **comportamiento público**, no tanto el privado.
Ya que ocurrirán problemas en los clientes de esas clases.
