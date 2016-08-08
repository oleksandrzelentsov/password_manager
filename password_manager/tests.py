from tempfile import mkdtemp
import unittest
import os
import subprocess

from password_manager.password_manager import PasswordManager as PManager


database_count = 1


class PasswordManagerUnitTest(unittest.TestCase):

    def create_manager(self, filename_wo_ext):
        return PManager(os.path.join(self.tmpdir,
                                     '{}.sqlite'.format(filename_wo_ext)))

    def setUp(self):
        self.tmpdir = mkdtemp()
        self.pms = []
        for i in range(database_count):
            self.pms.append(self.create_manager(str(i)))

    def tearDown(self):
        subprocess.call(['rm', '-Rf', self.tmpdir])

    def test_empty_tables_on_db_create(self):
        pm = self.pms.pop()
        self.assertTrue(len(pm.passwords()) == 0)
        self.assertTrue(len(pm.services()) == 0)

    def test_password_add(self):
        pm = self.pms.pop()
        empty_passwords = lambda: len(pm.passwords()) == 0
        self.assertTrue(empty_passwords())
        pm.add_password(password_login='hello', password='world')
        self.assertFalse(empty_passwords())

    def test_password_remove(self):
        pm = self.pms.pop()
        empty_passwords = lambda: len(pm.passwords()) == 0
        pm.add_password(password_login='hello', password='world')
        self.assertFalse(empty_passwords())
        pm.remove_password(pm.passwords()[0].password_id)
        self.assertTrue(empty_passwords())

    def test_service_add(self):
        pm = self.pms.pop()
        empty_services = lambda: len(pm.services()) == 0
        self.assertTrue(empty_services())
        pm.add_service(service_name='hello')
        self.assertFalse(empty_services())

    def test_service_remove(self):
        pm = self.pms.pop()
        empty_services = lambda: len(pm.services()) == 0
        pm.add_service(service_name='hello')
        self.assertFalse(empty_services())
        pm.remove_service(pm.services()[0].service_id)
        self.assertTrue(empty_services())

