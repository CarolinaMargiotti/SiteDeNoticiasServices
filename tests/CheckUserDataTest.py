import unittest
from controllers.adm_controller import checkUserDataIsValid
from unittest import TestCase

class CheckUserDataTest(TestCase):
    def test_shouldReturnStatusCode200IfDataCorrect(self):
        res = checkUserDataIsValid("user","password")
        self.assertEqual(res.status_code, 200)

    def test_shouldReturnRightStatusCodeAndMessageIfUserEmpty(self):
        res = checkUserDataIsValid("","password")
        res2 = checkUserDataIsValid(None,"password")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json.mensagem, '')
        self.assertEqual(res2.status_code, 400)
        self.assertEqual(res2.json.mensagem, '')

    def test_shouldReturnRightStatusCodeAndMessageIfPasswordEmpty(self):
        res = checkUserDataIsValid("user","")
        res2 = checkUserDataIsValid("user",None)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json.mensagem, '')
        self.assertEqual(res2.status_code, 400)
        self.assertEqual(res2.json.mensagem, '')


if __name__ == '__main__':
    unittest.main()
