from unittest import TestCase, main as unittest_main
from app import app

from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId

sample_hoodie_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_hoodie = {
    'title': 'Yeah',
    'description': 'The best!'
}
sample_form_data = {
    'title': sample_hoodie['title'],
    'description': sample_hoodie['description'],
}

class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    def test_index(self):
        """Test the homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoody.', result.data)
        
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_hoodie(self, mock_find):
        """Test showing a single hoodie."""
        mock_find.return_value = sample_hoodie

        result = self.client.get(f'/hoodies/{sample_hoodie_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Yeah', result.data)
        
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_hoodie(self, mock_find):
        """Test editing a single hoodie."""
        mock_find.return_value = sample_hoodie

        result = self.client.get(f'/hoodies/{sample_hoodie_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoody.', result.data)
        
    # @mock.patch('pymongo.collection.Collection.delete_one')
    # def test_delete_hoodie(self, mock_delete):
    #     form_data = {'_method': 'DELETE'}
    #     result = self.client.post(f'/hoodies/{sample_hoodie_id}/delete', data=form_data)
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_delete.assert_called_with({'_id': sample_hoodie_id})

if __name__ == '__main__':
    unittest_main()