import tkinter as tk 
import requests 
from io import BytesIO 
from PIL import Image, ImageTk  

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon//{nombre_pokemon}"
    response = requests.get(url) 
    
    if response.status_code==200: 
        data = response.json()
        nombre = data["name"]
        numero = data["id"]
        tipos = [tipos["type"]["name"] for tipos in data["types"]] 
        resultado = f"Nombre: {nombre}\n Número del pokemon: {numero}\n Tipo(s): {', '.join(tipos)}"

        imagen_url = data["sprites"]["front_default"]

        response_imagen = requests.get(imagen_url) 
        imagen = Image.open(BytesIO(response_imagen.content)) 
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen) 
        label_imagen.config(image=foto)
        label_imagen.image = foto 
    else:
        resultado = "No se encontró el pokemon"
        label_imagen.config(image=None) 
    label_resultado.config(text=resultado) 
window = tk.Tk()
window.title("Buscador de pokemon")
entry_pokemon = tk.Entry(window)
entry_pokemon.pack() 
button_buscar =tk.Button(window, text="Buscar", command=buscar_pokemon)
button_buscar.pack()
label_resultado = tk.Label(window, text="")
label_resultado.pack()
label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop() 