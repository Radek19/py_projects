import graphene

from graphene_django.types import DjangoObjectType

from shop.models import Product
from orders.models import Order, OrderItems


class ProductType(DjangoObjectType):

    class Meta:
        model = Product


class OrderType(DjangoObjectType):

    class Meta:
        model = Order


class OrderItemsType(DjangoObjectType):

    class Meta:
        model = OrderItems


class Query(object):
    all_products = graphene.List(ProductType)
    all_orders = graphene.List(OrderType)
    all_orderitems = graphene.List(OrderItemsType)

    def resolve_all_products(self, info, **kwargs):

        return Product.objects.all()

    def resolve_all_orders(self, info, **kwargs):

        return Order.objects.all()

    def resolve_all_orderitems(self, info, **kwargs):

        return OrderItems.objects.select_related('order').all()
        # return OrderItems.objects.all()
