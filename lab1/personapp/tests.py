from django.test import TestCase
from rest_framework.test import APIClient
from personapp.models import Person
from rest_framework import status


class AnimalTestCase(TestCase):
    url = '/persons'

    def setUp(self):
        self.client = APIClient()
        Person.objects.create(name="Ann", age=25, address="ul Kirova", work="programmer")
        Person.objects.create(name="Kristian", age=40, address="Kirova street", work="artist")

    # get request  - get info about person  запустить
    def test_get_existed_person_info(self):
        response = self.client.get(self.url + '/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], 'Ann')
        pass

    def test_get_non_existed_person_info(self):
        response = self.client.get(self.url + '/3')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        pass


    # post request: create person info
    def test_create_correct_person(self):
        data = {
              "name": "Arny",
              "age": 13,
              "address": "adress",
              "work": "work"
             }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, None)
        pass

    def test_create_no_name_person(self):
        data = {
            "age": 13,
            "address": "adress",
            "work": "work"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        pass

    def test_create_empty_request_person(self):
        data = None
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # patch request: update
    def test_update_correct_person(self):
        data = {
            "age": 33,
            "address": "adress",
            "work": "work"
        }
        response = self.client.patch(self.url+'/1', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass

    def test_update_incorrect_index_person(self):
        data = {
            "age": 33,
            "address": "adress",
            "work": "work"
        }
        response = self.client.patch(self.url + '/13', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        pass


    def test_update_empty_body_person(self):
        data = None
        response = self.client.patch(self.url + '/13', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    # delete request
    def test_delete_correct_person(self):
        response = self.client.delete(self.url + '/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_nonexistent_person(self):
        response = self.client.delete(self.url + '/12', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


