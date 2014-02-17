from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from fypscraper.items import SightingItem

class SightingSpider(Spider):
	name = "species"
	allowed_domains = ["http://www.iwdg.ie"]
	start_urls = ["http://www.iwdg.ie/_customasp/iscope/sightings/default.asp?dataset=sighting&searchType=advanced&from_day=1&from_month=1&from_year=2014&to_day=&to_month=&to_year=&resultsFormat=table&search1=Search",
	]

	def parse(self, response):
		sel = Selector(response)
		item = SightingItem()

		#loader = ItemLoader(item, sel)
		
		#loader.default_input_processor = MapCompose(unicode.strip)
		#loader.default_output_processor = Join()

		#loader.add_xpath('specname', ".//*[@id='k2Container']/div[2]/h2/span/text()")

		#return loader.load_item()

		item['specname'] = sel.xpath(".//*[@id='k2Container']/div[2]/h2/span/text()").extract()
		#item['specclass'] = "Mammalia"
		#item['specorder'] = "Cetecea"
		#item['clss'] = sel.xpath(".//*[@id='article_0']/p/text()").extract()
		return item

		#clss = sel.xpath('.//*[@id='article_0']/p').extract()
		#ordr = sel.xpath('').extract()





