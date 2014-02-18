from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from fypscraper.items import SpeciesItem

class SpeciesSpider(Spider):
	name = "species"
	allowed_domains = ["http://www.iwdg.ie"]
	start_urls = [
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2199",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2200",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2201",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2202",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2203",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2204",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2205",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2206",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2207",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2208",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2209",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2210",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2211",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2212",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2213",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2214",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2215",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2216",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2217",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2218",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2219",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2220",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2221",
		"http://www.iwdg.ie/index.php?option=com_k2&view=item&id=2222",
	]

	def parse(self, response):
		sel = Selector(response)
		item = SpeciesItem()
		item['specname'] = sel.xpath(".//*[@id='k2Container']/div[2]/h2/span/text()").extract()
		item['specclass'] = sel.xpath(".//*[@id='article_0']/p/text()").extract()
		return item

