class GetPostProduct():

    def __init__(self, product_id=None, product_type_id=None) -> None:
        
        self.product_id = product_id
        self.product_type_id = product_type_id

    def to_JSON(self):
        return {
            'PRODUCT_ID': self.product_id,
            'PRODUCT_TYPE_ID': self.product_type_id
        }
