```javascript

let url = http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html

let title = $x('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').map(x => x.wholeText).at()
> 'A Light in the Attic'

let stock = $x('//*[@id="content_inner"]/article[@class="product_page"]/div[@class="row"]/div/p[contains(@class, "instock")]/text()').map(x => x.wholeText).at(1).trim()
> 'In stock (22 available)'

let description = $x('//article["product_page"]/p/text()').map(x => x.wholeText).at()
> "It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more"

```