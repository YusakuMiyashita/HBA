import matplotlib as mpl
import matplotlib.font_manager as fm
import os

script_dir = os.path.dirname(__file__) # 現在のスクリプトファイルのディレクトリを取得
font_path = os.path.join(script_dir, 'MS Gothic.ttf') # 相対パスを指定してファイルのパスを作成

def fontfix():
    """
    フォントの設定
    """
    fm.fontManager.addfont(font_path) # フォントマネージャーにフォントを追加

    mpl.rcParams['font.family'] = 'MS Gothic'