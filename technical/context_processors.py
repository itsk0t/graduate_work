from products.models import Category
from technical.models import UserAddress


def header_menu(request):
    return {'category_menu': Category.objects.all()}


# def header_city(request):
#     if user.is_active:
#         return {'header_city': UserAddress.objects.filter(user_id=request.user)}
#     else:
#         pass

