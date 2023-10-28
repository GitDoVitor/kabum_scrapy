import arrow
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class KabumScrapyPipeline:
    def process_item(self, item, spider):
        return item
    
class EmptyPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('price') is None:
            adapter['price'] = '0'

        if adapter.get('name') is None:
            adapter['name'] = 'NA'

        if adapter.get('url') is None:
            adapter['url'] = 'NA'

        if adapter.get('last_update') is None:
            adapter['last_update'] = arrow.now().format('DD.MMM.YYYY')

        return item