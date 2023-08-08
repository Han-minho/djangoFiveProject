from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        """
            장바구니를 초기화합니다
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # 세션에 빈바구니를 저장합니다.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


