# shopping_list/api/viewsets.py
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet


from shopping_list.api.serializer import ShoppiItemSerializer
from shopping_list.models import ShoppingItems

class ShoppingItemsViewSet (ModelViewSet):
    queryset= ShoppingItems.objects.all()
    serializer_class = ShoppiItemSerializer
    # If you, for some reason, want only one view to be rendered as JSON, you can set it in renderer_classes inside the view.
    # renderer_classes = [JSONRenderer]

    # Delete Many
    @action(detail=False, methods=['DELETE'], url_path='delete_all_purchased', url_name='delete_all_purchased')
    def delete_purchased(self, request):
        ShoppingItems.objects.filter(purchased=True).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Mark all items 'purchased' AKA: Update Many
    @action(detail=False, methods=['PATCH'], url_path='mark_bulk_purchased', url_name='mark_bulk_purchased')
    def mark_bulk_purchased(self, request):
        try:
            queryset = ShoppingItems.objects.filter(id__in=request.data['shopping_items'])
            queryset.update(purchased=True)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)