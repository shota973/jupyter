# 接続を許可するIPアドレス
c.ServerApp.ip = "app"

# ポート番号
c.ServerApp.port = 8000

# アクセス時に必要なトークンを無効化
c.ServerApp.token = "jupyter-password"

# コマンド実行時にブラウザを開かない
c.ServerApp.open_browser = False

# ルートユーザーで使用する
c.ServerApp.allow_root = True

# ルートユーザーのホームディレクトリをJupyterLab上のルートディレクトリに設定
c.ServerApp.root_dir = "/app"

# JupyterLab上のファイルツリーで隠しファイルを表示するオプションを使用可能にする
c.ContentsManager.allow_hidden = True

# チェックポイントファイルを /tmp に保存する
c.FileContentsManager.checkpoints_kwargs = {
    "root_dir": "/tmp/ipynb_checkpoints",
}