# Done by Carlos amaral (2020/11/24)

from django.contrib.auth import  get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.todo = Todo.objects.create(
            title='A good title',
            description='Nice body content',
            created='2020-11-24',
            due_date='2020-11-25',
        )

    def test_string_representation(self):
        todo = Todo(title='A sample title')
        self.assertEqual(str(todo), todo.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.todo.get_absolute_url(), '/todo/1/')


    def test_todo_content(self):
        self.assertEqual(f'{self.todo.title}', 'A good title')
        self.assertEqual(f'{self.todo.description}', 'Nice body content')
        self.assertEqual(f'{self.todo.created}', '2020-11-24')
        self.assertEqual(f'{self.todo.due_date}', '2020-11-25')

    def test_todo_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_todo_detail_view(self):
        response = self.client.get('/todo/1/')
        no_response = self.client.get('/todo/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_new'), {
            'title': 'New title',
            'body': 'New text',
            'created': '2020-11-24',
            'due_date': '2020-11-25',
            'check': 'yes',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_edit', args='1'),{
            'title': 'Updated title',
            'body': 'Updated body',
            'created': '2020-11-23',
            'due_date': '2020-11-26',
            'check': 'no',
        })

    def test_todo_delete_view(self):
        response = self.client.get(
            reverse('todo_delete', args='1'))
        self.assertEqual(response.status_code, 200)
