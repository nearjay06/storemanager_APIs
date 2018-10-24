class ProductsPoints():
    def __init__(self,id,name,price):
      self.product_id = id
      self.product_name = name
      self.product_price = price
     
    def add_products_to_list(self):
      data={
          "product_id": self.product_id,
          "product_name": self.product_name,
          "product_price": self.product_price 
         }

      return data
        
             
