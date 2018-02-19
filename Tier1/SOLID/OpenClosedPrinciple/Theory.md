# Open/Closed principle
## Definición
Las unidades de software deberían ser abiertas para la extensión, pero cerradas
para modificación.

Básicamente, se refiere a que las unidades de software deberían estar escritas
de tal foma que nueva funcionalidad agregada debería mantener el código base
sin modificación y en su lugar agregar nuevo código que será utilizado.

No está claro aun (._-. )

Los módulos que conforman el principio de abierto/cerrado cumplen con:

1. Son "Abiertos para la extensión"
Lo que significa que el comportamiento del módulo puede ser **extendido**. Podemos
hacer que el módulo se comporte en una forma nueva y diferente como los requisitos
de la aplicación cambian, o para cumplir con las necesidades de nuevas aplicaciones.

2. Son "Cerrados para la modificación"
El código no se puede cambiar. Nadie debería estar permitido de cambiar el código base.
