if submit:
    url_script = "INCOLLA_QUI_URL_DI_GOOGLE_SCRIPT"
    dati = {
        "titolo": titolo,
        "dataOra": f"{data}T{ora}",
        "netlexKey": netlex_key
    }
    
    # Questo invia tutto al tuo Google Script che fa il lavoro sporco
    risposta = requests.post(url_script, json=dati)
    
    if risposta.status_code == 200:
        st.success("✅ Sincronizzato su Google Calendar e NetLex via Script!")
        st.balloons()
