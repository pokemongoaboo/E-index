import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="九宮格服務", layout="wide")

    st.title("九宮格服務")

    # 自定義CSS
    st.markdown("""
    <style>
    .service-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 30px;
    }
    .service-item {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .service-item:hover {
        transform: translateY(-5px);
    }
    .under-construction {
        background-color: #ffeeba;
        color: #856404;
    }
    </style>
    """, unsafe_allow_html=True)

    # 九宮格服務
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

    # 使用HTML和CSS創建九宮格
    grid_html = '<div class="service-grid">'
    for service in services:
        if service["url"]:
            grid_html += f"""
            <a href="{service['url']}" target="_blank" class="service-item">
                <h3>{service['name']}</h3>
                <p>{service['en_name']}</p>
            </a>
            """
        else:
            grid_html += f"""
            <div class="service-item under-construction">
                <h3>{service['name']}</h3>
                <p>{service['en_name']}</p>
                <small>建構中 (Under Construction)</small>
            </div>
            """
    grid_html += '</div>'

    # 渲染HTML
    components.html(grid_html, height=600)

if __name__ == "__main__":
    main()
