from queue import Empty
import arrow
from itemadapter import ItemAdapter

class KabumScrapyPipeline:
    def process_item(self, item, spider):
        return item
    
class EmptyItemPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price') == '----':
            adapter['price'] = 'NA'
        
        if adapter.get('name') == '----':
            adapter['name'] = 'NA'

        if adapter.get('url') == '----':
            adapter['url'] = 'NA'

        if adapter.get('last_update') is None:
            adapter['last_update'] = arrow.now().format('DD.MMM.YYYY')
        return item