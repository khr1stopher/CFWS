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

Expresiones Xpath

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

all the examples was using [quotes](http://quotes.toscrape.com)

### Predicados Xpath

is using '[]' into a xpath expresion

without predicate
```xpath
$x('/html/body/div/div')
return (2) [div.row.header-box, div.row]
```

with predicate
```xpath
$x('/html/body/div/div[1]')
return [div.row.header-box]
```

for get the last item we user 'last()
```xpath
$x('/html/body/div/div[last()]')
return [div.row]
```

with atributes
```xpath
$x('//span[@class="text"]/text()')
```

Operadores Xpath

1. '!=' i want to get all the span without the class .text 
```xpath
$x('//span[@class!="text"]')
(11) [span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.sh-red]
```
2. 'position()' u can use this with the common operators
```xpath
$x('/html/body/div/div[position()>1]')
```
3. 'or' if any of the conditions is truth we'll get the span with them
```xpath
$x('//span[@class="text" or @class="tag-item"]')
(20) [span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item]
```
4. 'and' we need both contentions to be true
```xpath
$x('//span[@class="text" and @class="tag-item"]')
[]
```


$x('//span[not(@class)]')
(11) [span, span, span, span, span, span, span, span, span, span, span]


### Wildcards

1. '/*' selecciona todos los nodos dentro del nodo seleccionado

```xpath
$x('/html/*')
(2) [head, body]
```

2. '//*' selecciona todos los nodos que existen

```xpath
$x('//*')
(153) [html, head, meta, title, link, link, style#operaUserStyle, style, body, div.container, div.row.header-box, div.col-md-8, h1, a, div.col-md-4, p, a, div.row, div.col-md-8, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, …]
```

3. '/@*'  select all the los attributes inside the node selected
```xpath
$x('//span[@class="text"]/@*')
(20) [class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop]
```

4. '//element/@*' select attributes of all the div elements in the body document

```xpath
$x('/html/body//div/@*')
(48) [class, class, class, class, class, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, itemscope, itemtype, class, class, class]
```

5. with node() u select all inside the current node
```xpath
$x('//span[@class="text" and @itemprop="text"]/node()')
(10) [text, text, text, text, text, text, text, text, text, text]
```

### In-text search en Xpath

1. starts-with
```xpath
$x('//small[@class="author" and starts-with(.,"A")]')
(4) [small.author, small.author, small.author, small.author]
```

```xpath
$x('//small[@class="author" and starts-with(.,"A")]/text()').map(x => x.wholeText)
(4) ['Albert Einstein', 'Albert Einstein', 'Albert Einstein', 'André Gide']
```

2. using the function 'contains'
```xpath
$x('//small[@class="author" and contains(.,"Ro")]/text()').map(x => x.wholeText)
(2) ['J.K. Rowling', 'Eleanor Roosevelt']
```

3. using the function 'ends-with'
```xpath
x('//small[@class="author" and ends-with(.,"t")]/text()').map(x => x.wholeText)
```

3. using the function 'matches'
```xpath
$x('//small[@class="author" and matches(.,"A.*n")]/text()').map(x => x.wholeText)
```