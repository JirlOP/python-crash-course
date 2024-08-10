from pathlib import Path
import json

path = Path("data.json")

nombre = "Jorge"
apellido = "Sagot"
gustos = ["Python", "Java", "C++"]

contents = {
    "nombre": nombre,
    "apellido": apellido,
    "gustos": gustos
}

path.write_text(json.dumps(contents))

# now read the file
contents = json.load(path.open())
# format the output
print(f"Nombre: {contents['nombre']}")
print(f"Apellido: {contents['apellido']}")
print("Gustos:")
for gusto in contents['gustos']:
    print(f"\t{gusto}")
