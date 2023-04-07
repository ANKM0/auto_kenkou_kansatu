# auto_kenkou_kansatu
健康観察を自動入力するシステムに初期情報を入力するためのサイトです

## URL
EC2サーバーで公開中です
http://13.115.159.130/


## やりたかったこと

健康観察を自動入力するシステムを作る

## 背景

健康観察を入力するのが面倒だったのでクローラーから自動で入力するシステムを作りました

友人に話したところ、使いたいとのことだったので、他の人が使えるように入力内容を登録するためのサイトを作りました


## 使用したもの

- Python
- フレームワーク
Django
Selenium

- DB
sqlite3

- サーバー
Heroku

その他
- Git,GitHub,VSCode,GitHub Actions

## 選んだ理由
安定した動作を実現したかったため、動的な待機ができるSeleniumを使用しました


# こだわったところ
- Lineログインに対応
パスワードを登録する手間を無くすために
Lineからログインできるようにしました
- UI UX
ユーザが何をしたら良いか分かりやすいように
データの状態によって不必要なボタンを表示しないようにしました
- テスト
動作を保障できるようにするために
機能テスト、単体テストのテストコードを作成し、GitHub Actionsを使って
プルリクエスト時にCIが動くように設定しました



# 苦労したところ
- Lineログイン
LIneをdjangoで使う際にOAuthの設定部分が上手く行きませんでした　
先例を調べたり、公式ドキュメントを読み込んだりすることで解決しました

- テスト
GitHub Actionsを使ってCIを動かす時にSeleniumが上手く動作しませんでした
先例と公式ドキュメントを参考に問題を切り分けて行くことで解決しました



# この先改善したいこと
- 開発方針をTDD形式に変更
手戻りが多かったので
先にテストコードを書くことが必要だと感じました
- 説明の追加
使用者が友人で事前に使い方を伝えていたため
説明が不足し、一般ユーザには使い方が分かりにくいかもしれないです


## 設計資料

<details>
<summary>設計資料</summary>

## <全体>
![portfolio_ax2](https://i.gyazo.com/d21eae30213e8b6a0e927448f3eb6c83.png)
## <サイト>
![portfolio_ax3](https://i.gyazo.com/8dc88c1768f03a944669c3d2558e64f5.png)
</details>



## how to setup

1. リポジトリをクローンします

    `git clone git@github.com:ANKM0/auto_kenkou_kansatu.git`


1. LINE TOKENとChannel ID (取得方法は省略)

    ```cmd
    cd auto_kenkou_kansatu
    touch .env
    ```


1. 以下のコマンドを実行してSECRET_KEYを作成します

    ```cmd
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()
    ```

1. ルートフォルダ(auto_kenkou_kansatu)直下に.envファイルを作成します

    ```cmd
    cd auto_kenkou_kansatu
    touch .env
    ```

1. .env_sanpleを参考に環境変数を入力します

    ```cmd
    SECRET_KEY='_hq51hv^!3s!i0jq!$*_q%$m7w1$f'
    SOCIAL_AUTH_LINE_KEY=1234567 # Channel ID
    SOCIAL_AUTH_LINE_SECRET="qawsedrftgyhujikolp"  # Channel secret
    ```

1. 以下のコマンドを実行してローカルサーバーを立ち上げます

    ```cmd
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
