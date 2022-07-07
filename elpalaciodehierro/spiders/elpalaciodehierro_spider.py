import scrapy
import datetime
'''
 default_dict = {
                    'Date': datetime.now().strftime("%Y-%m-%d"),
                    'Canal': 'Scorpion',
                    'Category': breadcrumbs_dict.get(0, ''),
                    'Subcategory': breadcrumbs_dict.get(1, ''),
                    'Subcategory2': breadcrumbs_dict.get(2, ''),
                    'Subcategory3': '',
                    'Marca': brand,
                    'Modelo': '',
                    'SKU': sku,
                    'UPC': sku,
                    'Item': item,
                    'Item Characteristics': item_characteristics,
                    'URL SKU': response.url,
                    'Image': image,
                    'Price': '',
                    'Sale Price': '',
                    'Shipment Cost': '',
                    'Sales Flag': '',
                    'Store ID': '',
                    'Store Name': '',
                    'Store Address': '',
                    'Stock': '',
                    'UPC WM': sku.zfill(16),
                    'Final Price': '',
                    }
'''

# scrapy.spiders.SitemapSpider
class ElpalaciodeSpider(scrapy.Spider):
    name = 'elpalaciode'
    #sitemap_urls = ['https://www.elpalaciodehierro.com/sitemap_index.xml']
    #sitemap_rules = [(r'.html', 'parse')]
    start_urls = ['https://www.elpalaciodehierro.com/under-armour-tenis-para-correr-shadow-hombre-41726918.html']

    def parse(self, response):
        item = dict()
        item['Marca'] = response.css('h2[class=b-product_main_info-brand] a::text').get().strip()
        #item['Date'] = datetime.datetime.now().strftime("%Y-%m-%d")
        #item['url'] = response.url
        yield item
