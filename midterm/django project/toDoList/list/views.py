from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


from django.shortcuts import render
from django.template.context_processors import csrf



class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        # Expecting the item ID in the URL to delete
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def item_list_view(request):
    context = {}
    context.update(csrf(request))  # Add CSRF token to the context
    # return render(request, 'item_list.html'

    return render(request, '/home/asifjahish/vscode/web development/Cloud Application/GoogleCloudApplication/midterm/django project/toDoList/list/templates/item_list.html', context)