```javascript
$x('//article[@class="product_pod"]/h3/a/@title').map(x => x.value)
(20) ['A Light in the Attic', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History of Humankind', 'The Requiem Red', 'The Dirty Little Secrets of Getting Your Dream Job', 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 'The Black Maria', 'Starving Hearts (Triangular Trade Trilogy, #1)', "Shakespeare's Sonnets", 'Set Me Free', "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'Rip it Up and Start Again', 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'Olio', 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'Libertarianism for Beginners', "It's Only the Himalayas"]
```

```javascript
$x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').map(x => x.wholeText)
(20) ['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']
```

```javascript
$x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()').map(x => x.wholeText)
(50) a lot of content :v
```