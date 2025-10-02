# Klasse als Data Dictionary
#
# AUTHOR Sven Schrodt
# SINCE 2025-09-26
class DD:

    pages = {
         "Sessions": "Sitzungsanalyse",
         "Sales": "Umsätze n. Vertriebskan.",
         "Upload" : "Dateiverwaltung",
         "Products": "Produkte"
    }

    col_transl = {
        "sess_ctry": "Land",
        "sess_loc": "Ort",  
        "datum": "Datum",
        "sug_platform": "Empfehlungsplattform",
        "landing_uri": "URI Landing Page",
        "session_duration": "Sitzungsdauer",
        "pages_per_sess": "Seiten je Sitzung",
        "jump_offs": "Absprünge",
        "sess_cart_add": "Sitzung: Artikel im Warenkorb",
        "sess_co": "Sitzung: Check-Out erreicht",
        "sess_co_done": "Sitzung: Check-Out abgeschlossen",
        "sessions": "Sitzungen",
        "Sitzung_min": "Sitzungsdauer[min.]",
    }

    session_y = ["jump_offs", "sess_cart_add", "sess_co", "sess_co_done", "sessions"]

    sales_chan_y = ["Vertriebskanal","Bestellungen","Bruttoumsatz","Rabatte","Rückgaben","Nettoumsatz","Versandgebühren","Steuern","Gesamtumsatz"]

# cloc --by-file --fullpath --match-d 'dash'
