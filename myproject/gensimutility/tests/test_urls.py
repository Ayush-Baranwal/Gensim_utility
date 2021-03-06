from django.test import TestCase
from django.urls import reverse,resolve
from gensimutility.views import Overview , dataset , home , about , learnmore ,sim_graph 



class TestURL(TestCase):
    
    def test_home_url_loads_properly(self):
            url = reverse('home')
            #print(resolve(url))
            response = self.client.get(url)
            self.assertEquals(resolve(url).func ,home )
    
   
    def test_Overview_url_loads_properly(self):
            url = reverse('overview')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,Overview )
    
    def test_dataset_url_loads_properly(self):
            url = reverse('dataset')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,dataset )
    
    def test_about_url_loads_properly(self):
            url = reverse('about')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,about )
    
    def test_learnmore_url_loads_properly(self):
            url = reverse('learnmore')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,learnmore )
    
    def test_result_url_loads_properly(self):
            url = reverse('sim')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,sim_graph ) 
   
