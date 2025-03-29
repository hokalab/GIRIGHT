from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # 開発環境ではデバッグモードをオン、本番環境ではオフ
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)