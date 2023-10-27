import scrapy
from scrapy.loader import ItemLoader
import arrow
from kabum_scrapy.items import KabumScrapyItem
from kabum_scrapy.itemloaders import KabumItemLoader

class KabumSpider(scrapy.Spider):
    name = "kabum"
    allowed_domains = ["www.kabum.com.br"]
    start_urls = ["https://www.kabum.com.br/computadores/monitores"]

    


    def parse(self, response):
        products = response.css('div.productCard')

        for product in products:
            kabum_item = KabumItemLoader(item=KabumScrapyItem(), selector=product)
            kabum_item.add_css('name', 'span.nameCard::text'),
            kabum_item.add_css('price', 'span.priceCard::text'),
            kabum_item.add_css('url', 'a.productLink::attr(href)'),
            kabum_item.add_value('last_update', arrow.now().format('DD.MMM.YYYY')),
            yield kabum_item.load_item()

        # next_page = f'https://www.kabum.com.br/computadores/monitores?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
