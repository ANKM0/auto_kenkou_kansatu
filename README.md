# auto_kenkou_kansatu
健康観察を自動入力するシステムとサイト

## URL
EC2サーバーで公開中です <br>
http://43.206.84.20/


# 使い方
1. ルートフォルダ(auto_kenkou_kansatu)直下に.envファイルを作成します <br>

1. 以下のコマンドを実行してSECRET_KEYを生成します <br>
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

3. .env_sanpleを参考にSECRET_KEYを入力 <br>
```
SECRET_KEY = [SECRET_KEY]
```
4. 以下のコマンドを実行してローカルサーバーを立ち上げます
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# 健康観察を自動入力するシステムとサイト
## ソースコード
https://github.com/ANKM0/auto_kenkou_kansatu
## 設計資料

<details>
<summary>設計資料</summary>

## <全体>
![portfolio_ax2](https://i.gyazo.com/d21eae30213e8b6a0e927448f3eb6c83.png)
## <サイト>
![portfolio_ax3](https://i.gyazo.com/8dc88c1768f03a944669c3d2558e64f5.png)
</details>


# やりたかったこと
健康観察を自動入力するシステムを作る

# 背景
健康観察を入力するのが面倒だったのでクローラーから自動で入力するシステムを作りました<br>
友人に話したところ、使いたいとのことだったので、<br>
他の人が使えるように入力内容を登録するためのサイトを作りました

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
安定した動作を実現したかったため、動的な待機ができるSeleniumを使用しました<br>


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
LIneをdjangoで使う際にOAuthの設定部分が上手く行きませんでした　<br>
先例を調べたり、公式ドキュメントを読み込んだりすることで解決しました

- テスト<br>
GitHub Actionsを使ってCIを動かす時にSeleniumが上手く動作しませんでした <br>
先例と公式ドキュメントを参考に問題を切り分けて行くことで解決しました



# この先改善したいこと
- 開発方針をTDD形式に変更<br>
手戻りが多かったので
先にテストコードを書くことが必要だと感じました
- 説明の追加<br>
使用者が友人で事前に使い方を伝えていたため <br>
説明が不足し、一般ユーザには使い方が分かりにくいかもしれないです
