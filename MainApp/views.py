from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

author = {
   "name": "Иван",
   "middlename": "Петрович",
   "lastname": "Иванов",
   "phone": "8-923-600-01-02",
   "email": "vasya@mail.ru",
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
   #text = """ <h1> "Изучаем django День первый" </h1>
   #           <strong> Автор </strong>: <i> Иванов И.П. </i> """
   #return HttpResponse(text)
   context = {
      "name": 'Петров Николай Иванович',
      "email": "my_mail@mail.ru",
   }
   return render(request, "index.html", context)



def about(request):
   result = f"""
      Имя: <b>{author["name"]}</b><br>
      Отчество: <b>{author["middlename"]}</b><br>
      Фамилия: <b>{author["lastname"]}</b><br>
      телефон: <b>{author["phone"]}</b><br>
      email: <b>{author["email"]}</b>
      """
   return HttpResponse(result)


# url /item/1
# url /item/2
def get_item(request, id):
   for item in items:
      if int(item["id"]) == id:
         # result = f"""
         #          <h1>Название: {item["name"]}</h1>
         #          <p>количество : {item["quantity"]}</p>
         #          <a href='/items'> Назад </a>
         #          """
         # return HttpResponse(result)
         context = {
            'item': item
         }
         return render(request, "item-page.html", context)
   return HttpResponseNotFound(f"Item with id={id} not found")

def items_list(request):
   # result = "<h2> Список товаров</h2><ol>"
   # for item in items:
   #    result += f"<li><a href='/item/{item['id']}'>Название: {item['name']}</a></li>"
   # result += "</ol>"
   context = {
      "items": items
   }
   return render(request, "items-list.html", context)
