from database.db import get_connection
from .entities.Product import Product


class ProductModel():

    @classmethod
    def getProducts(self, parameters):
        try:
            connection = get_connection()
            v_flag = 0
            v_params = {}
            if len(parameters) > 0:
                for v in parameters:
                    if v['value'] is not None and v['value'] != '':
                        v_params[v['fieldName']] = v['value']
                
            products_array = []

            with connection.cursor() as cursor:
                v_sql = """SELECT PRODUCT_ID, PRODUCT_TYPE_ID, PRODUCT_CODE,
                    PRODUCT_FINISH_GOODS_BRAND, PRODUCT_NAME,
                    PRODUCT_BATCH_NUMBER, PRODUCT_NETTO, PRODUCT_MEASUREMENT_UNIT_ID,
                    PRODUCT_COLOUR_ID, PRODUCT_RAW_MATERIAL_TRADENAME,
                    PRODUCT_RAW_MATERIAL_INCHINAME, PRODUCT_RAW_MATERIAL_INCHINAME_PERCENTAGE,
                    PRODUCT_RAW_MATERIAL_FUNCTION, PRODUCT_RAW_MATERIAL_EXPIRED_DATE,
                    PRODUCT_RAW_MATERIAL_HALAL_ID, PRODUCT_PACKAGING_ITEM,
                    PRODUCT_PACKAGING_ITEM_PART_ID, PRODUCT_FINISH_GOODS_NAME,
                    PRODUCT_FINISH_GOODS_BPOM_NUMBER, PRODUCT_FINISH_GOODS_BPOM_EXPIRED_DATE,
                    PRODUCT_FINISH_GOODS_HALAL_CERTIFICATION_NUMBER,
                    PRODUCT_FINISH_GOODS_SUBSTANCE_ID,
                    PRODUCT_PACKAGING_TYPE, PRODUCT_PACKAGING_ITEM_FULLNAME,
                    PRODUCT_CREATION_DATE, PRODUCT_UPDATE_DATE, PRODUCT_LAST_USER
                    FROM PRODUCTS """
                
                if (len(parameters) > 0 and
                    ('PRODUCT_ID' in v_params or
                     'PRODUCT_TYPE_ID' in v_params)):
                    
                    v_sql += """ WHERE """
                    if 'PRODUCT_ID' in v_params:
                        if v_flag == 1:
                            v_sql += """ AND """;
                        v_sql += f" PRODUCT_ID = {v_params['PRODUCT_ID']} ";
                        v_flag = 1;
                    
                    if 'PRODUCT_TYPE_ID' in v_params:
                        if v_flag == 1:
                            v_sql += """ AND """;
                        v_sql += f" PRODUCT_TYPE_ID = {v_params['PRODUCT_TYPE_ID']} ";
                        v_flag = 1;

                cursor.execute(v_sql);
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(
                        product_id=row[0],
                        product_type_id=row[1],
                        product_code=row[2],
                        product_finish_goods_brand=row[3],
                        product_name=row[4],
                        product_batch_number=row[5],
                        product_netto=row[6],
                        product_measurement_unit_id=row[7],
                        product_colour_id=row[8],
                        product_raw_material_tradename=row[9],
                        product_raw_material_inchiname=row[10],
                        product_raw_material_inchiname_percentage=row[11],
                        product_raw_material_function=row[12],
                        product_raw_material_expired_date=row[13],
                        product_raw_material_halal_id=row[14],
                        product_packaging_item=row[15],
                        product_packaging_item_part_id=row[16],
                        product_finish_goods_name=row[17],
                        product_finish_goods_bpom_number=row[18],
                        product_finish_goods_bpom_expired_date=row[19],
                        product_finish_goods_halal_certification_number=row[20],
                        product_finish_goods_substance_id=row[21],
                        product_packaging_type=row[22],
                        product_packaging_item_fullname=row[23],
                        product_creation_date=row[24],
                        product_update_date=row[25],
                        product_last_user=row[26]
                    )
                    products_array.append(product.to_JSON())

            connection.close()
            return products_array
        except Exception as ex:
            raise Exception(ex)

    # @classmethod
    # def update_product(self, movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("""UPDATE movie SET title = %s, duration = %s, released = %s 
    #                             WHERE id = %s""", (movie.title, movie.duration, movie.released, movie.id))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)

    # @classmethod
    # def delete_product(self, movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("DELETE FROM movie WHERE id = %s", (movie.id,))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)
