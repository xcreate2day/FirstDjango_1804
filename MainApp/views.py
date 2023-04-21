from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item
# Create your views here.


def home(request):
   #text = """ """
   #return HttpResponse(text)
   context = {
      "name": 'Петров Николай Иванович',
      "email": "my_mail@mail.ru",
   }
   return render(request, "index.html", context)



def about(request):
   author = {
      "name": "Иван",
      "middlename": "Петрович",
      "lastname": "Иванов",
      "phone": "8-923-600-01-02",
      "email": "vasya@mail.ru",
   }
   result = f"""
      Имя: <b>{author["name"]}</b><br>
      Отчество: <b>{author["middlename"]}</b><br>
      Фамилия: <b>{author["lastname"]}</b><br>
      телефон: <b>{author["phone"]}</b><br>
      email: <b>{author["email"]}</b><br>
      <a href="/">Home</a>
      """
   return HttpResponse(result)


# url /item/1
# url /item/2
def get_item(request, id):
   try:
      item = Item.objects.get(id=id)
   except ObjectDoesNotExist:
      return HttpResponseNotFound(f'Объект с id={id} не найден')
   else:
      context = {
         'item': item
      }
      return render(request, "item-page.html", context)
   #return HttpResponseNotFound(f"Item with id={id} not found")

def items_list(request):
   items = Item.objects.all()
   context = {
      "items": items
   }
   return render(request, "items-list.html", context)
