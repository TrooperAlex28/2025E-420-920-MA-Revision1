# Imports des classes et fonctions nécessaires
from .export_management import handle_export
from .data_handler import read_data_file
from .account_operations import AccountManager, validate_account_name
from .transaction_display import DisplayTransactions
from .statistics import Statistics, handle_statistics
from .search_operations import handle_date_search
from .ui_manager import UIManager
import os  # Nouvel import

def main(): 
    print("Chargement des données...")
    print(f"Répertoire de travail actuel: {os.getcwd()}")  # Ajouter import os en haut
    
    try:
        data = read_data_file()
        print(f"Debug - Type de data: {type(data)}")
        print(f"Debug - Valeur de data: {data}")
    except Exception as e:
        print(f"Erreur lors du chargement: {e}")
        return
    
    # ✅ Créer les instances une seule fois
    account_manager = AccountManager(data)
    display_manager = DisplayTransactions(data)
    stats_manager = Statistics(data)

    # Add null checks and error handling
    if data is None:
        print("❌ Erreur: Aucune donnée chargée!")
        return

    accounts = account_manager.get_all_accounts()
    if accounts is None:
        print("❌ Erreur: Impossible de récupérer les comptes!")
        accounts = []  # Fallback to empty list

    print(f"✅ {len(data)} transactions chargées avec succès!")
    print(f"✅ {len(accounts)} comptes détectés: {', '.join(accounts) if accounts else 'Aucun'}")
    
    running = True
    while running:
        UIManager(data).display_menu()
        
        try:
            choice = input("\nVotre choix: ").strip()
        except KeyboardInterrupt:
            print("\nAu revoir!")
            break
        
        if choice == "1":
            # ✅ Utiliser la fonction optimisée
            handle_balance_inquiry_optimized(account_manager, accounts)
        elif choice == "2":
            display_manager.display_all_transactions()
        elif choice == "3":
            print("\n--- Transactions par compte ---")
            print("Comptes disponibles:")
            for account in accounts:  
                print(f"  - {account}")
            
            account_input = input("\nEntrez le nom du compte: ").strip()
            
            if account_input:
                validated_account = validate_account_name(accounts, account_input)
                if validated_account:
                    display_manager.display_transactions_by_account(validated_account)
                else:
                    print(f"Compte '{account_input}' introuvable!")
            else:
                print("Nom de compte invalide!")
        elif choice == "4":
            display_manager.display_summary()
        elif choice == "5":
            # ✅ Corriger les paramètres de handle_statistics
            handle_statistics(data)  # Cette fonction n'attend qu'un seul paramètre
        elif choice == "6":
            handle_export(data, accounts)
        elif choice == "7":
            handle_date_search(data)
        elif choice == "0":
            print("\nMerci d'avoir utilisé le système de gestion comptable!")
            print("Au revoir!")
            running = False
        else:
            print("❌ Choix invalide! Veuillez sélectionner une option valide.")
        
        if running and choice != "0":
            input("\nAppuyez sur Entrée pour continuer...")

def handle_balance_inquiry_optimized(account_manager, accounts):
    """Version optimisée qui reçoit l'instance AccountManager"""
    print("\n--- Consultation de solde ---")
    print("Comptes disponibles:")
    for account in accounts:
        print(f"  - {account}")

    account_input = input("\nEntrez le nom du compte: ").strip()
    
    if not account_input:
        print("Nom de compte invalide!")
        return
    
    validated_account = validate_account_name(accounts, account_input)
    
    if validated_account:
        balance = account_manager.calculate_balance(validated_account)
        print(f"\nSolde du compte '{validated_account}': {balance:.2f}$")
    else:
        print(f"Compte '{account_input}' introuvable!")
        print("Vérifiez l'orthographe ou choisissez un compte dans la liste.")

if __name__ == "__main__":
    main()