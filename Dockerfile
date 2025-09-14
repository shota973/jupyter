# python:3.13.7-slim-trixieというimageをもとにimageを構築
FROM python:3.13.7-slim-trixie

# 以下のコマンドなどの実行を/appディレクトリで行う
WORKDIR /app

# jupyterlabのインストール
RUN pip install --upgrade pip
RUN python -m pip install jupyterlab

# ローカルの作業ディレクトリ内のファイルををコピー
COPY . .