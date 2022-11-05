from django.contrib.auth.models import User
from django.test import TestCase

# models test
from todo_app.models import ToDoList


class ToDoListTest(TestCase):

    def create_todolist(self, title="only a test"):
        user = User.objects.create_user(username='testuser', password='password')
        return ToDoList.objects.create(user=user, title=title)

    def test_todolist_creation(self):
        w = self.create_todolist()
        self.assertTrue(isinstance(w, ToDoList))
        self.assertEqual(w.__str__(), w.title)
