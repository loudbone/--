import streamlit as st
import random
st.title("クイズ〇〇keyを押せ")
KEYS=[
    "Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Ins","Prt","Del","Home","End","PgUp","PgDn",
    "半/全","1","2","3","4","5","6","7","8","9","0","-1","^","￥","Bs","NL","/1","*","-2",
    "Tab","Q","W","E","R","T","Y","U","I","O","P","@","[","En1","7.1","8.1","9.1","+1",
    "CL","A","S","D","F","G","H","J","K","L",";",":","]","En2","4.1","5.1","6.1","+2",
    "Sh1","Z","X","C","V","B","N","M",",",".1","/2","_","Sh2","1.1","2.1","3.1","En3",
    "Ct1","Fn","Win","Alt","無変換","Sp","変換","カひロ","Ct2","←","↑","↓","→","0",".2","En4"
]

if "what" not in st.session_state:
    st.session_state.what = random.choice(KEYS)

st.header(f"パソコン版このkeyを押せ：{st.session_state.what}")

if "result" not in st.session_state:
    st.session_state.result = ""
if "answered" not in st.session_state:
    st.session_state.answered = False

def check_answer(key):
    if key == st.session_state.what:
        st.session_state.result = f"正解！ {key}"
        st.balloons()
    else:
        st.session_state.result = f"不正解… 押したキー：{key}"
        st.snow()
    st.session_state.answered = True

def make_buttons(keys, row_name):
    cols = st.columns(10)
    for i, key in enumerate(keys):
        if cols[i % 10].button(key, key=f"{row_name}_{i}"):
            check_answer(key)

make_buttons(["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Ins","Prt","Del","Home","End","PgUp","PgDn"], "row1")
make_buttons(["半/全","1","2","3","4","5","6","7","8","9","0","-1","^","￥","Bs","NL","/1","*","-2"], "row2")
make_buttons(["Tab","Q","W","E","R","T","Y","U","I","O","P","@","[","En1","7.1","8.1","9.1","+1"], "row3")
make_buttons(["CL","A","S","D","F","G","H","J","K","L",";",":","]","En2","4.1","5.1","6.1","+2"], "row4")
make_buttons(["Sh1","Z","X","C","V","B","N","M",",",".1","/2","_","Sh2","1.1","2.1","3.1","En3"], "row5")
make_buttons(["Ct1","Fn","Win","Alt","無変換","Sp","変換","カひロ","Ct2","←","↑","↓","→","0",".2","En4"], "row6")

st.subheader(st.session_state.result)

if st.session_state.answered:
    if st.button("次の問題へ"):
        st.session_state.what = random.choice(KEYS)
        st.session_state.result = ""
        st.session_state.answered = False