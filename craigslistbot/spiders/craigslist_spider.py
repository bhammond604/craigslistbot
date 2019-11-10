# Imports
import scrapy
from craigslistbot.items import CraigslistbotItem

# Create the spider
class CraigslistSpider(scrapy.Spider):
	"""Spider for Craigslist
	
	Methods:
		__init__() - Initialize the spider
		start_requests() - Send HTTP requests
		parse() - Parse the response and write to file
	"""
	# Specify the spiders name
	name = "craigslistbot"
	
	def start_requests(self):
		"""Send HTTP requests
		
		Arguments:
			self - object - The CraigslistSpider object
		"""
		
		# Yield the HTTP response
		yield scrapy.Request("https://%s.craigslist.org/search/%s" % (self.location, self.category))
	
	def parse(self, response):
		""" Parse the response and write to file
		
		Arguments:
			self - object - The CraigslistSpider object
			response - object - The response from the start URL
		"""
		
		# Get the number of ads per page with the ad number range
		big_number = int(response.xpath("/html/body/section/form/div[3]/div[3]/span[2]/span[3]/span[1]/span[2]/text()").get())
		small_number = int(response.xpath("/html/body/section/form/div[3]/div[3]/span[2]/span[3]/span[1]/span[1]/text()").get())
		ads_per_page = (big_number - small_number) + 1
		
		# Write to log
		self.log("Ads per page: %d" % ads_per_page)
		
		# Iterate over every ad
		for i in range(1, ads_per_page+1):
			# Pull the <a> tags containing the ad
			ad = response.xpath("/html/body/section/form/div[4]/ul/li[%s]/p/a" % i).get()
			
			# Add the data to the item
			ad_name = response.xpath("/html/body/section/form/div[4]/ul/li[%s]/p/a/text()" % i).get()
			ad_link = response.xpath("/html/body/section/form/div[4]/ul/li[%s]/p/a/@href" % i).get()
			data_id = response.xpath("/html/body/section/form/div[4]/ul/li[%s]/p/a/text()" % i).get()
			
			# Create the item
			craigslistbot_item = CraigslistbotItem(name=ad_name, link=ad_link, identifier=data_id)
			
			# Yield the item
			yield craigslistbot_item
			
		# Get the next page
		next_page = response.xpath("/html/body/section/form/div[3]/div[3]/span[2]/a[3]/@href").get()
		
		# If the next page exists
		if next_page is not None:
			# Join the URL
			next_page = response.urljoin(next_page)
			
			# Parse the next page
			yield scrapy.Request(next_page, callback=self.parse)
	
		
		
