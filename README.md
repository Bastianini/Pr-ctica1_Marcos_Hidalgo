# Pr-ctica1_Marcos_Hidalgo

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