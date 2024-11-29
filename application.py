import tkinter
import tkinter.messagebox
import customtkinter as ctk

# Configurer l'apparence et le thème
ctk.set_appearance_mode("System")  # Peut être "System", "Dark", ou "Light"
ctk.set_default_color_theme("theme.json")  # Spécifiez le chemin correct vers le fichier du thème

# Définition de la classe principale
class App(ctk.CTk):  # Correction : Suppression des parenthèses ici
    def __init__(self):
        super().__init__()
        
        self.title("Trade managing")
        self.geometry(f"{1100}x{580}")  # Configuration de la taille de la fenêtre
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)
        
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        
        

# Point d'entrée principal
if __name__ == "__main__":
    app = App()
    app.mainloop()
