# https://forms.office.com/Pages/ResponsePage.aspx?id=skPpVutfMUa0cQNGQMsYbGpXnkvNOxxPlw82yuB56QdURUZTVVFIRkZWTkRBUEhUTktMSk84M1RFQS4u&qrcode=true

import datetime
import requests
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from sqlite_module import LocalCache

from typing import Any


def enter_kekou_kansatu(wait: WebDriverWait, class_number: int, student_number: int, student_name: str, body_temperature: int) -> None:
    """
    フォームに入力
    """
    # 入力欄をクリック
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input[1]")))
    search_box.click()
    # 今日の日付ボタンをクリック
    picker_button_today = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[1]")))
    picker_button_today.click()
    # クラス欄をクリック
    select_placeholder_class_number = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div")))
    select_placeholder_class_number.click()
    # クラス入力
    class_number_xpath = f"/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[{class_number}]"
    enter_name = wait.until(EC.element_to_be_clickable((By.XPATH, class_number_xpath)))
    enter_name.click()
    # 出席番号欄をクリック
    select_placeholder_student_number = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div")))
    select_placeholder_student_number.click()
    # 出席番号入力
    student_number_xpath = f"/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[{student_number}]"
    enter_student_number = wait.until(EC.element_to_be_clickable((By.XPATH, student_number_xpath)))
    enter_student_number.click()
    # 名前入力
    name_enter = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div/input")))
    name_enter.click()
    name_enter.send_keys(student_name)
    # 体温入力
    enter_body_temperature = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div/input")))
    enter_body_temperature.click()
    enter_body_temperature.send_keys(body_temperature)
    # 症状入力
    enter_no_symptom = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input")))
    enter_no_symptom.click()


def send_line_notify_message(notification_message):
    """
    LINEにメッセージを送る
    """
    # herokuに設定した環境変数"LINE_NOTIFY_TOKEN"からアクセストークンを持ってくる
    LINE_TOKEN = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f"{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


def send_line_notify_image(notification_message, image) -> None:
    """
    LINEにメッセージ&画像を送る
    """
    LINE_TOKEN = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f"{notification_message}"}
    # rbはバイナリファイルを読み取りモードで開くオプション
    files = {"imageFile": open(image, "rb")}
    requests.post(line_notify_api, headers=headers, data=data, files=files)


def datetime_to_str() -> str:
    """
    日時の取得&str型に変換
    """
    datetime_first = datetime.datetime.now()
    datetime_str = datetime_first.strftime("%Y-%m-%d %H:%M:%S")

    return datetime_str


def get_user_data() -> list[Any]:
    """
    DBから users_userinfoのusername_id=pkのものを取得
    """
    user_data_list: list[Any] = []

    dbname = 'db.sqlite3'
    db_instance = LocalCache(dbname)

    users_userinfo_pks: list[tuple[int]] = db_instance.execute_query("""SELECT username_id FROM users_userinfo""")
    pk_users_userinfo_list: list[int] = [item for sublist in users_userinfo_pks for item in sublist]

    for pk_users_userinfo in pk_users_userinfo_list:
        target_columns = db_instance.execute_query(f"""select * from users_userinfo where username_id = {pk_users_userinfo};""")
        for j in range(0, len(target_columns)):
            user_info_grade_number: int = target_columns[j][0]
            user_info_class_number: int = target_columns[j][1]
            user_info_student_number: int = target_columns[j][2]
            user_info_student_name: str = target_columns[j][3]
            user_info_body_temperature: int = target_columns[j][4]
            user_info_is_run_code: bool = target_columns[j][5]
            user_info_last_run_at: int = target_columns[j][6]
            username_id: int = target_columns[j][7]

            user_data_list += [user_info_grade_number, user_info_class_number, user_info_student_number, user_info_student_name, user_info_body_temperature, user_info_is_run_code, user_info_last_run_at, username_id]

    return user_data_list


def set_driver():
    """
    webdriverを設定する
    """
    options = Options()
    options.add_argument('--incognito')  # シークレットモードで実行
    options.add_argument('--headless')  # ブラウザ非表示で実行
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.implicitly_wait(30)

    url = "https://forms.office.com/Pages/ResponsePage.aspx?id=skPpVutfMUa0cQNGQMsYbGpXnkvNOxxPlw82yuB56QdURUZTVVFIRkZWTkRBUEhUTktMSk84M1RFQS4u&qrcode=true"
    driver.get(url)
    # 最大の読み込み時間を設定 今回は最大30秒待機できるようにする
    wait = WebDriverWait(driver=driver, timeout=30)

    return driver, wait


def is_run_code(user_info_is_run_code, user_info_grade_number) -> bool:
    """
    コードを実行するか判定する
    """
    if user_info_is_run_code == 1:
        if user_info_grade_number == 3:
            is_run_code = True
        elif user_info_grade_number == 2:
            print("2年生")
            is_run_code = False
        elif user_info_grade_number == 1:
            print("1年生")
            is_run_code = False
    else:
        is_run_code = False

    return is_run_code


def get_ss(driver, filename) -> None:
    """
    スクリーンショットを取得
    """
    page_width = driver.execute_script("return document.body.scrollWidth")
    page_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot(filename)
    # driver.save_screenshot("before.png")


def main():
    URL = "https://forms.office.com/Pages/ResponsePage.aspx?id=skPpVutfMUa0cQNGQMsYbGpXnkvNOxxPlw82yuB56QdURUZTVVFIRkZWTkRBUEhUTktMSk84M1RFQS4u&qrcode=true"
    driver, wait = set_driver()

    user_data_list = get_user_data()
    for i in range(0, len(user_data_list)):
        for j in range(0, len(user_data_list[i])):
            user_info_grade_number = user_data_list[i][j]
            user_info_class_number = user_data_list[i][j]
            user_info_student_number = user_data_list[i][j]
            user_info_student_name = user_data_list[i][j]
            user_info_body_temperature = user_data_list[i][j]
            user_info_is_run_code = user_data_list[i][j]
            # user_info_last_run_at = user_data_list[i][j]
            # username_id = user_data_list[i][j]

            is_run = is_run_code(user_info_is_run_code, user_info_grade_number)
            if is_run:

                driver.get(URL)
                enter_kekou_kansatu(wait, user_info_class_number, user_info_student_number, user_info_student_name, user_info_body_temperature)

                # get_ss(driver, "before.png")  #  ページ全体のスクショが欲しいとき

                # 送信ボタンをクリック
                send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div")))
                send_button.click()

                # 正常に動作したかどうか確認
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/span")))
                except TimeoutException:
                    print("なし")
                finally:
                    print(f"{i}回目 正常に動作しました")

                # get_ss(driver, "after.png")  #  送信ボタンをクリックした後のスクリーンショットを撮影
                driver.quit()

                print("Done " + datetime_to_str())

                # LINE送信
                # send_line_notify_image("before", "before.png")
                # send_line_notify_image("after", "after.png")
                send_line_notify_message(f"\n{i}回目 提出しました\n" + datetime_to_str())


if __name__ == "__main__":
    main()
