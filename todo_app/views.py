# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DeleteView, FormView

from todo_app.models import ToDoList, ToDoItem


class ListListView(ListView):
    model = ToDoList
    context_object_name = 'List all the todo lists'
    template_name = "todo_app/index.html"

    def get_context_data(self):
        context = super(ListListView, self).get_context_data()
        context["todo_lists"] = ToDoList.objects.all()
        return context

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/list-detail.html"

    def get_context_data(self):
        context = super(ItemListView, self).get_context_data()
        context["todo_list"] = ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
        context["title"] = ToDoList.objects.get(id=self.kwargs["list_id"]).title
        return context

class DeleteListView(DeleteView):
    pass

class DeleteItemView(DeleteView):
    pass

class AddListView(FormView):
    pass

class AddItemView(FormView):
    pass

class UpdateItemView(FormView):
    pass