from selenium import webdriver
import unittest

class HolaMundoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Asegúrate de tener el driver correcto instalado

    def test_hola_mundo(self):
        self.driver.get("file:///path/a/tu/proyecto/index.html")
        self.assertIn("Hola Mundo", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()