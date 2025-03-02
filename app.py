import streamlit as st
from streamlit_ace import st_ace

# Titolo della web app
st.title("Live HTML Editor 📝")

st.subheader("📝 Scrivi il tuo codice HTML")

# Editor con evidenziazione della sintassi
html_code = st_ace(
    value="<h1>Hello, World!</h1>\n<p>Scrivi il tuo codice HTML qui...</p>",
    language="html",
    theme="github",  # Cambia con: "monokai", "solarized_light", "dracula", ecc.
    font_size=14,
    tab_size=4,
    height=400
)

# Input per il nome del file
file_name = st.text_input("Nome del file (senza estensione):", value="mio_file")

# Creazione di due colonne per i pulsanti (opzionale per allineamento)
col1, col2 = st.columns([1, 1])

with col1:
    # Bottone per eseguire il codice
    run_code = st.button("▶️ Run")

with col2:
    # Bottone per scaricare il file
    if st.button("💾 Download"):
        if not file_name.strip():
            st.warning("⚠️ Inserisci un nome valido per il file!")
        else:
            st.download_button(label="📥 Scarica il codice HTML",
                               data=html_code,
                               file_name=f"{file_name}.html",
                               mime="text/html")

st.subheader("🌐 Anteprima")

# Esegui il codice solo quando si preme "Run"
if run_code:
    html_with_style = f"""
    <div style="background-color: white; padding: 20px; min-height: 300px;">
        {html_code}
    </div>
    """
    st.components.v1.html(html_with_style, height=400, scrolling=True)
else:
    st.info("Premi 'Run' per visualizzare il rendering del codice HTML.")
