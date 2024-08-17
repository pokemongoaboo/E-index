import streamlit as st

def main():
    st.set_page_config(page_title="九宮格服務", layout="wide")

    st.title("AI智慧陪伴助理-九宮格服務(AI Assistant for Aging Servcies)")

    # 定義服務列表
    services = [
        {"name": "查行事曆", "en_name": "Check Calendar", "url": "https://e-readcalendar.streamlit.app/"},
        {"name": "查農民曆", "en_name": "Lunar Calendar", "url": "https://e-lunarexp.streamlit.app/"},
        {"name": "整理新知", "en_name": "Update Information", "url": "https://e-langchainrag.streamlit.app/"},
        {"name": "圖卡生成", "en_name": "Create Picture", "url": "https://e-pokemongoaboo.streamlit.app/"},
        {"name": "掃描預約", "en_name": "Set Calendar", "url": "https://e-ocr2cal.streamlit.app/"},
        {"name": "創意繪本", "en_name": "Paint Books", "url": "https://e-paintbook2.streamlit.app/"},
        {"name": "浪漫樂曲", "en_name": "Make Music", "url": "https://e-sunoapi0808.streamlit.app/"},
        {"name": "更多工具", "en_name": "More Tools", "url": None},
        {"name": "應用市集", "en_name": "Apps Market", "url": None}
    ]

    # 使用Streamlit的列和列布局創建九宮格
    for i in range(0, 9, 3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                service = services[i+j]
                if service["url"]:
                    st.markdown(f"""
                    <div style="
                        background-color: #f8f9fa;
                        border-radius: 10px;
                        padding: 20px;
                        text-align: center;
                        height: 150px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        margin-bottom: 20px;
                    ">
                        <h3 style="margin-bottom: 10px;">{service['name']}</h3>
                        <p style="margin-bottom: 10px;">{service['en_name']}</p>
                        <a href="{service['url']}" target="_blank">前往服務</a>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="
                        background-color: #ffeeba;
                        border-radius: 10px;
                        padding: 20px;
                        text-align: center;
                        height: 150px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        margin-bottom: 20px;
                    ">
                        <h3 style="margin-bottom: 10px;">{service['name']}</h3>
                        <p style="margin-bottom: 10px;">{service['en_name']}</p>
                        <small>建構中 (Under Construction)</small>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
