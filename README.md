# GIRIGHT - アウトドアギア管理アプリ

GIRIGHTは、アウトドア愛好家のためのギア管理Webアプリケーションです。バックパッキングやハイキングなどのアクティビティに持っていくギアの重量管理、パックリスト作成をサポートします。

## 主な機能

- **ギア管理**: 名前、メーカー、重量、カテゴリなどの情報を登録・管理
- **重量計算**: パックリストの合計重量を自動計算、目標重量との差分を表示
- **カテゴリ分析**: カテゴリごとの重量分布をグラフで可視化
- **検索機能**: 名前やカテゴリでギアを検索
- **パックリスト**: 持っていくギアを選択してパックリストを作成

## カテゴリ

- Shelter（シェルター）: テント、タープなど
- Sleep（睡眠）: 寝袋、マットなど
- Pack（バッグ）: バックパック、ポーチなど
- Cook（調理）: ストーブ、クッカーなど
- Wear（衣類）: 衣類、レインウェアなど
- Water（水）: 水筒、浄水器など
- Electronics（電子機器）: ヘッドライト、GPSなど
- Misc（その他）: その他のギア

## インストール方法

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/GIRIGHT.git
cd GIRIGHT

# 仮想環境を作成して有効化
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 依存パッケージをインストール
pip install -r requirements.txt

# 環境変数の設定（オプション）
export SECRET_KEY="your-secret-key"
export FLASK_ENV="development"  # 開発環境の場合

# データベースの初期化
mkdir -p instance
flask --app run.py shell
# Pythonシェルで以下を実行
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
# Ctrl+Dでシェルを終了

# サンプルデータの追加（オプション）
python seed.py
```

## 使い方

```bash
# アプリケーションを実行
python run.py
```

ブラウザで http://localhost:5000 にアクセスしてください。

## プロジェクト構成

```
GIRIGHT/
├── app/
│   ├── __init__.py  # Flaskアプリケーションの初期化
│   ├── routes.py    # ルート定義
│   ├── models.py    # データモデル
│   ├── forms.py     # フォーム定義
│   ├── static/      # 静的ファイル（CSS、JavaScript、画像など）
│   └── templates/   # HTMLテンプレート
├── instance/        # インスタンス固有のファイル（データベースなど）
├── config.py        # 設定ファイル
├── run.py           # アプリケーション実行ファイル
├── seed.py          # サンプルデータ追加スクリプト
├── requirements.txt # 依存パッケージリスト
└── README.md        # このファイル
```

## 開発環境

- Python 3.9+
- Flask 3.1.0
- SQLAlchemy 2.0.39
- Flask-SQLAlchemy 3.1.1
- Flask-WTF 1.2.2

## ライセンス

MIT