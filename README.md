# fundamentos_python
## Seccion #1
Funcion print("")
Primeramente vamos a crear el codigo para darle salida a la ejecucion del comando "print("!Hola, Mundo")" para al momento de hacer su ejecucion de salida a:
```bash 
py lab1.py
!Hola, Mundo
```

## Laboratorio 1
-1 Primeramente se utiliza el tipico "print("!Hola, Mundo!")" comun y corriente para luego de ejecutarlo el comando de salida a:
```bash
!Hola, Mundo!
```
-2 Ahora lo que haremos sera una modificacion para que a la funcion "print()" haga una salida diferente de esta manera print("Juan Jose Giraldo") , ahora que imprima nuestro nombre: 
```bash
Juan Jose Giraldo 
```
en la terminal se vera el proceso

-3 Ahora vamos a quitarle las comillas doble a nuestro codigo para poder ver la reaccion que llega a tener python con el control de errores "print(Juan Jose Giraldo)" para dar salida a:

```bash
File "C:\Users\uiehc\OneDrive\Documentos\fundamentos_python\src\seccion1\lab1.py", line 2
    print(Juan Jose Giraldo)
          ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
``` 
este error es de sintaxis, la estructura de la linea no es valida en python esto siendo ya que "print" es una funcion y necesita parentesis alrededor de su argumentos


-4 Ahora el proposito sera eliminar los parentesis y volver a poner las comillas dobles "print "Juan Jose Giraldo" y al momento de ejecutar el codigo nuevamente, el error que saldra es: 
```bash
File "C:\Users\uiehc\OneDrive\Documentos\fundamentos_python\src\seccion1\lab1.py", line 3
    print "Juan Jose Giraldo"
    ^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```
este error significa que Python nos dice que los parantesis alrededor de los argumentos de print siendo este error ya que se usa python 2 (una version antigua)

-5 Ahora lo que haremos sera una prueba general agregando comillas simples, usando multiples funciones "print" en la misma linea y luego en diferentes lineas para ver si su salida es excitosa
```bash
File "C:\Users\uiehc\OneDrive\Documentos\fundamentos_python\src\seccion1\lab1.py", line 2
    print(´Juan Jose Giraldo´)
          ^
SyntaxError: invalid character '´' (U+00B4)
```
Con esto podemos ver que no se ejecuto de manera correcta ya que tenemos un error tipo SyntaxError significando esto que se encontro un caracter que no es valido dentro de la sintaxis del lenguaje ya si se arregla dicho error 

```bash
File "C:\Users\uiehc\OneDrive\Documentos\fundamentos_python\src\seccion1\lab1.py", line 3
    print("Monsalve") print ("doble funcion en 1 linea")
                      ^^^^^
SyntaxError: invalid syntax. Did you mean 'in'?
```
Ahora podemos ver otro error tipo SyntaxError lo que significa que Python no entiende la estructura de la linea porque hay dos intrucciones seguidas sin una separacion valida, el error es: 
```bash 
print("Monsalve") print ("doble funcion en 1 linea")
```
Una vez arreglado el comando salida sera:

```bash
!Hola, Mundo
Juan Jose Giraldo
Monsalve
doble funcion en 1 linea
diferente linea
```
## Laboratorio 2
- Ahora aca vamos a trabajar con modificaciones a la linea del codigo con el editor, siendo de esta manera que usaremos las palabras claves reservadas sep y end, para que se obtenga la salida esperada, se emeplea dos funciones print() con el editor, dando la creacion y a la solucion de este laboratorio a algo asi 
```bash
print("Programming", "Essentials", "in",  sep="***", end="...Python")
```
```bash
Programming***Essentials***in...Python
```

## Laboratorio 3

-1 Primeramente vamos a minimizar el numero de invocaciones de la funcion "print ()" intertando varios "\n" en las cadenas de esta manera:
```bash 
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
```
dando salida a:
```bash
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****
  ```

-2 Ahora vamos hacer que la flecha sea el doble de grande (pero vamos a mantener las proporciones) utilizando el mismo metodo de "\n"
```bash
print("    *\n")
print("   * *\n")
print("  *   *\n")
print(" *     *\n")
print("***   ***\n")
print("  *   *\n")
print("  *   *\n")
print("  *****\n")
```
con la salida de:
```bash
    *

   * *

  *   *

 *     *

***   ***

  *   *

  *   *

  *****
```
-3 ahora el proposito sera duplicar la flecha, colocando ambas flechas una al lado de la otra utilizando un atajo el cual seria (string *2) ya que asi el produciria "stringstring" dando como resultado al comando deseado:
```bash
print("    *     " *2)
print("   * *    " *2)
print("  *   *   " *2)
print(" *     *  " *2)
print("***   *** " *2)
print("  *   *   " *2)
print("  *   *   " *2)
print("  *****   "*2)
```
ahora el mensaje salida es:
```bash
    *         *     
   * *       * *    
  *   *     *   *   
 *     *   *     *  
***   *** ***   *** 
  *   *     *   *   
  *   *     *   *   
  *****     *****   
```

-4 en este tendremos un error de SyntaxError en el cual se esta usando el print como si fuera una declaracion (estilo Python 2, una version antigua) y se especifica el motivo del error "print "   *  " *2"

```bash
print "    *     " *2
print("   * *    " *2)
print("  *   *   " *2)
print(" *     *  " *2)
print("***   *** " *2)
print("  *   *   " *2)
print("  *   *   " *2)
print("  *****   "*2)
```
dando salida a:
```bash
File "c:\Users\uiehc\OneDrive\Documentos\fundamentos_python\src\seccion1\lab3.py", line 23
    print "    *     " *2
    ^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

-5 Ahora se hara otro trabajo de error (SyntaxError) en el cual el "Print" no se esta definiendo de manera correcta, dando asi salida a "print" 
```bash
Print("    *     " *2)
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

-6 Ahora se trabaja un error de igual manera de sintaxis, siendo ahora que el error que estamos agregando un string indeterminado (') dando salida este error:
```bash
"Print("    *     ' *2)"
SyntaxError: unterminated string literal (detected at line 23)
```
## Seccion 2

## Laboratorio 1

-1 Aca vamos a escribir un fragmento de codigo de una linea utilizando una funcion "print" asi como los caracteres de nuevalinea y de escape 

```bash
print ("\"Estoy\"\"\"aprendiendo\"\"\"\"\"Python\"\"\"")
Dando salida a:
Users/uiehc/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/uiehc/OneDrive/Documentos/fundamentos_python/src/seccion2/lab1.py
"Estoy"""aprendiendo"""""Python"""
```

## Seccion 4

## Laboratorio 1


## 1
- Primeramente se crean las variables "john,mary y adam, a las cuales se les va a asignar un valor el cual corresponde al texto
```bash
john = 10
adam = 6
mary = 5
```


## 2
- Ahora lo que se hizo fue que una vez los numeros de los variables ya esten definidos, los imprima en una sola linea y que los separe cada una de ellas con una coma
```bash
print(john, mary, adam, sep=", ")
```


## 3
- Ahora se va a crear una variable que se llame "total_apples" y la funcion de dcha es que debe igualas a la suma de las tres variables ya creadas (john,adam y mary)
```bash
total_apples = john + adam + mary
```


## 4
-Para luego hacer que imprima el valor almacenado que tenemos en "total_apples" en la consola
```bash 
print("Número total de manzanas:", total_apples)
```


## 5
-Principalmente lo que se hizo fue crear 4 variables mas, las cuales se trabajaron precio, cantidad de estudiantes y manzanas, se hicieron 3 operaciones aritmeticas con "resta-division entera y multiplicacion" con su correcto funcionamiento y su salida en la terminal totalmente correcta
```bash
print("\n--- Experimentar el codigo ---")
manzanas_restantes = total_apples - 3
print("Si john se roba 3, estarian quedando:", manzanas_restantes)

total_pagar = precio_manzana * cantidad
print("Precio total por 8 manzanas:", total_pagar, "pesos")

por_estudiante = manzanas // estudiantes
print("Cada estudiante recibe", por_estudiante, "manzanas enteras")
```


## Laboratorio 2


## Ejercicio 1
-Se multiplicaron las miles por 1.61 para poder tener las "miles_to_kilometers" asi divide los "kilometers" entre 1.61 para asi poder tener "kilometers_to_miles" y de esa manera el "print" da el codigo de salida y funcionando de esta manera:
```bash
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
```


## Laboratorio 3


-Se le asigno el valor a la X (en este caso se le asigno el valor "1") para que el pudiera calcular la formula de manera correcta sin ningun tipo de error y salida es en este caso: 
```bash
  y = 21.0
  ```