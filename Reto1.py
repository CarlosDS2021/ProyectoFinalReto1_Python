import sys
import unittest
import time


from selenium import webdriver

class TestReto1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_reto1(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        time.sleep(2)


        start_button = driver.find_element_by_xpath("//button[contains(text(),'Start')]")
        time.sleep(1)
        start_button.click()
        time.sleep(1)

        name = ("Jhon", "Jane", "Albert", "Michael", "Doug", "Jessie", "Stan", "Michelle", "Stacy", "Lara")
        n = iter(name)
            
        rol = ("Analyst", "Medical Engineer", "Accountant", "IT Specialist", "Analyst", "Scientist", "Advisor", "Scientist", "HR Manager", "Programmer")
        r = iter(rol)

        cel = ("40716543298", "40791345621", "40735416854", "40733652145", "40799885412", "40733154268", "40712462257", "40731254562", "40741785214", "40731653845")
        c = iter(cel)

        dir = ("98 North Road", "11 Crown Street", "22 Guild Street", "17 Farburn Terrace", "99 Shire Oak Road","27 Cheshire Street", "10 Dam Road", "13 White Rabbit Street", "19 Pineapple Boulevard","87 Orange Street")
        d = iter(dir)

        cor = ("jsmith@itsolutions.co.uk", "jdorsey@mc.com", "kipling@waterfront.com", "mrobertson@mc.com","dderrick@timepath.co.uk", "jmarlowe@aperture.us", "shamm@sugarwell.org", "mnorton@aperture.us","sshelby@techdev.com", "lpalmer@timepath.co.uk")
        e = iter(cor)

        ape = ("Smith", "Dorsey", "Kipling", "Robertson", "Derrick", "Marlowe", "Hamm", "Norton", "Shelby", "Palmer")
        p = iter(ape)

        com = ("IT Solutions", "MediCare", "Waterfront", "MediCare", "Timepath Inc.", "Aperture Inc.", "Sugarwell", "Aperture Inc.", "TechDev", "Timepath Inc.")
        y = iter(com)

        for a in range(10):
            firstName_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelFirstName']")
            firstName_text.send_keys(next(n))

            roleInCompany_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelRole']")
            roleInCompany_text.send_keys(next(r))

            phoneNumber_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelPhone']")
            phoneNumber_text.send_keys(next(c))

            addres_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelAddress']")
            addres_text.send_keys(next(d))

            email_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelEmail']")
            email_text.send_keys(next(e))

            lastName_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelLastName']")
            lastName_text.send_keys(next(p))

            companyName_text = driver.find_element_by_css_selector("input[ng-reflect-name='labelCompanyName']")
            companyName_text.send_keys(next(y))

            submit_button = driver.find_element_by_xpath("/html[1]/body[1]/app-root[1]/div[2]/app-rpa1[1]/div[1]/div[2]/form[1]/input[1]")
            time.sleep(1)
            submit_button.click()


        text_output = driver.find_element_by_css_selector("div.body.row1.scroll-y app-rpa1:nth-child(2) div.row.parent div.congratulations.col.s8.m8.l8 > div.message2")
        time.sleep(1)

        resultado = text_output.text.split()

        valor = resultado[4].rstrip(resultado[4][-1])


        if int(float(valor)) > 90:
            assert int(float(valor)) > 90
        else:
            raise ValueError('El % es menor ó igual 90')


if __name__ == '__main__':
    unittest.main()
