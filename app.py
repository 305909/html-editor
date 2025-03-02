import streamlit as st

# Titolo della web app
st.title("Live HTML Editor 📝")

# Campo di testo per scrivere codice HTML
html_code = st.text_area("Scrivi il tuo codice HTML qui:", height=300, 
                         value="<h1>Hello, World!</h1>\n<p>Scrivi il tuo codice HTML qui...</p>")

# Mostra il rendering del codice HTML
st.subheader("Anteprima:")
st.components.v1.html(html_code, height=400, scrolling=True)
