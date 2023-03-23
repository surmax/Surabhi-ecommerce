from django.db.models import Q
from django.http import Http404
from .models import Product, Category

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .azureSearchClient import AzureSearchClient


# Create your views here.
class LatestProductsList(APIView):
    def get(self, request, format=None):
        azureClient = AzureSearchClient()
        product_json = azureClient.getProducts('*')
        products = product_json['value'] 
        products_refined = []
        for each_product in products:
            products_refined.append({'id':each_product['id'], 'name':each_product['name'], 
                'get_absolute_url':each_product['category']+'/'+each_product['slug'], 
                'description':each_product['description'], 'price':each_product['price'], 
                'get_image':each_product['image'], 'get_thumbnail':each_product['thumbnail']})

        return Response(products_refined[0:4])


class CategoryDetail(APIView):
    def get(self, request, category_slug, format=None):
        #category = self.get_object(category_slug)
        #serializer = CategorySerializer(category)
        azureClient = AzureSearchClient()
        search_query = f"{category_slug}&searchFields=category&searchMode=all"
        products_json = azureClient.getProducts(search_query)
        products = products_json['value']
        products_refined = []
        for each_product in products:
            products_refined.append({'id': each_product['id'], 'name':each_product['name'], 'get_absolute_url': each_product['category']+'/'+each_product['slug'], 
            'description': each_product['description'], 'price': each_product['price'], 'get_image': each_product['image'], 'get_thumbnail':each_product['thumbnail']})

        category_response = {'name': category_slug, 'products': products_refined}

        return Response(category_response)



class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        azureClient = AzureSearchClient()
        search_query = f"{product_slug} {category_slug}&searchFields=slug,category&searchMode=all"
        product_json = azureClient.getProducts(search_query)
        products = product_json['value']
        products_refined = []
        for each_product in products:
            products_refined.append({'id':each_product['id'], 'name':each_product['name'], 
                'get_absolute_url':each_product['category']+'/'+each_product['slug'], 
                'description':each_product['description'], 'price':each_product['price'], 
                'get_image':each_product['image'], 'get_thumbnail':each_product['thumbnail']})

        if len(products_refined) > 0:
            return Response(products_refined[0])
        else:
            print("No products found with that search query") 
            return Response()

class Search(APIView):
    def post(self, request, format=None):
        query = request.data.get('query', '')

        if query:
            azureClient = AzureSearchClient()
            product_json = azureClient.getProducts(query)
            products = product_json['value'] 
            products_refined = []
            for each_product in products:
                products_refined.append({'id':each_product['id'], 'name':each_product['name'], 
                    'get_absolute_url':each_product['category']+'/'+each_product['slug'],
                    'description':each_product['description'], 'price':each_product['price'],
                    'get_image':each_product['image'], 'get_thumbnail':each_product['thumbnail']})
            return Response(products_refined)
        else:
            return Response({"products": []})
