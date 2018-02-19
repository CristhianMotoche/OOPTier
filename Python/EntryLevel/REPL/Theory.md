# REPL
Read, Eval, Print, Loop

## REPL de python
El REPL por defecto de Python permite ejecutar cualquier sentencia de Python.

```
>>> x = 42
>>> print(x)
>>>
>> class MyClass(object):
...     def __init__(self):
...             pass
...
>>> mc = MyClass()
```

Además, proporciona algunos comandos extra, por ejemplo:

```
>>> help(mc)
Help on MyClass in module __main__ object:

class MyClass(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
...

>>>
>>> dir()
['MyClass', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'n', 'x']
```

- **help** permite consultar sobre variables, funciones del REPL y demás. Proporciona
información conveniente.
- **dir** retorna una lista de strings con los nombres en el alcance actual.
