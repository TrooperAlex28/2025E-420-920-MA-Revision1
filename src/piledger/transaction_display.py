"""Module pour l'affichage des transactions"""

from piledger.account_operations import AccountManager

class DisplayTransactions:
    """Gestionnaire d'affichage des transactions"""
    def __init__(self, data):
        self.data = data

    def display_all_transactions(self):
        """Affiche toutes les transactions"""
        print("\n--- Toutes les transactions ---")
        print(f"Total: {len(self.data)} transactions")
        print("-" * 80)
        
        for transaction in self.data:
            # Use dictionary key access instead of attribute access
            print(f"Transaction {transaction['No txn']} - {transaction['Date']}")
            print(f"  Compte: {transaction['Compte']}")
            print(f"  Montant: {transaction['Montant']}$")
            if transaction['Commentaire']:
                print(f"  Commentaire: {transaction['Commentaire']}")
            print("-" * 40)
    
    def display_transactions_by_account(self, account_name):
        print(f"\n=== TRANSACTIONS POUR LE COMPTE '{account_name}' ===")
        found_any = False
        for transaction in self.data:
            if transaction['Compte'] == account_name:
                found_any = True
                print(f"Transaction {transaction['No txn']} - {transaction['Date']}")
                print(f"  Montant: {transaction['Montant']}$")
                if transaction['Commentaire']:
                    print(f"  Commentaire: {transaction['Commentaire']}")
                print()
        if not found_any:
            print(f"Aucune transaction trouvée pour le compte '{account_name}'")

    
    def display_summary(self):
        print("\n=== RÉSUMÉ DES COMPTES ===")
        accounts = AccountManager(self.data).get_all_accounts()
        for account in accounts:
            balance = AccountManager(self.data).calculate_balance(account)
            print(f"{account}: {balance:.2f}$")
