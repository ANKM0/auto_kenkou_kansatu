from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class NewVisitorTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_is_enter(self):
        """ユーザがサイトに入れることをテスト"""
        # ユーザがサイトを訪問する
        self.browser.get("http://localhost:8000")

        # 彼はtitleやheaderに『To-Do』と書いてあるためこのサイトが
        # To-Doサイトで間違いないことを確認する
        self.assertIn("AUTO KENKO KANSATSU", self.browser.title)

    def test_is_capable_rogin(self):
        """ユーザがログインできることをテスト"""
        # ユーザが簡単ログインからログインする
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"簡単ログイン")]'))

        # ログイン出来ていることを確認
        self.assertEqual(self.browser.find_element(By.XPATH, '//*a[contains(text(),"ログアウト")]').text, 'ログアウト')

    def test_is_not_have_data_user_make_data(self):
        """まだデータを登録していないログインユーザがデータを登録できることをテスト"""
        # データ登録ボタンを押すと createページに遷移
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"データ登録")]'))
        self.assertEqual(self.browser.current_url, '/create/')

        # ユーザが情報を登録する
        self.browser.execute_script('document.getElementById("id_user_info_class_number").value=1;')
        self.browser.execute_script('document.getElementById("id_user_info_student_number").value=2;')
        self.browser.execute_script('document.getElementById("id_user_info_student_name").value="test_user";')
        self.browser.execute_script('document.getElementById("id_user_info_body_temperature").value=36.5;')
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))

        # ユーザが情報を登録できたことを確認
        self.assertEqual(self.browser.current_url, '/')
        self.assertEqual(self.browser.find_element(By.XPATH, '//*a[contains(text(),"データ確認")]').text, 'データ確認')

    def test_visit_detail_from_homepage(self):
        """ホームページからデータを確認できることをテスト"""
        # ユーザがデータを確認する
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))

        self.assertRegex(self.browser.current_url, r'/detail/[0-9]')
        self.assertRegex(self.browser.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p'), r'[0-9]')

        # 戻るボタンをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"戻る")]'))
        self.assertEqual(self.browser.current_url, '/')

    def test_visit_update_from_homepage(self):
        """ホームページからデータを更新できることをテスト"""
        # ユーザがデータを確認する
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))

        self.assertRegex(self.browser.current_url, r'/detail/[0-9]')
        self.assertRegex(self.browser.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p'), r'[0-9]')

    def test_visit_update_from_detail(self):
        """ユーザ情報ページからデータを更新できることをテスト"""
        # ユーザが更新ボタンをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"データ確認")]'))

        # ユーザが情報を更新する
        select_user_info_grade_number = Select(self.browser.find_element(By.XPATH, 'id_user_info_grade_number'))
        select_user_info_grade_number.select_by_value("1")
        self.browser.execute_script('document.getElementById("id_user_info_class_number").value=2;')
        self.browser.execute_script('document.getElementById("id_user_info_student_number").value=3;')
        self.browser.execute_script('document.getElementById("id_user_info_student_name").value="updated_user";')
        self.browser.execute_script('document.getElementById("id_user_info_body_temperature").value=35;')
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"更新する")]'))

        # データが登録されたことを確認
        self.assertRegex(self.browser.current_url, r'/detail/[0-9]')
        self.assertRegex(self.browser.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/p'), r'[0-9]')

    def test_is_capable_rogout(self):
        """ログアウトできることを確認"""
        # ログアウトボタンをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"ログアウト")]'))
        self.assertEqual(self.browser.current_url, '/logout_safety/')

        # ホームページに戻るボタンをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"ホームページ")]'))
        # ログアウトをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"ログアウト")]'))
        # safetyページでログアウトをクリック
        self.browser.execute_script('arguments[0].click();', self.browser.find_element(By.XPATH, '//*[contains(text(),"ログアウト")]'))

        self.assertEqual(self.browser.current_url, '/')
