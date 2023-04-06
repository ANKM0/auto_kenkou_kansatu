from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def click_by_execute_script(driver: WebDriver, wait_time: int, kind_of_selctor: str = "XPATH", location_name: str = "") -> None:
    """
    execute_scriptで要素をクリックする関数

    Args:
        driver (webdriver): webdriverオブジェクト
        wait_time (int, optional): 待機する秒数. Defaults to 30.
        kind_of_selctor (str, optional): 対象要素を何を使って指定するか. Defaults to "XPATH".
        location_name (str, optional): 要素のxpath,id,name...etc. Defaults to "".
    """
    # element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[1]/div[1]/h2')))
    element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((getattr(By, f"{kind_of_selctor}"), location_name)))
    driver.execute_script("arguments[0].click();", element)


class UiTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15')
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.live_server_url = "http://127.0.0.1:8000/"
        cls.driver.get(cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        wait_time = 30

        # adminにログイン
        cls.driver.get(cls.live_server_url + "admin/users/userinfo/")
        cls.driver.execute_script('document.getElementById("id_username").value="xings";')
        cls.driver.execute_script('document.getElementById("id_password").value="gllilwe9d9f16";')
        # cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input'))
        click_by_execute_script(cls.driver, wait_time, "XPATH", '//*[@id="login-form"]/div[3]/input')


        # user_infoを削除
        # cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a'))
        # cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="userinfo_form"]/div/div/p/a'))
        # cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/input[2]'))
        click_by_execute_script(cls.driver, wait_time, "XPATH", '//*[@id="result_list"]/tbody/tr/th/a')
        click_by_execute_script(cls.driver, wait_time, "XPATH", '//*[@id="userinfo_form"]/div/div/p/a')
        click_by_execute_script(cls.driver, wait_time, "XPATH", '//*[@id="content"]/form/div/input[2]')

        cls.driver.quit()
        super().tearDownClass()

        # cls.driver.execute_script('arguments[0].click();', WebDriverWait(cls.driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'データ登録'))))
        click_by_execute_script(cls.driver, wait_time, "PARTIAL_LINK_TEXT", 'データ登録')


    def test_is_enter(self) -> None:
        """ユーザがサイトに入れることをテスト"""
        # ユーザがサイトを訪問する
        self.assertIn("AUTO KENKO KANSATSU", self.driver.title)

    def test_is_capable_rogin(self) -> None:
        """ユーザがログインできることをテスト"""
        wait_time = 30
        # ユーザが簡単ログインからログインする
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"簡単ログイン")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", '簡単ログイン')
        self.assertEqual(self.live_server_url, self.driver.current_url)
        # ログイン出来ていることを確認
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="navbarNav4"]/ul/li[2]/a').text, 'ログアウト')

    def test_is_not_have_data_user(self) -> None:
        """まだデータを登録していないログインユーザがデータを登録できることをテスト"""
        wait_time = 30
        # データ登録ボタンを押すと createページに遷移
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ登録")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", 'データ登録')
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}create/')

        # ユーザが情報を登録する
        self.driver.execute_script('document.getElementById("id_user_info_class_number").value=1;')
        self.driver.execute_script('document.getElementById("id_user_info_student_number").value=2;')
        self.driver.execute_script('document.getElementById("id_user_info_student_name").value="test_user";')
        self.driver.execute_script('document.getElementById("id_user_info_body_temperature").value=36.5;')
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"登録する")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", '登録する')

        # ユーザが情報を登録できたことを確認
        self.assertEqual(self.driver.current_url, self.live_server_url)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]').text, 'データ確認')

        """ホームページからデータを確認できることをテスト"""
        # ユーザがデータを確認する
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", 'データ確認')
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p').text, "1")
        # 戻るボタンをクリック
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"戻る")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", '戻る')
        self.assertEqual(self.driver.current_url, self.live_server_url)

        """ホームページからデータを更新できることをテスト"""
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ更新")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", 'データ更新')

        self.assertRegex(self.driver.current_url, r'/update/[0-9]')
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", '更新する')
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')

        """ユーザ情報ページからデータを更新できることをテスト"""
        # ユーザが更新ボタンをクリック
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"ユーザー情報更新")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", 'ユーザー情報更新')

        # ユーザが情報を更新する
        select_user_info_grade_number = Select(self.driver.find_element(By.XPATH, '//*[@id="id_user_info_grade_number"]'))
        select_user_info_grade_number.select_by_value("1")
        self.driver.execute_script('document.getElementById("id_user_info_class_number").value=2;')
        self.driver.execute_script('document.getElementById("id_user_info_student_number").value=3;')
        self.driver.execute_script('document.getElementById("id_user_info_student_name").value="updated_user";')
        self.driver.execute_script('document.getElementById("id_user_info_body_temperature").value=35;')
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", '更新する')


        # データが登録されたことを確認
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p').text, "2")

        """ログアウトできることを確認"""
        # ログアウトボタンをクリック
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"ログアウト")]'))
        click_by_execute_script(self.driver, wait_time, "LINK_TEXT", 'ログアウト')

        # ログアウトできることを確認
        self.assertEqual(self.driver.current_url, self.live_server_url)
