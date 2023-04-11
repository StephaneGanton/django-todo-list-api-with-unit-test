from turtle import update
from urllib import response
#from django.test import TestCase

from rest_framework.test import APITestCase #to test the create and list APIView (API)
from django.urls import reverse # to get an endpoint by its name
from rest_framework import status
import todos

from todos.models import Todo


class TodoAPITestCaseSetup(APITestCase):

    def createTodo(self):
        sample_todo = {'title': 'Hello', 'description': 'Test'}
        response = self.client.post(reverse("todos"), sample_todo)

        return response

    def authenticate(self):

        self.client.post(reverse("register"), {
            'username': 'user',
            'email': 'user@gmail.com',
            'password': 'password',
        })

        response = self.client.post(reverse("login"), {
            'email': 'user@gmail.com',
            'password': 'password',
        } )

        self.client.credentials(HTTP_AUTHORIZATION= f'Bearer {response.data["token"]}')


class TestListCreateTodo(TodoAPITestCaseSetup):
    # APITestCase gives us access to aclient

    def test_should_not_create_todo_with_no_auth(self):

        response = self.createTodo()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
    
        response = self.createTodo()

        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['description'], 'Test')

    def test_retrieves_all(self):
        self.authenticate()
        response = self.client.get(reverse('todos'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        sample_todo = {'title': 'Hello', 'description': 'Test'}
        self.client.post(reverse("todos"), sample_todo)
        res = self.client.get(reverse("todos"))

        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)


class TestTodoDetailAPIView(TodoAPITestCaseSetup):

    def test_retrives_one_item(self):
        self.authenticate()
        response = self.createTodo()

        res = self.client.get(reverse('todo', kwargs = { 'id': response.data['id'] }))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get( id=response.data['id'] )

        self.assertEqual(todo.title, res.data['title'])

    def test_update_one_item(self):
        self.authenticate()
        response = self.createTodo()

        res = self.client.patch(
                reverse('todo', 
                kwargs = { 'id': response.data['id'] },
            ),
            {
                # new values for updating
                'title': 'updated', 'is_complete': True
            }
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_todo = Todo.objects.get( id = response.data['id'] )

        self.assertEqual(updated_todo.is_complete, True)
        self.assertEqual(updated_todo.title, 'updated')

    def test_delete_one_item(self):
        self.authenticate()
        response = self.createTodo()

        prev_db_count = Todo.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1) # DO have in mind that the DB is considered empty each test

        res = self.client.delete(reverse('todo', 
                kwargs = { 'id': response.data['id'] }))
            
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Todo.objects.all().count(), 0 ) # 0 = prev_db_count - 1
            

