class Product():

    def __init__(self, product_id=None, product_type_id=None, product_code=None, 
                 product_finish_goods_brand=None,
                 product_name=None, product_batch_number=None, 
                 product_netto=None, product_measurement_unit_id=None,
                 product_colour_id=None,
                 product_raw_material_tradename=None,
                 product_raw_material_inchiname=None, 
                 product_raw_material_inchiname_percentage=None,
                 product_raw_material_function=None,
                 product_raw_material_expired_date=None,
                 product_raw_material_halal_id=None, 
                 product_packaging_item=None,
                 product_packaging_item_part_id=None,
                 product_finish_goods_name=None, product_finish_goods_bpom_number=None, 
                 product_finish_goods_bpom_expired_date=None, 
                 product_finish_goods_halal_certification_number=None, 
                 product_finish_goods_substance_id=None, product_packaging_type=None,
                 product_packaging_item_fullname=None, product_creation_date=None, 
                 product_update_date=None, product_last_user=None) -> None:
        
        self.product_id = product_id
        self.product_type_id = product_type_id
        self.product_batch_number = product_batch_number
        self.product_netto = product_netto
        self.product_measurement_unit_id = product_measurement_unit_id
        self.product_colour_id = product_colour_id
        self.product_raw_material_tradename = product_raw_material_tradename
        self.product_raw_material_inchiname = product_raw_material_inchiname
        self.product_raw_material_inchiname_percentage = product_raw_material_inchiname_percentage
        self.product_raw_material_function = product_raw_material_function
        self.product_raw_material_expired_date = product_raw_material_expired_date
        self.product_raw_material_halal_id = product_raw_material_halal_id
        self.product_packaging_item = product_packaging_item
        self.product_packaging_item_part_id = product_packaging_item_part_id
        self.product_finish_goods_name = product_finish_goods_name
        self.product_finish_goods_bpom_number = product_finish_goods_bpom_number
        self.product_finish_goods_bpom_expired_date = product_finish_goods_bpom_expired_date
        self.product_finish_goods_halal_certification_number = product_finish_goods_halal_certification_number
        self.product_finish_goods_substance_id = product_finish_goods_substance_id
        self.product_creation_date = product_creation_date
        self.product_update_date = product_update_date
        self.product_last_user = product_last_user
        self.product_packaging_item_fullname = product_packaging_item_fullname
        self.product_code = product_code
        self.product_finish_goods_brand = product_finish_goods_brand
        self.product_name = product_name
        self.product_packaging_type = product_packaging_type

    def to_JSON(self):
        return {
            'PRODUCT_ID': self.product_id,
            'PRODUCT_TYPE_ID': self.product_type_id,
            'PRODUCT_BATCH_NUMBER': self.product_batch_number,
            'PRODUCT_NETTO': self.product_netto,
            'PRODUCT_MEASUREMENT_UNIT_ID': self.product_measurement_unit_id,
            'PRODUCT_COLOUR_ID': self.product_colour_id,
            'PRODUCT_RAW_MATERIAL_TRADENAME': self.product_raw_material_tradename,
            'PRODUCT_RAW_MATERIAL_INCHINAME': self.product_raw_material_inchiname,
            'PRODUCT_RAW_MATERIAL_INCHINAME_PERCENTAGE': self.product_raw_material_inchiname_percentage,
            'PRODUCT_RAW_MATERIAL_FUNCTION': self.product_raw_material_function,
            'PRODUCT_RAW_MATERIAL_EXPIRED_DATE': self.product_raw_material_expired_date,
            'PRODUCT_RAW_MATERIAL_HALAL_ID': self.product_raw_material_halal_id,
            'PRODUCT_PACKAGING_ITEM': self.product_packaging_item,
            'PRODUCT_PACKAGING_ITEM_PART_ID': self.product_packaging_item_part_id,
            'PRODUCT_FINISH_GOODS_NAME': self.product_finish_goods_name,
            'PRODUCT_FINISH_GOODS_BPOM_NUMBER': self.product_finish_goods_bpom_number,
            'PRODUCT_FINISH_GOODS_BPOM_EXPIRED_DATE': self.product_finish_goods_bpom_expired_date,
            'PRODUCT_FINISH_GOODS_HALAL_CERTIFICATION_NUMBER': self.product_finish_goods_halal_certification_number,
            'PRODUCT_FINISH_GOODS_SUBSTANCE_ID': self.product_finish_goods_substance_id,
            'PRODUCT_CREATION_DATE': self.product_creation_date,
            'PRODUCT_UPDATE_DATE': self.product_update_date,
            'PRODUCT_LAST_USER': self.product_last_user,
            'PRODUCT_PACKAGING_ITEM_FULLNAME': self.product_packaging_item_fullname,
            'PRODUCT_CODE': self.product_code,
            'PRODUCT_FINISH_GOODS_BRAND': self.product_finish_goods_brand,
            'PRODUCT_NAME': self.product_name,
            'PRODUCT_PACKAGING_TYPE': self.product_packaging_type
        }
