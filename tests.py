
# tests.py
import unittest
import os
import json
from app import create_app, db

class CommentingTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.comment_category = {'comment_category': 'Finance_department'}
        self.comment_object = {'category_id': 11, 'object_type': 'staff'}
        self.comment = {'comment': 'I called the client, he said i should call back.', 'category_id': 1, 'object_id': 1}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_comment_category_creation(self):
        """Test API can create a comment category (POST request)"""
        res = self.client().post('/comment_category', data=self.comment_category)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Finance_department', str(res.data))

    def test_api_can_get_all_comment_category(self):
        """Test API can get a bucketlist (GET request)."""
        res = self.client().post('/comment_category', data=self.comment_category)
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/comment_category')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Finance_department', str(res.data))

    def test_object_type_creation(self):
        """Test API can create an Object type creation (POST request)"""
        res = self.client().post('/comment_object', data=self.comment_object)
        self.assertEqual(res.status_code, 201)
        self.assertIn('staff', str(res.data))

    def test_api_can_get_all_comment_object(self):
        """Test API can get a comment_object (GET request)."""
        res = self.client().post('/comment_object', data=self.comment_object)
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/comment_object')
        self.assertEqual(res.status_code, 200)
        self.assertIn('staff', str(res.data))

    def test_comment_creation(self):
        """Test API can create a comment (POST request)"""
        res = self.client().post('/comment', data=self.comment)
        self.assertEqual(res.status_code, 201)
        self.assertIn('I called the client, he said i should call back.', str(res.data))

    def test_api_can_get_all_comment(self):
        """Test API can get comments (GET request)."""

        res = self.client().post('/comment', data=self.comment)
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/comment')
        self.assertEqual(res.status_code, 200)
        self.assertIn('I called the client', str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()