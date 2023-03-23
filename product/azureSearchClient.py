import requests 

class AzureSearchClient(): 
	def __init__(self): 
		self.url = "https://ecomproductsearchservice.search.windows.net/indexes/product-index/docs?api-version=2021-04-30-Preview&search="
		api_key = "CvL0Uali8dquLdI5EpGGWSmhnahH19MTJl6sHWlbLAAzSeDPaT15"
		self.header = {"api-key":api_key}

	def getProducts(self, query): 
		self.url = self.url+query
		print(self.url)
		response = requests.get(self.url, headers=self.header)
		response_json = response.json()
		return response_json