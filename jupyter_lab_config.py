# IPアドレス (コンテナ名によるDNS解決を利用)
c.ServerApp.ip = "app"

# ポート番号
c.ServerApp.port = 8000

# アクセス時に必要なトークンを設定
c.ServerApp.token = "jupyter-password"

# コマンド実行時にブラウザを開かない
c.ServerApp.open_browser = False

# ルートユーザーで使用する
c.ServerApp.allow_root = True

# JupyterLabのルートディレクトリを /app に設定
c.ServerApp.root_dir = "/app"

# 隠しファイルを表示する
c.ContentsManager.allow_hidden = True

# チェックポイントファイルを /root/ipynb_checkpoints に保存する
c.FileContentsManager.checkpoints_kwargs = {
    "root_dir": "/root/ipynb_checkpoints",
}