import os
import sys
from openai import OpenAI


def start_chat():
    print("========================================")
    print("    人工智能导论 HW02 - DeepSeek Chatbot")
    print("========================================")

    # 优先从环境变量获取，如果没有则提示手动输入，防止 Key 泄露到 GitHub
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        api_key = input("请输入您的 DeepSeek API Key: ").strip()

    if not api_key:
        print("错误：未检测到有效的 API Key，程序退出。")
        return

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

        messages = [{"role": "system", "content": "你是一个有用的 AI 助手。"}]
        print("\n[系统] 连接成功！开始你的对话吧（输入 'q' 退出）")

        while True:
            user_input = input("\nUser: ").strip()
            if not user_input: continue
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("再见！")
                break

            messages.append({"role": "user", "content": user_input})

            # 调用 DeepSeek API
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )

            answer = response.choices[0].message.content
            print(f"\nAI: {answer}")
            messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        print(f"\n[发生错误]：{e}")
        print("请检查你的 API Key 是否正确或网络是否连通。")


if __name__ == "__main__":
    start_chat()