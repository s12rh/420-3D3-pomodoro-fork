import tkinter as tk
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        """Met à jour l'affichage de l'état (Travail ou Pause)."""
        donnees = sujet.get_donnees()
        etat = donnees["etat"]
        self._label.config(text=etat)
        self._label.config(fg="blue" if etat == "Pause" else "black")
        
