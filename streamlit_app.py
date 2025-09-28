# -*- coding: utf-8 -*-
import dashscope
from dashscope import Generation
import streamlit as st

# 设置页面标题
st.title("💬 通义千问 Chatbot")

# 在侧边栏输入 API Key
with st.sidebar:
    dashscope_api_key = st.text_input("DashScope API Key", key="qwen_api_key", type="password")

# 初始化 messages（对话历史）
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你好！我是通义千问，有什么我可以帮你的吗？"}]

# 显示历史消息
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 监听用户输入
if prompt := st.chat_input():
    # 检查是否提供了 API Key
    if not dashscope_api_key:
        st.info("请在侧边栏输入你的 DashScope API Key 才能继续。")
        st.stop()

    # 设置 API Key
    dashscope.api_key = dashscope_api_key

    # 将用户输入添加到历史记录并显示
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # 调用 Qwen-Turbo 模型
        response = Generation.call(
            model="qwen-turbo",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=1000,
            result_format='message'
        )

        # 检查响应状态
        if response.status_code == 200:
            msg = response.output.choices[0].message
        else:
            msg = {"role": "assistant", "content": f"错误：{response.code} - {response.message}"}

    except Exception as e:
        msg = {"role": "assistant", "content": f"调用失败：{str(e)}"}

    # 将模型回复添加到历史并显示
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])