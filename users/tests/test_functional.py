from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class IsCapableRoginTest(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.live_server_url = 'http://localhost:8000/'
        self.driver.get(self.live_server_url)

    def test_is_enter(self):
        """ユーザがサイトに入れることをテスト"""
        # ユーザがサイトを訪問する
        self.assertIn("AUTO KENKO KANSATSU", self.driver.title)

    def test_is_capable_rogin(self):
        """ユーザがログインできることをテスト"""
        # ユーザが簡単ログインからログインする
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"簡単ログイン")]'))
        # ログイン出来ていることを確認
        self.assertEqual(self.driver.find_element(By.XPATH, '//a[contains(text(),"ログアウト")]').text, 'ログアウト')

    def tearDown(self):
        self.driver.quit()


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.live_server_url = 'http://localhost:8000'

        self.driver.get(self.live_server_url)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"簡単ログイン")]'))

    def tearDown(self):
        # adminにログイン
        self.driver.get(f"{self.live_server_url}/admin/users/userinfo/")
        self.driver.execute_script('document.getElementById("id_username").value="xings";')
        self.driver.execute_script('document.getElementById("id_password").value="gllilwe9d9f16";')
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input'))
        # user_infoを削除
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a'))
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[@id="userinfo_form"]/div/div/p/a'))
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/input[2]'))
        # ログアウト
        self.driver.get(f"{self.live_server_url}/")
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[@id="navbarNav4"]/ul/li[2]/a'))

        self.driver.quit()

    def test_is_not_have_data_user(self):
        """まだデータを登録していないログインユーザがデータを登録できることをテスト"""
        # データ登録ボタンを押すと createページに遷移
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ登録")]'))
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/create/')

        # ユーザが情報を登録する
        self.driver.execute_script('document.getElementById("id_user_info_class_number").value=1;')
        self.driver.execute_script('document.getElementById("id_user_info_student_number").value=2;')
        self.driver.execute_script('document.getElementById("id_user_info_student_name").value="test_user";')
        self.driver.execute_script('document.getElementById("id_user_info_body_temperature").value=36.5;')
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"登録する")]'))

        # ユーザが情報を登録できたことを確認
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/')
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]').text, 'データ確認')

        """ホームページからデータを確認できることをテスト"""
        # ユーザがデータを確認する
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))
        self.assertRegex(self.driver.current_url, r'/detail/[0-9]')
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p').text, "1")
        # 戻るボタンをクリック
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, '//*[contains(text(),"戻る")]'))
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/')

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
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/')
