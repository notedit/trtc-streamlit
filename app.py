import streamlit as st
from datetime import datetime


import TLSSigAPIv2

from trtc_component import trtc_component


api = TLSSigAPIv2.TLSSigAPIv2(
    1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
sig = api.gen_sig("xiaojun")

if 'counter' not in st.session_state:
    st.session_state.counter = 0


def main():
    def run_component(props):

        value = trtc_component(name='hello', **props)
        print(value)
        return value

    def handle_event(value):
        st.session_state.counter = st.session_state.counter + 1

    st.title('Toggle Buttons Component Demo')
    st.session_state.counter = st.session_state.counter + 1

    props = {
        'action': sig,
        'counter': st.session_state.counter,
        'datetime': str(datetime.now().strftime("%H:%M:%S, %d %b %Y"))
    }

    handle_event(run_component(props))


if __name__ == '__main__':
    main()
