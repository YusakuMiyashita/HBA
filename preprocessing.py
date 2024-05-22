import pandas as pd
import collections

"""
前処理の関数ファイル
"""

def decode_bytes(s):
    """
    float以外のデータ型に対してdecode処理を行う関数
    """
    if isinstance(s, float):
        #Dtype('o')をisinstance関数の引数(データ型)として指定できず->floatもfloat objectとして扱われてしまう
        #参照：https://note.nkmk.me/python-pandas-dtype-astype/#pandasdtype
        return s
    else:
        return s.decode()

def _rename_multicol(df):
    """
    カラム名の一括処理
    """
    df_col=df.columns
    df = df.T.reset_index(drop=False).T
    for  i in range(df.shape[1]):
        rename_col = {i:"_".join(df_col[i])}
        df = df.rename(columns = rename_col)
    return df

def tag_count(dfs):
    """
    Seriesの頻度分布をtable形式で出力
    """
    tag_count = collections.Counter(dfs)
    count = pd.DataFrame(list(tag_count.values()),
                        columns=["Count"],
                        index=list(tag_count.keys()) )
    return count

def merge_dataframes(dfs):
    """
    複数のデータフレームを"SUBJID"をキーにマージする関数
    """
    merged_df = dfs[0]
    for i in range(1, len(dfs)):
        merged_df = pd.merge(merged_df, dfs[i], on="SUBJID", how="outer")
    return merged_df
