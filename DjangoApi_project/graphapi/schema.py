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
    product = graphene.Field(ProductType,
                             id=graphene.Int(),
                             name=graphene.String())
    all_products = graphene.List(ProductType)

    all_orders = graphene.List(OrderType)
    order = graphene.Field(OrderType,
                           id=graphene.Int(),
                           owner=graphene.String())

    all_orderitems = graphene.List(OrderItemsType)

    def resolve_all_products(self, info, **kwargs):

        return Product.objects.all()

    def resolve_all_orders(self, info, **kwargs):

        return Order.objects.all()

    def resolve_all_orderitems(self, info, **kwargs):

        return OrderItems.objects.select_related('order').all()
        # return OrderItems.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Product.objects.get(pk=id)

        if name is not None:
            return Product.objects.get(name=name)

        return None

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        owner = kwargs.get('owner')

        if id is not None:
            return Order.objects.get(pk=id)

        if name is not None:
            return Order.objects.get(owner=owner)

        return None
