import streamlit as st

def main():
    st.set_page_config(page_title="AI智慧陪伴助理-九宮格服務", layout="wide")

    # 使用 markdown 來創建置中的兩行標題
    st.markdown("""
    <h1 style="text-align: center;">AI智慧陪伴助理-九宮格服務</h1>
    <h2 style="text-align: center;">(AI Assistant for Aging Services)</h2>
    """, unsafe_allow_html=True)

    # 添加一些間距
    st.markdown("<br>", unsafe_allow_html=True)

    # 定義服務列表
    services = [
        {"name": "查農民曆", "en_name": "Lunar Calendar", "url": "https://e-lunarexp.streamlit.app/"},
        {"name": "創意繪本(語音版)", "en_name": "Paint Books", "url": "https://acgsound.streamlit.app/"},
        {"name": "整理新知", "en_name": "Update Information", "url": "https://e-langchainrag.streamlit.app/"},
        {"name": "浪漫樂曲(台)", "en_name": "Make Music", "url": "https://e-sunoapi0808.streamlit.app/"},
        {"name": "浪漫樂曲(國)", "en_name": "Make Music", "url": "https://e-sunoapi_C.streamlit.app/"},
        {"name": "浪漫樂曲(英)", "en_name": "Make Music", "url": "https://e-sunoapi_E.streamlit.app/"},
        {"name": "更多工具", "en_name": "More Tools", "url": None},
        {"name": "應用市集", "en_name": "Apps Market", "url": None},
        {"name": "與我聯繫", "en_name": "Contact Us", "url": None}
        
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
                        background-color: #81D8D0;
                        border-radius: 10px;
                        padding: 20px;
                        text-align: center;
                        height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        margin-bottom: 20px;
                    ">
                        <h3 style="margin: 0; color: #ffffff;">{service['name']}</h3>
                        <p style="margin: 10px 0; color: #ffffff; font-size: 1.4em; font-weight: bold;">{service['en_name']}</p>
                        <a href="{service['url']}" target="_blank" style="
                            background-color: #ffffff;
                            color: #81D8D0;
                            padding: 5px 10px;
                            border-radius: 5px;
                            text-decoration: none;
                            font-weight: bold;
                        ">前往服務</a>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="
                        background-color: #F0F0F0;
                        border-radius: 10px;
                        padding: 20px;
                        text-align: center;
                        height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        margin-bottom: 20px;
                    ">
                        <h3 style="margin: 0; color: #333333;">{service['name']}</h3>
                        <p style="margin: 10px 0; color: #333333; font-size: 1.4em; font-weight: bold;">{service['en_name']}</p>
                        <small style="color: #666666;">建構中 (Under Construction)</small>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
