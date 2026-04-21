import streamlit as st
from datetime import datetime, time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="NetLex Agenda", page_icon="📅")

st.title("📅 NetLex Smart Agenda")
st.markdown("Inserimento rapido appuntamenti con verifica disponibilità.")

# --- 2. BARRA LATERALE (NETLEX API) ---
with st.sidebar:
    st.header("Connessione NetLex")
    # Qui userai la chiave che ti fornirà TeamSystem
    api_key_netlex = st.text_input("Inserisci API Key NetLex", type="password")
    st.divider()
    st.info("L'app verificherà in tempo reale se lo slot è libero sul tuo database NetLex.")

# --- 3. FORM APPUNTAMENTO ---
# Usiamo un modulo (form) per inviare i dati tutti insieme
with st.form("form_netlex"):
    st.subheader("Nuovo Impegno")
    
    # Campo Titolo: su Android puoi usare il microfono della tastiera qui
    titolo = st.text_input("Titolo Appuntamento", placeholder="Es: Incontro Cliente Rossi / Udienza")
    
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("Data Appuntamento", datetime.now())
    with col2:
        ora_inizio = st.time_input("Ora Inizio", time(9, 0))
    
    durata = st.select_slider(
        "Durata stimata (minuti)",
        options=[15, 30, 45, 60, 90, 120],
        value=60
    )
    
    st.divider()
    submit = st.form_submit_button("Verifica e Salva in Agenda")

# --- 4. LOGICA DI FUNZIONAMENTO ---
if submit:
    if not api_key_netlex:
        st.error("⚠️ Errore: Inserisci la chiave API di NetLex nella barra laterale.")
    elif not titolo:
        st.warning("⚠️ Per favore, inserisci un titolo per l'appuntamento.")
    else:
        # Qui l'app fa il suo lavoro
        try:
            with st.spinner("Connessione a NetLex in corso..."):
                # Simulazione del controllo disponibilità
                # In futuro, qui inseriremo la chiamata API reale
                successo = True 
                
                if successo:
                    st.success(f"✅ Slot libero! L'appuntamento '{titolo}' è stato registrato.")
                    st.balloons()
                else:
                    st.error("❌ Errore: Lo slot selezionato è già occupato in agenda.")
                    
        except Exception as e:
            st.error(f"Si è verificato un problema tecnico: {e}")

# --- 5. FOOTER ---
st.caption("Interfaccia ottimizzata per dispositivi Android - Collegamento REST API NetLex")
