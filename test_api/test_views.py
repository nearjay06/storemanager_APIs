import json
import unittest
from view.views import app


class FlaskTest(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
    
  
  def test_admin_can_get_all_products(self):
    response = self.app.get('/api/v1/products/')
    self.assertEqual(response.status_code,400)
    self.assertEqual(response.content_type,'application/json')


  # def test_admin_can_add_product(self):
    # response = self.app.post('/api/v1/products',
    #                          content_type="application/json",
    #                           data=json.dumps(dict( product_name = "water",
    #                                                 product_price = 800)))
    # response_json = json.loads(response.data.decode())
    # response_json = json.get_json()
    # self.assertEqual(response.status_code,200)
    # self.assertIn("product added", response_json['message'])


  def test_get_specific_product(self):
    response = self.app.get('/api/v1/products/1')
    response_json = json.loads(response.data.decode())
    self.assertIn("have product", response_json['message'])
    # self.assertEqual(response.status_code,200)

  def test_store_attendant_can_add_sale_order(self):
    response = self.app.post('/api/v1/sales/',
                              content_type="application/json",
                              data=json.dumps(dict(sale_id = 1,
                                                    sale_product = "soap",
                                                    sale_total = 3000)))
    response_json = json.loads(response.data.decode())                                                
    self.assertEqual(response.status_code,201)
    self.assertEqual("sale order record created", response_json['message'])

  def test_admin_can_get_sale_order_records(self):
    response = self.app.get('/api/v1/sales/',
                                content_type="application/json",
                                data=json.dumps(dict(sale_id = 1,
                                                      sale_product = "soap",
                                                      sale_total = 3000)))                                               
    self.assertEqual(response.status_code,400)

  def test_get_specific_sale_order_record(self):
    response = self.app.get('/api/v1/sales/1')
    response_json = json.loads(response.data.decode())
    self.assertEqual("sale order record not found", response_json['message'])
    
    

if __name__ == '__main__':
     unittest.main()
