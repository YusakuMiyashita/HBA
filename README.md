HBA：Hospital Bed Analysis
==============================

厚労省が集計している病床機能報告データの分析を目的とする。

## 環境構築
コード管理はGithubを利用している。  
分析環境はDockerで構築し、VSCodeのDevContainersを利用することを推奨。

### コード管理

Githubを利用してコード管理をしていく。  

基本的にはタスク単位でブランチを切り、プルリクエストでPM確認の後にマージする運用とする。  

### 分析環境構築

#### macOSの場合
初回のみ1〜4を実施する。2回目以降は5からでよい

1. Docker環境をインストールする。Mac環境では[Rancher Desktop](https://rancherdesktop.io/)を推奨

2. （推奨）Rancher Desktopの右上の⚙️ボタン→「Virtual Machine」→「Hardware」→ Memoryを8GB、CPUを8に設定する

3. VSCodeの拡張機能 [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) をインストールする

4. このリポジトリをクローンする

```sh
git clone https://github.com/YusakuMiyashita/HBA.git
```

5. Rancher Desktopを起動する

6. VSCodeを起動、コマンドパレットを開き`Dev Containers: Rebuild and Reopen in Container..`または`Dev Containers: Open Folder in Container..`を選択し`HBA`フォルダを選択

7. VSCode内でNotebookを開き、セルを実行する。その際、カーネルの選択を求められることがあるが、.venv上の`Python 3.12`系を選択すればよい。

8. コンテナから抜ける場合は、VSCodeの左下の「><」ボタンを押し、`フォルダーをローカルで再度開く`を選択

## フォルダ構成
[cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)にしたがってフォルダ構成を作成。  
この通りにする必要はないので、適宜見直していく。

------------

    |-- README.md
    |-- csv
    |   `--
    |-- dataanalysis
    |   |-- __init__.py
    |   |-- data
    |   |   |-- __init__.py
    |   |   `-- make_dataset.py
    |   |-- features
    |   |   `-- __init__.py
    |   |-- models
    |   |   `-- __init__.py
    |   `-- visualization
    |       `-- __init__.py
    |-- .gitignore
    |-- notebook
    |   `--
    |-- poetry.lock
    |-- preprocessing.py
    `-- pyproject.toml
    
    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
