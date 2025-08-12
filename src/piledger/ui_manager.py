"""Module pour l'interface utilisateur"""

from piledger.account_operations import AccountManager


class UIManager:
    """Gestionnaire de l'interface utilisateur"""
    def __init__(self, data):
        self.data = data
        self.account_manager = AccountManager(data)

    def display_menu(self):
        print("\n" + "="*50)
        print("SYSTÈME DE GESTION COMPTABLE PERSONNEL")
        print("="*50)
        print("1. Afficher le solde d'un compte")
        print("2. Afficher toutes les transactions")
        print("3. Afficher les transactions d'un compte")
        print("4. Afficher le résumé de tous les comptes")
        print("5. Afficher les statistiques")
        print("6. Exporter les écritures d'un compte")
        print("7. Rechercher par période")
        print("0. Quitter")
        print("="*50)
        