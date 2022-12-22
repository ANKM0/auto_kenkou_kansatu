from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class UiTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        cls.live_server_url = "http://127.0.0.1:8000/"
        cls.driver.get(cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        # adminにログイン
        cls.driver.get(cls.live_server_url + "admin/users/userinfo/")
        cls.driver.execute_script('document.getElementById("id_username").value="xings";')
        cls.driver.execute_script('document.getElementById("id_password").value="gllilwe9d9f16";')
        cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input'))
        # user_infoを削除
        cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a'))
        cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="userinfo_form"]/div/div/p/a'))
        cls.driver.execute_script('arguments[0].click();', cls.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/input[2]'))

        cls.driver.quit()
        super().tearDownClass()

    def test_is_enter(self) -> None:
        """ユーザがサイトに入れることをテスト"""
        # ユーザがサイトを訪問する
        self.assertIn("AUTO KENKO KANSATSU", self.driver.title)

    def test_is_capable_rogin(self) -> None:
        """ユーザがログインできることをテスト"""
        # ユーザが簡単ログインからログインする
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"簡単ログイン")]'))
        # self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/div/div/div[2]/button/a'))
        self.assertEqual(self.live_server_url, self.driver.current_url)
        # ログイン出来ていることを確認
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="navbarNav4"]/ul/li[2]/a').text, 'ログアウト')

    def test_is_not_have_data_user(self) -> None:
        """まだデータを登録していないログインユーザがデータを登録できることをテスト"""
        # データ登録ボタンを押すと createページに遷移
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ登録")]'))
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}create/')

        # ユーザが情報を登録する
        self.driver.execute_script('document.getElementById("id_user_info_class_number").value=1;')
        self.driver.execute_script('document.getElementById("id_user_info_student_number").value=2;')
        self.driver.execute_script('document.getElementById("id_user_info_student_name").value="test_user";')
        self.driver.execute_script('document.getElementById("id_user_info_body_temperature").value=36.5;')
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"登録する")]'))

        # ユーザが情報を登録できたことを確認
        self.assertEqual(self.driver.current_url, self.live_server_url)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]').text, 'データ確認')

        """ホームページからデータを確認できることをテスト"""
        # ユーザがデータを確認する
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p').text, "1")
        # 戻るボタンをクリック
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"戻る")]'))
        self.assertEqual(self.driver.current_url, self.live_server_url)

        """ホームページからデータを更新できることをテスト"""
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ更新")]'))
        self.assertRegex(self.driver.current_url, r'/update/[0-9]')
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')

        """ユーザ情報ページからデータを更新できることをテスト"""
        # ユーザが更新ボタンをクリック
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"ユーザー情報更新")]'))

        # ユーザが情報を更新する
        select_user_info_grade_number = Select(self.driver.find_element(By.XPATH, '//*[@id="id_user_info_grade_number"]'))
        select_user_info_grade_number.select_by_value("1")
        self.driver.execute_script('document.getElementById("id_user_info_class_number").value=2;')
        self.driver.execute_script('document.getElementById("id_user_info_student_number").value=3;')
        self.driver.execute_script('document.getElementById("id_user_info_student_name").value="updated_user";')
        self.driver.execute_script('document.getElementById("id_user_info_body_temperature").value=35;')
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))

        # データが登録されたことを確認
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p').text, "2")

        """ログアウトできることを確認"""
        # ログアウトボタンをクリック
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"ログアウト")]'))
        # ログアウトできることを確認
        self.assertEqual(self.driver.current_url, self.live_server_url)
