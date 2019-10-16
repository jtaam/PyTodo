from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class PortfolioApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'tam',
            'age': '33',
            'profession': 'web developer',
        }
        return Response(data)
