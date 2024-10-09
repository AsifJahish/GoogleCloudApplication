# myapp/urls.py

# from django.urls import path
# from .views import ItemList

# urlpatterns = [
#     path('items/', ItemList.as_view(), name='item-list'),
#     path('api/items/', ItemList.as_view(), name='item_list_api')
# ]


# list/urls.py

from django.urls import path
from .views import ItemList, item_list_view
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', item_list_view, name='item_list'),   # Render HTML page
    path('items/', ItemList.as_view(), name='item_list_api'),  # API endpoint for GET and POST
    path('items/<int:pk>/', ItemList.as_view(), name='item_delete'),  # API endpoint for DELETE
]

