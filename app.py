import streamlit as st

# Titolo della web app
st.title("Live HTML Editor 📝")

# Creazione di due colonne (Editor a sinistra, Anteprima a destra)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Scrivi il tuo codice HTML")
    html_code = st.text_area("Editor HTML:", height=500, 
                             value="<h1>Hello, World!</h1>\n<p>Scrivi il tuo codice HTML qui...</p>")

with col2:
    st.subheader("🌐 Anteprima")
    
    # Aggiungere un background bianco per evitare lo sfondo nero
    html_with_style = f"""
    <div style="background-color: white; padding: 20px; height:100%;">
        {html_code}
    </div>
    """
    
    st.components.v1.html(html_with_style, height=500, scrolling=True)
