from django.shortcuts import redirect, render
from django.views import View
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4
import pprint

# Create your views here.


class SSLCOMMERZ_GATEWAY(View):
    def get(self, request):
        sslcommerz_settings = {
            'store_id': settings.STORE_ID,
            'store_pass': settings.STORE_PASSWORD,
            'issandbox': True
        }
        sslcommerz = SSLCOMMERZ(sslcommerz_settings)
        post_body = {}
        post_body['total_amount'] = 10000
        post_body['currency'] = "BDT"
        post_body['tran_id'] = uuid4()
        post_body['success_url'] = "http://127.0.0.1:8000/sslcommerz/success/"
        post_body['fail_url'] = "http://127.0.0.1:8000/sslcommerz/fail/"
        post_body['cancel_url'] = "http://127.0.0.1:8000/sslcommerz/cancel/"
        post_body['emi_option'] = 0
        post_body['cus_name'] = "Customer Name"
        post_body['cus_email'] = "Customer Email"
        post_body['cus_phone'] = "Customer Phone"
        post_body['cus_add1'] = "Customer Address"
        post_body['cus_city'] = "Customer City"
        post_body['cus_country'] = "Customer Country"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 10
        post_body['product_name'] = "Product Name"
        post_body['product_category'] = "miscellaneous"
        post_body['product_profile'] = "miscellaneous"

        response = sslcommerz.createSession(post_body)
        pprint.pprint(response)

        return redirect(response["redirectGatewayURL"])

    def post(self, request):
        sslcommerz_settings = {
            'store_id': settings.STORE_ID,
            'store_pass': settings.STORE_PASSWORD,
            'issandbox': True
        }
        sslcommerz = SSLCOMMERZ(sslcommerz_settings)
        post_body = {}
        post_body['total_amount'] = 10000
        post_body['currency'] = "BDT"
        post_body['tran_id'] = uuid4()
        post_body['success_url'] = "http://127.0.0.1:8000/"
        post_body['fail_url'] = "http://127.0.0.1:8000/"
        post_body['cancel_url'] = "http://127.0.0.1:8000/"
        post_body['emi_option'] = 0
        post_body['cus_name'] = "Customer Name"
        post_body['cus_email'] = "Customer Email"
        post_body['cus_phone'] = "Customer Phone"
        post_body['cus_add1'] = "Customer Address"
        post_body['cus_city'] = "Customer City"
        post_body['cus_country'] = "Customer Country"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 10
        post_body['product_name'] = "Product Name"
        post_body['product_category'] = "miscellaneous"
        post_body['product_profile'] = "miscellaneous"

        response = sslcommerz.createSession(post_body)

        return redirect(response["redirectGatewayURL"])


class SSLCOMMERZ_PAYMENT_FAILED(View):
    @csrf_exempt
    def get(self, request):
        return redirect("students:index")


class SSLCOMMERZ_PAYMENT_CANCELLED(View):
    @csrf_exempt
    def get(self, request):
        return redirect("students:index")


class SSLCOMMERZ_PAYMENT_SUCCESS(View):
    @csrf_exempt
    def get(self, request):
        return redirect("students:index")


@csrf_exempt
def _sslcommerz_success(request):
    return redirect("students:index")


@csrf_exempt
def _sslcommerz_failed(request):
    return redirect("students:index")


@csrf_exempt
def _sslcommerz_cancel(request):
    return redirect("students:index")
