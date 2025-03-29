import random
from app import create_app, db
from app.models import Gear

app = create_app()
app.app_context().push()

categories = ['shelter', 'sleep', 'pack', 'cook', 'wear', 'water', 'elec', 'misc']
sample_gears = [
    'ULテント', 'ダウンシュラフ', 'アルミマット', 'クッカー', 'ウィンドジャケット',
    'ボトル', 'LEDライト', 'モバイルバッテリー', 'タープ', 'スタッフバッグ',
    '軽量ザック', 'レインウェア', '浄水器', 'ティッシュ', '小型ナイフ',
    'ガスバーナー', 'ロングスプーン', 'エマージェンシーシート', 'ファーストエイド', '予備ソックス'
]

manufacturers = ['mont-bell', 'NEMO', 'NANGA', 'EVERNEW', 'SOTO', 'Sea To Summit', 'MSR', 'UNIQLO', 'Daiso']

# 既存データ削除（任意）
db.session.query(Gear).delete()

for name in sample_gears:
    gear = Gear(
        name=name,
        manufacturer=random.choice(manufacturers),
        weight=round(random.uniform(20, 800), 1),
        category=random.choice(categories),
        essential=random.choice([True, False]),
        is_packed=random.choice([True, False]),
        notes='テスト登録アイテム'
    )
    db.session.add(gear)

db.session.commit()
print("✅ テスト用ギア20個登録完了！")