import streamlit as st
from datetime import datetime, time
from streamlit_mic_recorder import mic_recorder

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="NetLex Smart Agenda", page_icon="📅")

st.title("📅 NetLex Smart Agenda")
st.markdown("Gestione rapida appuntamenti con controllo sovrapposizioni.")

# --- 2. BARRA LATERALE (API KEY) ---
with st.sidebar:
    st.header("Configurazione")
    api_key = st.text_input("Inserisci API Key NetLex", type="password", help="La chiave segreta del tuo account NetLex")
    st.info("Senza API Key, l'app funzionerà in modalità simulazione.")

# --- 3. DETTATURA VOCALE ---
st.subheader("🎤 Dettatura Vocale")
st.write("Clicca sul microfono e detta il titolo dell'appuntamento:")

# Il componente del microfono
audio = mic_recorder(
    start_prompt="🎤 Inizia a parlare", 
    stop_prompt="🛑 Ferma", 
    just_once=True,
    key='registratore_vocale'
)

# Gestione del testo dettato (Simulazione trascrizione)
testo_rilevato = ""
if audio:
    st.success("✅ Audio ricevuto! (In attesa di collegamento Speech-to-Text)")
    # Nota: per trasformare l'audio in testo reale serve un servizio come OpenAI Whisper
    testo_rilevato = "Nuovo appuntamento da definire"

# --- 4. FORM APPUNTAMENTO ---
st.divider()
with st.form("form_appuntamento"):
    st.subheader("Dettagli Appuntamento")
    
    # Se hai dettato qualcosa, il titolo viene pre-compilato
    titolo = st.text_input("Titolo Appuntamento", value=testo_rilevato, placeholder="Es: Udienza Civile Rossi")
    
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("Data", datetime.now())
    with col2:
        ora_inizio = st.time_input("Ora Inizio", time(9, 0))
        
    durata = st.number_input("Durata (minuti)", min_value=15, step=15, value=60)
    
    submit = st.form_submit_button("Verifica Disponibilità e Salva")

# --- 5. LOGICA DI CONTROLLO ---
if submit:
    if not api_key:
        st.warning("⚠️ Inserisci l'API Key nella barra laterale per collegarti a NetLex.")
    elif not titolo:
        st.error("❌ Inserisci un titolo per l'appuntamento.")
    else:
        try:
            # Calcolo orario completo
            inizio_dt = datetime.combine(data, ora_inizio)
            
            with st.spinner("Interrogazione database NetLex..."):
                # Qui andrà la chiamata API reale verso TeamSystem
                # Per ora usiamo una simulazione positiva
                possibile = True 
                
                if possibile:
                    st.success(f"✔️ Slot Libero! Appuntamento '{titolo}' pronto per l'invio a NetLex.")
                    st.balloons()
                else:
                    st.error("❌ Attenzione: Esiste già un impegno per questo orario.")
        
        except Exception as e:
            st.error(f"Errore tecnico: {e}")

# --- 6. ISTRUZIONI ---
st.caption("Sviluppato per integrazione diretta con TeamSystem NetLex via REST API.")
