import streamlit as st

# Titolo della web app
st.title("Live HTML Editor 📝")

# Creazione di due colonne (una per il codice e una per il rendering)
col1, col2 = st.columns([1, 1])  # Due colonne uguali

with col1:
    st.subheader("📝 Scrivi il tuo codice HTML")
    html_code = st.text_area("Editor HTML:", height=500, 
                             value="<h1>Hello, World!</h1>\n<p>Scrivi il tuo codice HTML qui...</p>")

with col2:
    st.subheader("🌐 Anteprima")
    st.components.v1.html(html_code, height=500, scrolling=True)
