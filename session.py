# -*- ecoding: utf-8 -*-
# @ModuleName: session
# @Author: wk
# @Email: 306178200@qq.com
# @Time: 2024/1/8 16:41
import streamlit as st

# 定义一个用于更新计数的回调函数
def update_counter():
    st.session_state['counter'] += 1

# 检查并初始化会话状态变量
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

if 'my_list' not in st.session_state:
    st.session_state['my_list'] = []

# 显示当前计数
st.write(f'当前计数: {st.session_state["counter"]}')

# 创建一个按钮，点击时调用 update_counter 函数
st.button('增加计数', on_click=update_counter)

# 添加元素到列表的示例（这里我们添加当前计数器的值）
st.session_state['my_list'].append(st.session_state['counter'])

# 显示列表内容
st.write('当前列表:', st.session_state['my_list'])
