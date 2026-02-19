raw_data_legacy = """
janis.berzins;IT;Admin;15.5h
peteris.k;HR;User;8h
anna_liepina;Finance;Manager;NULL
karlis.ozols;IT;User;240m
maris.ozolins;IT;Admin;1.5h
zane_v;Sales;User;45m
unknown_user;DevOps;SuperAdmin;N/A
Juris Kalns;IT;User;120m
evija.berzina;Marketing;Manager;2h
admin;IT;SuperAdmin;999h
"""

rows = raw_data_legacy.strip().split('\n')

for row in rows:
    parts = row.split(';')
    vards_raw = parts[0].replace('_', '.').replace(' ', '.')
    laiks_raw = parts[3]
    
    if 'h' in laiks_raw:
        laiks = float(laiks_raw.replace('h', ''))
    elif 'm' in laiks_raw:
        laiks = float(laiks_raw.replace('m', '')) / 60
    else:
        laiks = 0.0
        
    epasts = f"{vards_raw.lower()}@uznemums.lv"
    print(f"Lietotājs: {epasts} | Laiks: {laiks:.1f} h.")
