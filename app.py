import streamlit as st
from streamlit_ace import st_ace

# Titolo della web app
st.title("Live HTML Editor 📝")

# Creazione di due colonne (Editor a sinistra, Anteprima a destra)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Scrivi il tuo codice HTML")
    
    # Editor di codice con evidenziazione della sintassi
    html_code = st_ace(
        value="<h1>Hello, World!</h1>\n<p>Scrivi il tuo codice HTML qui...</p>",
        language="html",
        theme="monokai",  # Puoi provare anche "github", "tomorrow_night", "solarized_light", ecc.
        font_size=14,
        tab_size=4,
        height=500
    )

    # Input per il nome del file
    file_name = st.text_input("Nome del file (senza estensione):", value="mio_file")

    # Bottone per eseguire il codice
    run_code = st.button("▶️ Run")

    # Bottone per scaricare il file
    if st.button("💾 Download"):
        if not file_name.strip():
            st.warning("⚠️ Inserisci un nome valido per il file!")
        else:
            st.download_button(label="📥 Scarica il codice HTML",
                               data=html_code,
                               file_name=f"{file_name}.html",
                               mime="text/html")

with col2:
    st.subheader("🌐 Anteprima")
    
    # Esegui il codice solo se l'utente preme il pulsante "Run"
    if run_code:
        html_with_style = f"""
        <div style="background-color: white; padding: 20px; height:100%;">
            {html_code}
        </div>
        """
        st.components.v1.html(html_with_style, height=500, scrolling=True)
    else:
        st.info("Premi 'Run' per visualizzare il rendering del codice HTML.")
