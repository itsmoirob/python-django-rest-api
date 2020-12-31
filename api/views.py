from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
        'Detail': '/task-detail/<str:pk>',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }

    return Response(api_urls)
