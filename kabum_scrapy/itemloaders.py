from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class KabumItemLoader(ItemLoader):

    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x : x.split('R$')[-1].strip())
    url_in = MapCompose(lambda x : 'https://www.kabum.com.br' + x)