# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, FormView, CreateView, UpdateView

from todo_app.forms import ListForm, ItemForm
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
        context["todo_list_id"] = self.kwargs["list_id"]
        context["title"] = ToDoList.objects.get(id=self.kwargs["list_id"]).title
        return context

class DeleteListView(DeleteView):
    pass

class DeleteItemView(DeleteView):
    pass

class ListAddView(CreateView):
    form_class = ListForm
    template_name = "todo_app/add_list.html"
    success_url = reverse_lazy("list-view")

class ItemAddView(CreateView):
    form_class = ItemForm
    template_name = "todo_app/add_item.html"

    def get_context_data(self):
        context = super(ItemAddView, self).get_context_data()
        context["title"] = ToDoList.objects.get(id=self.kwargs["list_id"]).title
        return context

    def get_success_url(self):
        return reverse_lazy("item-view", args=[self.kwargs["list_id"]])

class ItemUpdateView(UpdateView):
    form_class = ItemForm
    template_name = "todo_app/update_item.html"

    def get_context_data(self):
        context = super(ItemUpdateView, self).get_context_data()
        context["title"] = ToDoList.objects.get(id=self.kwargs["list_id"]).title
        context["task_title"] = ToDoItem.objects.get(id=self.kwargs["pk"]).title
        return context

    def get_success_url(self):
        return reverse_lazy("item-view", args=[self.kwargs["list_id"]])

    def get_queryset(self):
        return ToDoItem.objects.all()