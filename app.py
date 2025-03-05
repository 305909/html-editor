import streamlit as st
from streamlit_ace import st_ace


x, y, z = st.columns([1, 2, 1])
with y:
    st.image("docs/iiscena-logo.png", width=50)
    
st.title("Live HTML Editor 📝")
    
st.subheader("📝 Write Your HTML Code")

html_content = st_ace(
    value="<h1>Hello, World!</h1>\n<p>Write your HTML code here...</p>",
    language="html",
    theme="monokai",
    font_size=14,
    tab_size=4,
    height=400
)

execute_code = st.button("▶️ Run")

st.subheader("🌐 Preview")

if execute_code:
    rendered_html = f"""
    <div style="background-color: white; padding: 20px; min-height: 300px;">
        {html_content}
    </div>
    """
    st.components.v1.html(rendered_html, height=400, scrolling=True)
    
else:
    st.info("Press 'Run' to display the HTML code on screen.")

st.markdown("---")

file_name = st.text_input("📁 File name (without extension):", value="file")
st.download_button(
    label="📥 Download HTML Code",
    data=html_content,
    file_name=f"{file_name}.html",
    mime="text/html"
)
