import streamlit as st
import random
st.title("クイズ〇〇keyを押せ")
#問題の作成
KEYS=[
    "Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Ins","Prt","Del","Home","End","PgUp","PgDn",
    "半/全","1","2","3","4","5","6","7","8","9","0","-1","^","￥","Bs","NL","/1","*","-2",
    "Tab","Q","W","E","R","T","Y","U","I","O","P","@","[","En1","7.1","8.1","9.1","+1",
    "CL","A","S","D","F","G","H","J","K","L",";",":","]","En2","4.1","5.1","6.1","+2",
    "Sh1","Z","X","C","V","B","N","M",",",".1","/2","_","Sh2","1.1","2.1","3.1","En3",
    "Ct1","Fn","Win","Alt","無変換","Sp","変換","カひロ","Ct2","←","↑","↓","→","0",".2","En4"
]
#問題を選ぶ
if "what" not in st.session_state:
    st.session_state.what = random.choice(KEYS)
#問題の表示
st.header(f"スマホ版このkeyを押せ：{st.session_state.what}")

if "result" not in st.session_state:
    st.session_state.result = ""
if "answered" not in st.session_state:
    st.session_state.answered = False
#正解、不正解かどちらかの確認
def check_answer(key):
    if key == st.session_state.what:
        st.session_state.result = f"正解！ {key}"
        st.balloons()
    else:
        st.session_state.result = f"不正解… 押したキー：{key}"
        st.snow()
    st.session_state.answered = True
#ボタンを作る
def make_buttons(keys, row_name):
    row = st.columns([0.5 for _ in keys])
    for i, (col, key) in enumerate(zip(row, keys)):
        if col.button(key, key=f"{row_name}_{i}"):
            check_answer(key)
#ボタンの種類の作成
keys1 = ["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Ins","Prt","Del","Home","End","PgUp","PgDn"]
make_buttons(keys1, "row1")

keys2 = ["半/全","1","2","3","4","5","6","7","8","9","0","-1","^","￥","Bs","NL","/1","*","-2"]
make_buttons(keys2, "row2")

keys3 = ["Tab","Q","W","E","R","T","Y","U","I","O","P","@","[","En1","7.1","8.1","9.1","+1"]
make_buttons(keys3, "row3")

keys4 = ["CL","A","S","D","F","G","H","J","K","L",";",":","]","En2","4.1","5.1","6.1","+2"]
make_buttons(keys4, "row4")

keys5 = ["Sh1","Z","X","C","V","B","N","M",",",".1","/2","_","Sh2","1.1","2.1","3.1","En3"]
make_buttons(keys5, "row5")

keys6 = ["Ct1","Fn","Win","Alt","無変換","Sp","変換","カひロ","Ct2","←","↑","↓","→","0",".2","En4"]
make_buttons(keys6, "row6")
#正解不正解の表示
st.subheader(st.session_state.result)
#次の問題へのボタンの作成
if st.session_state.answered:
    if st.button("次の問題へ"):
        st.session_state.what = random.choice(KEYS)
        st.session_state.result = ""
        st.session_state.answered = False