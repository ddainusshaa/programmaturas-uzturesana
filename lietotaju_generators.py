new_employees = [
    {"name": "Liga Berzina", "dept": "HR", "admin": False},
    {"name": "Janis Ozols",  "dept": "IT", "admin": True},
    {"name": "Andris Liepa", "dept": "IT", "admin": False},
    {"name": "Ilze Kalna",   "dept": "Finance", "admin": False},
    {"name": "Karlis Krumins", "dept": "IT", "admin": True},
    {"name": "Martins Zalite", "dept": "Finance", "admin": False},
    {"name": "Baiba Ozola", "dept": "HR", "admin": False},
    {"name": "Viktors Koks", "dept": "IT", "admin": False},
    {"name": "Sanda Liepina", "dept": "Finance", "admin": True}
]

print("#!/bin/bash\n")

for emp in new_employees:
    name_parts = emp["name"].lower().split()
    username = name_parts[0][0] + name_parts[1]
    if emp["dept"] == "IT":
        groups = "wheel,developers"
    else:
        groups = "staff"
    print(f"useradd -m -G {groups} {username}")
    print(f"echo {username}:DEFAULT | chpasswd")
    if emp["admin"]:
        print(f"passwd -e {username}")
