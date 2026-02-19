service_health = [
    {"service": "Database", "status": "UP", "latency_ms": 15},
    {"service": "Database", "status": "UP", "latency_ms": 20},
    {"service": "Database", "status": "UP", "latency_ms": 850},
    {"service": "Web",      "status": "UP", "latency_ms": 10},
    {"service": "Web",      "status": "DOWN", "latency_ms": 0},
    {"service": "Web",      "status": "UP", "latency_ms": 900},
    {"service": "Backup",   "status": "UP", "latency_ms": 100},
    {"service": "Backup",   "status": "DOWN", "latency_ms": 0},
    {"service": "API",      "status": "UP", "latency_ms": 45},
    {"service": "API",      "status": "UP", "latency_ms": 600}
]

stats = {}

for entry in service_health:
    name = entry["service"]
    status = entry["status"]
    latency = entry["latency_ms"]
    
    if name not in stats:
        stats[name] = {"total": 0, "ok": 0}
    stats[name]["total"] += 1
    if status == "UP" and latency < 500:
        stats[name]["ok"] += 1

for name, data in stats.items():
    uptime_pct = (data["ok"] / data["total"]) * 100
    print(f"Serviss: {name} | Uptime: {uptime_pct:.1f}%")
