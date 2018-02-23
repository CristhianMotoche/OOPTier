# La Ley de Demeter
Es una guía de diseño para el desarrollo de software, aplicado principalmente en
la POO. La ley se puede resumir en los siguientes enuncionados:

- Cada unidad debe tener un limitado conocimiento sobre otras unidades y solo
conocer aquellas unidades estrechamente relacionadas a la unidad actual.
- Cada unidad debe hablar solo a sus amigos y no hablar con extraños.
- Solo hablar con sus amigos inmediatos

## La Ley de Demeter para Funciones/Métodos
Un método `m` de un objecto `obj` solo debería ser capaz de invocar a los
siguientes métodos:

- Aquellos que son propios de `obj`
- De los parámetros de `m`
- Cualquier objeto creado/instanciado dentro de `m`
- Los componentes directos de `obj`
- Una variable global accedidad por `obj` y en el alcance de `m`

Este caso puede entenderse simplemente como _utiliza solo un punto_
Es decir, que el código como: `a.b.m()` rompe la ley de Demeter, pero `a.m()` no
lo hace.

La ley es útil ya que disminuye el acoplamiento y fortalece el encapsulamiento.

# Anti-patrón
Seguir esta ley puede llevar al anti-patrón de los _Métodos Privados en Capa_.
Que consiste en colocar las llamadas a los métodos que incumplen con la ley de demeter
en un método privado.
