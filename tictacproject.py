import numpy as np
import streamlit as st

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1       
    st.session_state.result = None

symbols = {0: " ", 1: "X", -1: "O"}

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    if not 0 in b:
        return "DRAW"

    return None



st.title("🎮 Tic-Tac-Toe (NumPy + Streamlit)")

if st.session_state.result:
    if st.session_state.result == "DRAW":
        st.success("😎 Ohoo, it's a draw!")
    else:
        st.success(f"🏆 {st.session_state.result} wins!")
else:
    turn = "X" if st.session_state.current == 1 else "O"
    st.info(f"It's **{turn}**'s turn")

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        with cols[j]:
            cell_value = symbols[st.session_state.board[i, j]]
            is_disabled = (st.session_state.board[i, j] != 0) or (st.session_state.result is not None)
            if st.button(cell_value or " ", key=f"{i}-{j}", disabled=is_disabled):
                st.session_state.board[i, j] = st.session_state.current
                result = check_winner(st.session_state.board)
                if result:
                    st.session_state.result = result
                else:
                    st.session_state.current *= -1
                st.rerun()      

if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None
    st.rerun()          
