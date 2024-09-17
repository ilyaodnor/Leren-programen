month_discount_brands = 'Vespa,Kymc,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price:float, brand: str, month_discount_brands:str)->float:
    discount_brands = month_discount_brands.split(',')

    if brand  in month_discount_brands:
        return round(price/100*10, 2)
    else:
        return 0.0
