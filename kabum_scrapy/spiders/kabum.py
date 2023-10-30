from types import NoneType
import scrapy
import arrow
from kabum_scrapy.items import KabumScrapyItem
from kabum_scrapy.itemloaders import KabumItemLoader

class KabumSpider(scrapy.Spider):
    name = "kabum"
    allowed_domains = ["www.kabum.com.br"]
    start_urls = ["https://www.kabum.com.br/computadores/monitores"]

    custom_feed = {
        'scraping/feeds/%(name)s_%(time)s.csv': {'format': 'csv'},
    }

    custom_settings = {
        'LOG_LEVEL': 'INFO',
    }
    
    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        settings.setdefault("FEEDS", {}).update(cls.custom_feed)


    def parse(self, response):
        base_url = 'https://www.kabum.com.br/computadores/monitores?'
        products = response.css('div.productCard')

        for product in products:
            kabum_item = KabumItemLoader(item=KabumScrapyItem(), selector=product)
            kabum_item.add_css('name', 'span.nameCard::text'),
            kabum_item.add_css('price', 'span.priceCard::text'),
            kabum_item.add_css('url', 'a.productLink::attr(href)'),
            kabum_item.add_value('last_update', arrow.now().format('DD.MMM.YYYY')),
            yield kabum_item.load_item()

        next_page = response.css('[rel="next"] ::attr(href)').get().split('?')[1]
        if next_page is not NoneType:
            next_page_url = base_url + next_page  
            print(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)
      
            
            