import graphene

import graphapi.schema


class Query(graphapi.schema.Query, graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query)
