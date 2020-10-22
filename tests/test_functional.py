from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys


class SeleniumTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.user = User.objects.create_user(username="test",
                                            first_name="test",
                                            password="password",
                                            email="test@user.fr")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('test@user.fr')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Connexion"]').click()

    def test_search_form(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        form_input = self.selenium.find_element_by_id("id_research")
        form_input.send_keys('noix de coco')
        #self.selenium.find_element_by_id('chercher').click()
        form_input.send_keys(Keys.RETURN)
