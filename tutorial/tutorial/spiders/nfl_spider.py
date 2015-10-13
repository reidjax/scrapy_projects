import scrapy
from tutorial.items import players


class nflSpider(scrapy.Spider):
	name = 'nfl'
	allowed_domains = ['http://espn.go.com']
	start_urls =['http://espn.go.com/nfl/college/_/letter/a']

	def parse(self, response):
		item = players()
		
		item['title'] = response.xpath('//title/text()').extract()
		item['college_team'] = response.xpath('//tr[contains(@class, "stathead")]/td/text()').extract()
		item['player_and_nfl_team'] = response.xpath("//tr[contains(@class, 'oddrow') or contains(@class, 'evenrow')]/td/a/text()").extract()
		item['position'] = response.xpath("//tr[contains(@class, 'oddrow') or contains(@class, 'evenrow')]/td/text()").extract()

		yield item

		# filename = response.url.split("/")[-2] + '.html'
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)






# Things to extract

# response.xpath('//tr[@class="stathead"]')
# response.xpath("//tr[contains(@class, 'oddrow') or contains(@class, 'evenrow')]")
# response.xpath("//tr[contains(@class, 'oddrow') or contains(@class, 'evenrow') or contains(@class, 'stathead')]")

# # add /a for names and teams, exclude for position
# # look into adding an OR option
# response.xpath("//tr[contains(@class, 'oddrow') or contains(@class, 'evenrow') or contains(@class, 'stathead')]/td/a/text()").extract()
# # Page title
# response.xpath('//title/text()').extract()