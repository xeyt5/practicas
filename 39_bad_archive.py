import os

# lista de extensiones consideradas peligrosas
dangerous_extensions = [".exe", ".bat", ".sh", ".ps1", ".js", ".vbs", ".scr"]

path = input("Introduce la ruta de la carpeta a analizar: ")
if not os.path.isdir(path):
    print("La ruta no existe o no es una carpeta.")
    exit()

print("\n Analizando archivos...\n")

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isdir(full_path):
        continue

    alerts = []

    if file.startswith("."):
        alerts.append("archivo oculto")

    if file.count(".") >= 2:
        alerts.append("doble extensión")

    for ext in dangerous_extensions:
        if file.lower().endswith(ext):
            alerts.append(f"extensión peligrosa ({ext})")

    if alerts:
        print(f"{file}")
        for alert in alerts:
            print(f"   - {alert}")
