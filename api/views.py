from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {
    "name": "Toast",
    "description": "A totally toast NFT!",
    "image": "https://www.webcryptobit.com/nft/doge.jpg",
    "attributes": [
        {
            "trait_type": "cuteness",
            "value": 10
        }
    ]
    }
    return Response(person)
