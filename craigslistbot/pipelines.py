# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Imports
import json
from scrapy.exporters import JsonItemExporter
# Constants
JSON_FILE = "output.json"

class CraigslistbotPipeline(object):
	"""Pipeline for writing to JSON
	
	Methods:
		__init__() - Initialize the data pipeline
		close_spider() - Stop the spider and close the file
		process_item() - Export to JSON
	"""
	
	def __init__(self):
		"""Initialize the data pipeline
		
		Arguments:
			self - object - The CraigslistbotPipeline object
		"""
		
		# Open the JSON file
		self.file = open(JSON_FILE, "wb")
		
		# Create the exporter
		self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
		
		# Begin exporting the data
		self.exporter.start_exporting()
		
	def close_spider(self, spider):
		"""Stop the spider and close the file
		
		Arguments:
			self - object - The CraigslistbotPipeline object
			spider - object The spider
		"""
		
		# Stop exporting
		self.exporter.finish_exporting()
		
		# Close the file
		self.file.close()
	
	def process_item(self, item, spider):
		"""Export to JSON
		
		Arguments:
			self - object - The CraigslistbotPipeline object
			item - object - The item to export to JSON
			spider - object - The spider
		"""
		
        # Export the item and return
		self.exporter.export_item(item)
		return item
