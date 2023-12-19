import unittest
from main import app, db, User

class UserTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jorlyn95@192.168.1.9/bnka'
        self.app = app.test_client()

        with app.app_context():
            db.create_all()


    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        with app.app_context():
            response = self.app.post('/create_user', json={'username': 'testuser', 'email': 'test@example.com'})
            self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        # Asumiendo que hay un usuario en la base de datos
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            db.session.add(user)
            db.session.commit()

            response = self.app.get('/get_user/1')
            self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        # Asumiendo que hay un usuario en la base de datos
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            db.session.add(user)
            db.session.commit()

            response = self.app.put('/update_user/1', json={'username': 'newusername'})
            self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        # Asumiendo que hay un usuario en la base de datos
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            db.session.add(user)
            db.session.commit()

            response = self.app.delete('/delete_user/1')
            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
