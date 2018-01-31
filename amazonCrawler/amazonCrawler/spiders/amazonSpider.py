# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider

class AmazonspiderSpider(CrawlSpider):
    name = 'amazonSpider'
    allowed_domains = ['https://www.amazon.in/gp/bestsellers/electronics/1389432031']
    start_urls = ['https://www.amazon.in/gp/bestsellers/electronics/1389432031']

  
   

    def parse(self, response):

    	#Extracting Product Information from the page
    	for products in response.xpath("//*[@id='zg_centerListWrapper']"):
    		for product in products.xpath("//div[@class='zg_itemWrapper']"):
    			product_image = product.xpath("//div/div/a/div/img/@src").extract()
    			product_name =[name.strip() for name in product.xpath("//div/div/a/div/text()").extract()]
    			product_price = product.xpath("//div/div/div/span/span/text()").extract()
    			product_ratings = product.xpath("//div/div/div/a[@class='a-link-normal']/@title").extract()
    			product_reviews= product.xpath("//div/div/div/a[@class='a-size-small a-link-normal']/text()").extract()
    			
    	

    	#Merging Product Information into a single variable for each product
    	Product = zip(product_name,product_price,product_ratings,product_reviews,product_image)

    	#Defining a dictionary of product information and yeilding it to the console
    	for product in Product:
    		product_info = {
    				'product_name' : product[0],
    				'product_price' : product[1],
    				'product_ratings' : product[2],
    				'product_reviews' : product[3],
    				'product_image' : product[4]
    			}
    		yield product_info
    	






       

        

        