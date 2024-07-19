import unittest
from qrgen import create_qr

class TestCreateQR(unittest.TestCase):
    def test_create_qr(self):
        account = "UA683052990000026004026814882"
        edrpo = "44327069"
        recipient = "ОСББ ТРИПІЛЛЯ-ПАТРІОТИКА"
        amount = "UAH3000.00"
        purpose = "Добровільний внесок на генератор, квартира XXX"
        test_url = "https://bank.gov.ua/qr/QkNCCjAwMgoxClVDVAoK0J7QodCR0JEg0KLQoNCY0J_QhtCb0JvQry3Qn9CQ0KLQoNCG0J7QotCY0JrQkApVQTY4MzA1Mjk5MDAwMDAyNjAwNDAyNjgxNDg4MgpVQUgzMDAwLjAwCjQ0MzI3MDY5CgoK0JTQvtCx0YDQvtCy0ZbQu9GM0L3QuNC5INCy0L3QtdGB0L7QuiDQvdCwINCz0LXQvdC10YDQsNGC0L7RgCwg0LrQstCw0YDRgtC40YDQsCBYWFgK"

        # Call the function
        url = create_qr(account, edrpo, recipient, amount, purpose)

        # Assert that the QR code is generated successfully
        self.assertEqual(url, test_url)

        # You can add additional assertions here if needed
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()