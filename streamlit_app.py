import streamlit as st
from openai import OpenAI  # <--- Nuova libreria
from streamlit_mic_recorder import mic_recorder
import io

# --- CONFIGURAZIONE NEI "SECRETS" DI STREAMLIT ---
# Incolla la tua chiave OpenAI nelle impostazioni (Settings > Secrets) di Streamlit Cloud
# openai_key = st.secrets["OPENAI_API_KEY"]
# client = OpenAI(api_key=openai_key)

st.subheader("🎤 Dettatura Vocale Real-Time")

audio = mic_recorder(
    start_prompt="Inizia a parlare", 
    stop_prompt="Smetti e Trascrivi", 
    just_once=True,
    key='registratore_reale'
)

testo_rilevato = ""

if audio:
    try:
        # Trasformiamo i dati audio in un file "virtuale" che OpenAI può leggere
        audio_bio = io.BytesIO(audio['bytes'])
        audio_bio.name = "audio.wav"
        
        with st.spinner("Trascrizione in corso..."):
            # Chiamata a OpenAI Whisper
            # NOTA: Assicurati di avere la chiave configurata
            if "OPENAI_API_KEY" in st.secrets:
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                response = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_bio,
                    language="it"  # Forza la lingua italiana
                )
                testo_rilevato = response.text
                st.success(f"Ho capito: {testo_rilevato}")
            else:
                st.error("Manca la chiave OPENAI_API_KEY nei Secrets di Streamlit!")
                
    except Exception as e:
        st.error(f"Errore nella trascrizione: {e}")

# Poi il testo_rilevato andrà automaticamente nel campo Titolo
titolo = st.text_input("Titolo Appuntamento", value=testo_rilevato)
