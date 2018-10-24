class Transactions():
    def __init__(self,sale_id,sale_product,sale_total):
     self.sale_id = sale_id
     self.sale_product = sale_product
     self.sale_total = sale_total

    def return_sales_records(self):
        trades ={
          "sale_id": self.sale_id,
          "sale_product": self.sale_product,
          "sale_total": self.sale_total 
         }
        
        return trades
