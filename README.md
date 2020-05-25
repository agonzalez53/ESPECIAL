# CALCULAR RUMBOS Y PROYECCIONES 
  
#  Universidad de Colima
 
# Facultad de Ingeniería Civil
 
# Ingeniero Topógrafo Geomático
  
Alma Judith González Montes 

Correo electronico:

galma0564@gmail.com 
  
# RESUMEN
  
Para este proyecto se desarrollara un código Python para poder calcular rumbos y proyeccio-nes de un are que se desea trabajar, donde se integraran algunas funciones trigonométricas para poder saber los resultados de estas ya mencionadas.
  
Palabras clave: Python, rumbos, proyecciones y funciones trigonométricas.
  
# Abstract
  
For this project, a Python code will be developed to calculate the directions and projections of an area that you want to work, where some trigonometric functions will be integrated to know the results of these already mentioned.

Keywords: Python, bearings, projections, and trig functions

# 1.	Introduction 

Para determinar la orientación de algún predio en algún lugar determinado con respecto al norte se emplean los rumbos y azimut, estos son sinónimos pero tienen pequeñas diferencia entre ello al expresarlos escritos. Ambos siste-mas dependen de la dirección del norte real.

El rumbo el ángulo horizontal agudo (90º) que forma con un meridiano de referencia general-mente se toma como tal una línea Norte-Sur que puede estar definida por el N geográfico o el N magnético.

Las proyecciones cartográficas utilizan fórmulas matemáticas para relacionar las coordenadas esféricas del globo con coordenadas planas. Están diseñadas para fine específicos como para datos de gran escala de un área limitada.

Con este proyecto se busca lograr una eficaz raides por medio del código y poder obtener rumbos, azimut y proyecciones de un área limi-tada cuando sea necesario.

# 2. 	Desarrollo

Para hacer una aplicación de cualquier cosa para minimizar los tiempos en su utilización, es necesario tener en cuenta todos los aspectos necesarios que ayudaran a tomar decisiones al momento de elegir los nuevos recursos.

Que tanto será la disminución de tiempo que se generaran a partir de la aplicación, en este caso, se busca minimizar tiempo en hacer algún trabajo topográfico y también, en un futuro sea una muy buena aplicación para que pueda servir en un futuro a cualquier persona.

Es necesario conocer qué tipo de trabajo que se va a realizar, así también el área de superficie que alcanza para posteriormente comenzar con la aplicación de dicho código y también porque no que otras personas le puedan hacer mejorías de un nuevo modelo que mejore todos los as-pectos posibles.

También debemos tomar en cuenta que este tipo de trabajos son utilizados en muchos dife-rentes lugares que requieren una amplia área de estudio.

En la figura de abajo vamos a ilustrar lo que viene siendo el rumbo.

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/1.png)

Para poder realizar dicho trabajo es necesario también sabes que fórmulas que cosas ocupas para confortar el código a utilizar.

•	Primeramente se tienen que pedir los datos en este caso seria los valores de la superficie en  que consta el terreno.

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/2.png)


 Ingresando los valores de las “X y Y” depen-diendo del terreno, superficie o área que se vaya a trabajar. Como en este caso tenemos x1	, x2, y1, y2.
 
•	Continuando con el proceso teniendo esos valores ya, dado el código seguirá calcular los rumbo donde aquí  se em-plea una formula.

          RUMBO = Tan-1  x2 - x1
                         y2 – y1
                         
![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/3.png)

Aquí mismo se aplica esa fórmula ya menciona-da y es así como se obtiene el valor del rumbo. 

•	Calcular la distancia es el siguiente pa-so a realizar en este código aplicando otra fórmula donde se ocupan de los datos que se vienen manejando y poder obtener el resultado esperado.

DISTANCIA = √(x2 – x1)2 + (y2 – y1)2

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/4.png)

•	Proseguiremos con calcular las proyec-ciones tanto como “x” y cómo “y”. Tam-bién se emplean fórmulas para esta par-te de las proyecciones.

PROYECCION X= distancia (Sen (rum-bo))

PROYECCION Y= distancia (Cos (rum-bo))

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/5.png)

Para que así finalmente se obtenga los rumbos y  las proyecciones de una superficie un área o un terreno.

# 2.1. 	Manejo de datos

# 1.	Tratamiento de datos

El programa tomara los datos recaba-dos que la persona ingrese manualmen-te, de esta manera las instrucciones en el código seguirán hasta que se obten-ga lo buscado.

# 2.	Plataforma

Se pretende que este programa funcio-né con la plataforma Windows, anqué se espera que para poder aumentar el uso de este programa se convierta en multiplataforma.

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/6.jpg)

# 3.	Programas

El programa que tiene una gran rele-vancia en este proyecto es el de Python. Esto por  la gran facilidad que le da a estos procedimientos.

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/7.jpg)

# 2.2. 	Resultados

Tratamiento de datos

El programa tomara los datos recabados que la persona ingrese manualmente, de esta manera las instrucciones en el código seguirán hasta que se obtenga lo buscado.

Se observara la primera parte de resultados  que se explicó anteriormente dando los valores de las “x” y las “y“. (Son valores que se les die-ron para corroborar que si funcionaba y corría el programa).

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/8.png)

En seguida se muestra el valor de los rumbos y de las distancias para así proseguir y sacar las proyecciones que ocuparíamos.

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/9.png)

Finalmente ya obtenidos los datos necesarios como distancia y rumbos podemos calcular las proyecciones.

![PalabrasdelTextoAlternativo(https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/10.png)

# 3. 	El resumen
Un resumen de manera personal el proyecto aquí emplead como lo es “ Calculo de rumbos y proyecciones ”se me hace un código muy prác-tico para poder saber las proyecciones de un área superficie terreno oh el cual vean la manera más adecuada y correcta de emplear  y si es que puede funcionar en alguna otra área o algún otro objetivo. 

Porque no, adelantes como mejor lo vea la persona para su adaptación. Por alcance la determinación de dicho código tiene un fin que si bien se ha venido dando a conocer como lo son las proyecciones y los rumbos.

# Referencias

•	https://www.cursosgis.com/cuales-con-las-ides-mas-actuales-y-recomendadas-para-trabajar-con-python/

•	https://www.muycomputer.com/2019/01/14/adios-a-windows-7-un-ano/

•	https://desktop.arcgis.com/es/arcmap/10.3/guide-books/map-projections/about-map-projections.htm

•	https://sites.google.com/site/rumbosyazimut/introduccion

•	https://es.slideshare.net/alexmay12/azimut-y-rumbo-maycol-vergara

•	http://sanvincentvr.blogspot.com/2010/10/rumbo-y-direccion.html 


# POSTER

![PalabrasdelTextoAlternativo](https://github.com/agonzalez53/ESPECIAL/blob/master/IMAGENES/11.png)










 






