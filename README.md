# auto_kenkou_kansatu
健康観察を自動入力するシステムとサイト


# 使い方
1. ルートフォルダ直下に.envファイルを作成 <br>

1. 以下のコマンドを実行してSECRET_KEYを生成 <br>
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

3. .env_sanpleを参考にSECRET_KEYを入力 <br>
```
SECRET_KEY = [SECRET_KEY]
```
4. 以下のコマンドを実行してローカルサーバーを立ち上げる
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# 健康観察を自動入力するシステムとサイト
## ソースコード
https://github.com/ANKM0/showcase/tree/main/auto_kenkou_kansatu
## 設計資料

<details>
<summary>設計資料</summary>

## <全体>
![portfolio_ax2](https://user-images.githubusercontent.com/76755363/186117514-acec9b22-ccd5-4bcc-b9f7-d03ccf7beaa1.png)
## <サイト>
![portfolio_ax3](https://user-images.githubusercontent.com/76755363/186117565-3a2016e5-808f-40c6-b781-430f496d21fd.png)
</details>



# やりたかったこと
健康観察を自動入力するシステムを作る

# 背景
健康観察を入力するのが面倒でクローラーから自動で入力するシステムを作った<br>
友人に話したところ、使いたいとのことだったので、<br>
他の人が使えるように入力内容を登録するためのサイトを作った

# 使用したもの
- Python
- フレームワーク<br>
Django<br>
Selenium

- DB<br>
sqlite3<br>

- サーバー<br>
Heroku<br>

その他<br>
- Git,GitHub,VSCode,GitHub Actions
## 選んだ理由
安定した動作を実現したかったため、動的な待機ができるSeleniumを使用した<br>


# こだわったところ
- Lineログインに対応<br>
パスワードを登録する手間を無くすために<br>
Lineからログインできるようにしました
- UI UX <br>
ユーザが何をしたら良いか分かりやすいように<br>
データの状態によって不必要なボタンを表示しないようにしました
- テスト <br>
動作を保障できるようにするために <br>
機能テスト、単体テストのテストコードを作成し、GitHub Actionsを使って
プルリクエスト時にCIが動くように設定しました



# 苦労したところ
- Lineログイン<br>
LIneをdjangoで使う際にOAuthの設定部分が上手く行かなかった　<br>
先例を調べたり、公式ドキュメントを読み込んだりすることで解決した

- テスト<br>
GitHub Actionsを使ってCIを動かす時にSeleniumが上手く動作しなかった <br>
先例と公式ドキュメントを参考に問題を切り分けて行くことで解決した



# この先改善したいこと
- 開発方針をTDD形式に変更<br>
手戻りが多かったので
先にテストコードを書くことが必要だと感じた
- 説明の追加<br>
使用者が友人で事前に使い方を伝えていたため
説明が不足している<br>
一般ユーザには使い方が分からないかもしれない
- サーバーの変更<br>
高校を卒業したこと、herokuが有料化したことなどによって<br>
現在はサーバー上で動していないので<br>
もし、動かすならサーバーの変更が必要
