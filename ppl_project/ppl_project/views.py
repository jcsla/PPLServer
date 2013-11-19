
from django.http import HttpResponse
from ppl_project.ppl.models import *
import json

def insert_ppl_data(request):
    try:
        drama_code = request.GET['drama_code']
        product_name = request.GET['product_name']
        product_image = request.GET['product_image']
        brand_name = request.GET['brand_name']
        store_link = request.GET['store_link']
        price = request.GET['price']
        start_time = request.GET['start_time']
        end_time = request.GET['end_time']
        story = request.GET['story']
    except:
        story = ''

    drama_list = Drama.objects.all()
    drama_code_flag = True
    for drama in drama_list:
        if drama_code == drama.drama_code:
            drama_code_flag = False

    if drama_code_flag:
        drama_make = Drama(drama_code=drama_code, story=story)
        drama_make.save()

    product_make = Product(drama_code=drama_code, product_name=product_name
        , product_image=product_image, brand_name=brand_name, store_link=store_link, price=price)
    product_make.save()

    get_product_code = Product.objects.all()

    ppl_make = PPL(drama_code=drama_code,
                   product_code=get_product_code[len(get_product_code) - 1].product_code,
                   start_time=start_time, end_time = end_time)
    ppl_make.save()

    return HttpResponse(True)

def get_ppl_data(request):
    try:
        drama_code = request.GET['drama_code']
    except:
        return HttpResponse(False)
    try:
        current_time = int(request.GET['current_time'])
    except:
        product_list = []
        all_product = Product.objects.filter(drama_code=drama_code)
        all_time = PPL.objects.filter(drama_code=drama_code)
        for i in range(len(all_product)):
            product_list.append({"drama_code": all_product[i].drama_code, "product_code": all_product[i].product_code, "product_name": all_product[i].product_name,
                                 "product_image": all_product[i].product_image, "brand_name": all_product[i].brand_name, "store_link": all_product[i].store_link,
                                 "price": all_product[i].price, "start_time": all_time[i].start_time, "end_time": all_time[i].end_time})

        return HttpResponse(json.dumps(product_list, ensure_ascii=False))

    all_ppl = PPL.objects.all()
    product_code_list = []
    for data in all_ppl:
        if data.drama_code == drama_code and \
                        data.start_time <= current_time and data.end_time >= current_time:
            product_code_list.append(data.product_code)

    product_list = []
    for product_code in product_code_list:
        p = Product.objects.filter(drama_code=drama_code, product_code=product_code)
        time_data = PPL.objects.filter(drama_code=drama_code, product_code=product_code)
        for data in p:
            product_list.append({"drama_code": data.drama_code, "product_code": data.product_code, "product_name": data.product_name,
                                 "product_image": data.product_image, "brand_name": data.brand_name, "store_link": data.store_link, "price": data.price,
                                 "start_time": time_data[0].start_time, "end_time": time_data[0].end_time})

    return HttpResponse(json.dumps(product_list, ensure_ascii=False))

def modify_ppl_data(request):
    try:
        product_code = request.GET['product_code']
    except:
        return HttpResponse(False)
    try:
        product_name = request.GET['product_name']
    except:
        product_name = ''
    try:
        product_image = request.GET['product_image']
    except:
        product_image = ''
    try:
        brand_name = request.GET['brand_name']
    except:
        brand_name = ''
    try:
        store_link = request.GET['store_link']
    except:
        store_link = ''
    try:
        price = int(request.GET['price'])
    except:
        price = ''
    try:
        start_time = int(request.GET['start_time'])
    except:
        start_time = ''
    try:
        end_time = int(request.GET['end_time'])
    except:
        end_time = ''

    product_data = Product.objects.filter(product_code=product_code)[0]
    ppl_data = PPL.objects.filter(product_code=product_code)[0]

    if is_blank(product_name) is False:
        product_data.product_name = product_name

    if is_blank(product_image) is False:
        product_data.product_image = product_image

    if is_blank(brand_name) is False:
        product_data.brand_name = brand_name

    if is_blank(store_link) is False:
        product_data.store_link = store_link

    if is_blank(price) is False:
        product_data.price = price

    if is_blank(start_time) is False:
        ppl_data.start_time = start_time

    if is_blank(end_time) is False:
        ppl_data.end_time = end_time


    product_data.save()
    ppl_data.save()
    str_json = {"drama_code": product_data.drama_code, "product_code": product_data.product_code, "product_name": product_data.product_name,
            "product_image": product_data.product_image, "brand_name": product_data.brand_name, "store_link": product_data.store_link,
            "price": product_data.price, "start_time": ppl_data.start_time, "end_time": ppl_data.end_time}

    return HttpResponse(json.dumps(str_json, ensure_ascii=False))

def is_blank(product):
    if product == '':
        return True
    else:
        return False