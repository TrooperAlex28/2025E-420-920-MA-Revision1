# Imports des classes et fonctions nécessaires
from .export_management import handle_export
from .account_manager import (
    read_data_file,
    AccountManager, 
    DisplayTransactions,
    Statistics,
    UIManager,
    handle_balance_inquiry,
    handle_statistics,
    handle_date_search,
    validate_account_name,  # ✅ Déjà définie dans account_manager.py
)

def main():
    print("Chargement des données...")
    data = read_data_file()
    account_manager = AccountManager(data)
    accounts = account_manager.get_all_accounts()
    
    # Créer les instances une fois pour toute la session
    display_manager = DisplayTransactions(data)
    stats_manager = Statistics(data)
    
    print(f"✅ {len(data)} transactions chargées avec succès!")
    
    running = True
    while running:
        UIManager(data).display_menu()
        
        try:
            choice = input("\nVotre choix: ").strip()
        except:
            print("\nAu revoir!")
            break
        
        if choice == "1":
            handle_balance_inquiry(data, accounts)
        elif choice == "2":
            display_manager.display_all_transactions()
        elif choice == "3":
            print("\n--- Transactions par compte ---")
            print("Comptes disponibles:")
            i = 0
            while i < len(accounts):
                print(f"  - {accounts[i]}")
                i += 1
            
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
            handle_statistics(data)
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

if __name__ == "__main__":
    main()