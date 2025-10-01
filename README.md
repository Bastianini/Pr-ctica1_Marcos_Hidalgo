# Pr-ctica1_Marcos_Hidalgo

Información importante:
Jupyter no maneja bien el uso de varios inputs seguidos. Entonces hay veces que la respuesta se imprime dos veces pero el código está bien, ya que lo he probado fuera de jupyter y esto no ocurre. Por eso tengo un fichero Prueba.py, en el que he ido probando el código cuando veia algo raro.

Preguntas LLM's. Para esta practica usaré copilot.

Pregunta 1:

- Necesito saber como se define una cadena y una lista en python.

Le he hecho esta consulta porque python es practicamente nuevo para mi y no tenía muy claro si sabia o no definir cadenas y listas. Su respuesta ha sido correcta, ya que coincide con lo que pone en los apuntes de clase.

Pregunta 2: 

- ¿que es y como se hace un docstring?

Me ha explicado como se hace un docstring y me ha contado su utilidad mediante la función help(). Es bastante util, ya que te permite buscar información sobre una función en concreto rapidamente en lugar de ir buscando a lo largo de todo el código.

Pregunta 3: 

- Tengo un problema en el ejercicio 2 de numeros primos ya que quiero que el usuario pueda meter el valor del límite de la lista de primos por teclado, pero al mostrar por pantalla me muestra el resultado por duplicado. Le he preguntado como solucionarlo.

Su primera idea era que jupyter se liaba con la función main(), ya que al estar dividido en celdas, podia ser que ejecutara la celda automaticamente y que se llamara la función dos veces. Tras un rato discutiendo, ha llegado a la conclusión de que el problema era que jupyter por su forma de trabajar no maneja bien varios inputs seguidos y actua ejecutando la celda más de una vez. Está solución es correcta ya que he probado las mismas funciones con valores fijos y se imprimia el resultado solo una vez. 

Pregunta 4:

- Le he preguntado como hacer el menú del ejercicio 3

Me ha respondido con un menú funcional, usando bucle while, pero yo esperaba que me contestara con la otra forma que vimos en clase, que era el match statement. Lo he tenido que buscar en los apuntes de clase y hasta que no le he dicho como se llama la instrucción no ha sido capaz de explicar.

Pregunta 5:

- ¿Porqué me imprime 'hola' como cadena más corta y cadena más larga si he puesto 'que'?

En el ejercicio 4, el de la lista de cadenas en la primera prueba, he hecho un ejemplo con una lista corta ['hola', 'que ', 'hola']. Durante la prueba he introducido sin querer un espacio después de 'que ' y por eso no salia que 'que' es la cadena más corta de la lista, porque al llevar un espacio detrás ocupa 4 caracteres.

Pregunta 6:

- ¿Que son las expresiones regulares en python?

Por lo que he entendido las expresiones regulares son como "atajos" para realizar busquedas rápidas de elementos que no son palabras, por ejemplo, numeros, fin e inicio de linea...

Pregunta 7: 

- ¿Que hace re.compile? (Usado para la fecha en el ejercicio 6)

Compile es una expresión regular de python que "traduce" una cadena al formato que realmente queremos expresar, por ejemplo una fecha, al introducir una fechar se introduce como cadena de caracteres pero con re.compile este la "transforma" en un objeto de tipo fecha de tal forma que se pueda reutilizar de forma mas eficiente.  

Para está práctica he utilizado copilot ya que es bastante accesible en Visual Studio Code. Lo que ocurre es que no reacciona ante diferentes estados de ánimo ni diferencia entre consulta y orden.