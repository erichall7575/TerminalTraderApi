import unittest
from schema import create_db
from seed import seed
import os
from app import Account,Trade,Position
from app.orm import ORM

ORM.database='_test.db'

class TestAccount(unittest.TestCase):
    def setUp(self):
        create_db('_test.db')
        seed('_test.db')
    
    def tearDown(self):
        os.remove('_test.db')

    def testApiAuthenticate(self):
        eric=Account.api_authenticate('000000000000')
        self.assertIsInstance(eric,Account,"api key loads account")
