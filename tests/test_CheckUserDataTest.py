import unittest
from controllers.adm_controller import checkUserDataIsValid
from unittest import TestCase

class CheckUserDataTest(TestCase):
    def test_shouldReturnStatusCode200IfDataCorrect(self):
        res = checkUserDataIsValid("user","password")
        self.assertEqual(res,{"mensagem":'',"status_code":200})

    def test_shouldReturnErrorCodeAndMessageIfUserEmpty(self):
        res = checkUserDataIsValid("","password")
        res2 = checkUserDataIsValid(None,"password")
        self.assertEqual(res,  {"mensagem":'falta nome do usuario',"status_code":400})
        self.assertEqual(res2,  {"mensagem":'falta nome do usuario',"status_code":400})

    def test_shouldReturnErrorCodeAndMessageIfPasswordEmpty(self):
        res = checkUserDataIsValid("user","")
        res2 = checkUserDataIsValid("user",None)
        self.assertEqual(res, {"mensagem":'falta senha do usuario',"status_code":400})
        self.assertEqual(res2, {"mensagem":'falta senha do usuario',"status_code":400})


if __name__ == '__main__':
    unittest.main()
