# Qiime-top-OTU-search

sample code

入力したtsvファイル(例：collapsed_table_relative_L6.tsv)から検体ごとに最も存在比が高い細菌の分類を標準出力する

q_search 'collapsed_table_relative_L6.tsv' --module 'tophit_all'


入力したtsvファイル(collapsed_table_relative_L6.tsv)から指定した検体(例：L6S68)の最も存在比が高い細菌の分類を標準出力する

q_search 'collapsed_table_relative_L6.tsv' --module 'tophit' --scpname 'L6S68'
