firewall_rules = {
    "192.168.1.5": ["SSH", "HTTP"],
    "LV": ["HTTP", "HTTPS"],
    "EE": ["HTTP"],
    "Blocklist": ["10.10.10.10", "RU", "CN"]
}

network_traffic = [
    {"ip": "192.168.1.5", "country": "LV", "service": "SSH"},
    {"ip": "85.254.1.1",  "country": "LV", "service": "HTTP"},
    {"ip": "10.10.10.10", "country": "US", "service": "HTTP"},
    {"ip": "5.5.5.5",      "country": "RU", "service": "SSH"},
    {"ip": "2.2.2.2",      "country": "EE", "service": "HTTPS"},
    {"ip": "8.8.8.8",      "country": "US", "service": "DNS"}
]

for packet in network_traffic:
    ip = packet["ip"]
    country = packet["country"]
    service = packet["service"]
    status = "DENY"

    if ip in firewall_rules["Blocklist"] or country in firewall_rules["Blocklist"]:
        status = "DENY"
    
    elif ip in firewall_rules:
        if service in firewall_rules[ip]:
            status = "ALLOW"
        else:
            status = "DENY"
            
    elif country in firewall_rules:
        if service in firewall_rules[country]:
            status = "ALLOW"
        else:
            status = "DENY"
    
    else:
        status = "DENY"

    print(f"[{status}] {ip} > {service}")
