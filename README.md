# Curso de Fundamentos de Web Scraping con Python y Xpath

Web scraping: Es una técnica usada por data scientist y backend developers para extraer información de internet, accede a esto usando el protocolo de tranferencias de hipertexto (HTTP) o a través de un navegador. Los datos extraídos usualmente son guardados en una
base de datos, incluso en una hoja de cálculo para posteriores análisis. Puede hacerse de manera automática (bot) o manualmente.

Xpath: es un lenguaje que sirve para apuntar a las partes de un documento XML. Xpath modela un documento XML como un árbol de nodos. Existen diferentes tipos de nodos: elementos, atributos, texto.

Corparations than use webscrapy
- NSA
- CIA

## articles

1. [14 Web Scraping Tools: Who They Are For & What They Excel At](https://www.scraperapi.com/blog/the-14-best-web-scraping-tools/)

2. ParseHub is a system for automated scrap

3. http://plasmasturm.org/log/xpath101/

frameworks to do webscrapy

1. scrapy
2. Puppeteer
3. playwright
4. cypress

http status category

Informational responses (100 – 199)
Successful responses (200 – 299)
Redirection messages (300 – 399)
Client error responses (400 – 499)
Server error responses (500 – 599)

hypertext markup language :v

snipet: a lite piece of code

robots.txt
proporciona información a los rastreadores de los buscadores sobre las páginas o los archivos que pueden solicitar o no de tu sitio web.

https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt?hl=es&visit_id=638213797110764645-1443811511&rd=1

XPath esta formado por nodos/etiquetas

site to practice scraping
http://toscrape.com

NODOS: a node is either a redistribution point or a communication endpoint /ETIQUETAS Un nodo puede contener a otros nodos.
En otras palabras Xpath nos permitirá navegar en los diferentes niveles de profundidad
deseados con el fin extraer información. Para describir los nodos y relaciones con Xpath se usan una
sintaxis de ejes.

Para escribir expresiones se usara lo siguiente 
$x(''). Entre las comillas se van a escribir las expresiones,
las expresiones tienen diferentes símbolos que tienen una utilidad.

Se describe la utilidad de cada expresión.

/ hace referencia a la raíz, o tambien significa un salto entre nodos. 
e.g /html/bodyMuestra todo lo que hay dentro del body de html
// Sirve para acceder a todos los nodos con la etiqueta seleccionada. 
e.g [*//span](//span) muestra todas las etiquetas span*
.. Sirve para acceder a los nodos padre de la etiqueta tag. 
e.g //span/.. accede a todos los nodos padre de span
. Hace referencia al nodo actual. 
e.g. //span/. es equivalent a //span
@ Sirve para traer los atributos. 
e.g //div/@class Nos da las clases de todos los divs