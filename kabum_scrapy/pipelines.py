from itemadapter import ItemAdapter
class KabumScrapyPipeline:
    def process_item(self, item, spider):
        return item
    
class WriteCSV:
    def open_spider(self, spider):
        self.file = open('kabum.csv', 'w', encoding='utf-8')
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        line = f'{item["name"]};{item["price"]};{item["url"]};{item["last_update"]}\n'
        self.file.write(line)
        return item