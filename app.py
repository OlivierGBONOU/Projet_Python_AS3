from PIL import Image
from customtkinter import *
import customtkinter as ctk

set_default_color_theme("theme.json")

# Define the appearance mode (light theme)
ctk.set_appearance_mode("light")  # Set the application to light mode

def show_frame(frame):
    for f in frames.values():
        f.pack_forget()
    frames[frame].pack(fill="both", expand=True)

# Initialize main window
app = ctk.CTk()
app.geometry("900x600")
app.title("Application de Gestion Commerciale")

# Configure grid layout
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Sidebar menu
sidebar = ctk.CTkFrame(app, width=200)
sidebar.grid(row=0, column=0, sticky="we")

# Charger l'image du logo
logo = Image.open("lion.png")

# Redimensionner l'image à une taille beaucoup plus grande (par exemple, 5000x5000 pixels)
logo_resized = logo.resize((5000, 5000))  # Augmentation significative de la taille

# Créer l'objet CTkImage avec l'image redimensionnée
logo_image = ctk.CTkImage(light_image=logo_resized, size=(250, 250))  # Définir une taille d'affichage raisonnable

# Créer un label avec l'image redimensionnée
logo_label = ctk.CTkLabel(sidebar, image=logo_image, text="")
logo_label.pack(pady=40)  # Espace pour le logo

# Buttons for the sidebar
buttons = [
    ("Acceuil", lambda: show_frame("acceuil")),
    ("Stock", lambda: show_frame("stock")),
    ("Commandes", lambda: show_frame("commandes")),
    ("Ventes", lambda: show_frame("ventes")),
    ("Fournisseurs", lambda: show_frame("fournisseurs")),
    ("Factures", lambda: show_frame("factures")),
    ("Analyses de données", lambda: show_frame("analyses"))
]

# Create buttons
for text, command in buttons:
    btn = ctk.CTkButton(sidebar, text=text, command=command)
    btn.pack(pady=15, padx=10, fill="y")

# Main content area (frames)
frames = {}
content_area = ctk.CTkFrame(app)
content_area.grid(row=0, column=1, sticky="nswe")

# Create frames for each section
for frame_name in ["acceuil", "stock", "commandes", "ventes", "fournisseurs", "factures", "analyses"]:
    frame = ctk.CTkFrame(content_area)
    frames[frame_name] = frame

# Acceuil Frame
acceuil_frame = ctk.CTkLabel(frames["acceuil"], text="Acceuil", font=("Arial", 20))
acceuil_frame.pack(pady=20)

# Stock Frame
stock_label = ctk.CTkLabel(frames["stock"], text="Gestion des Stocks", font=("Arial", 20))
stock_label.pack(pady=20)

# Commandes Frame
commandes_label = ctk.CTkLabel(frames["commandes"], text="Formulaire de Commande", font=("Arial", 20))
commandes_label.pack(pady=20)

# Ventes Frame
ventes_label = ctk.CTkLabel(frames["ventes"], text="Gestion des Ventes", font=("Arial", 20))
ventes_label.pack(pady=20)

# Fournisseurs Frame
fournisseurs_label = ctk.CTkLabel(frames["fournisseurs"], text="Gestion des Fournisseurs", font=("Arial", 20))
fournisseurs_label.pack(pady=20)

# Factures Frame
factures_label = ctk.CTkLabel(frames["factures"], text="Gestion des Factures", font=("Arial", 20))
factures_label.pack(pady=20)

# Analyses de Données Frame
analyses_label = ctk.CTkLabel(frames["analyses"], text="Analyses de Données", font=("Arial", 20))
analyses_label.pack(pady=20)

# Show initial frame
show_frame("acceuil")

# Run the application
app.mainloop()