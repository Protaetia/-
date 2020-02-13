from graphillion import GraphSet as gs
import pandas as pd

df=pd.read_csv("") #ここでCSVファイルを読み込み

univ=[]
weight={}

for i, v in df.iterrows():
 egde=(v["start"],v["end"])
 univ.append(edge)
 weight[edge]=v["kiro"]

gs.set_universe(univ)
path=gs.paths("","") #始点と終点を入力
max_path=next(path.max_iter(weight))
print(max_path)
