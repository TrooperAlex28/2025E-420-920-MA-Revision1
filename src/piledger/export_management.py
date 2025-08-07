import csv

def validate_account_name(accounts, account_name):
    """Fonction standalone pour valider un nom de compte."""
    for account in accounts:
        if account.lower() == account_name.lower():
            return account
    return None

class ExportTransactions:
    def __init__(self, data):
        self.data = data

    def get_all_accounts(self):
        """Obtient tous les comptes uniques depuis les données."""
        accounts = set(transaction.compte for transaction in self.data)
        return list(accounts)

    def validate_account_name(self, account_name):
        """Valide un nom de compte (insensible à la casse)."""
        all_accounts = self.get_all_accounts()
        
        for account in all_accounts:
            if account.lower() == account_name.lower():
                return account
        return None

    def export_account_postings(self, account_name, filename):
        """Exporte les écritures d'un compte vers un fichier CSV."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['No txn', 'Date', 'Compte', 'Montant', 'Commentaire']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                exported_count = 0
                for transaction in self.data:
                    if transaction.compte == account_name:
                        writer.writerow({
                            'No txn': transaction.no_txn,
                            'Date': transaction.date,
                            'Compte': transaction.compte,
                            'Montant': transaction.montant,
                            'Commentaire': transaction.commentaire
                        })
                        exported_count += 1
                
                if exported_count > 0:
                    print(f"✅ {exported_count} écritures du compte '{account_name}' exportées vers '{filename}'")
                else:
                    print(f"⚠️  Aucune écriture trouvée pour le compte '{account_name}'")
                    
        except Exception as e:
            print(f"❌ Erreur lors de l'exportation: {e}")

def handle_export(data, accounts):
    """Gère le processus d'exportation des écritures d'un compte."""
    print("\n--- Exportation ---")
    print("Comptes disponibles:")
    for account in accounts:
        print(f"  - {account}")
    
    account_input = input("\nEntrez le nom du compte à exporter: ").strip()
    
    if not account_input:
        print("Nom de compte invalide!")
        return
    
    validated_account = validate_account_name(accounts, account_input)
    
    if validated_account:
        filename = input("Nom du fichier de sortie (ex: export.csv): ").strip()
        if not filename:
            filename = f"export_{validated_account.replace(' ', '_').lower()}.csv"
        
        # Ajouter .csv si pas d'extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        exporter = ExportTransactions(data)
        exporter.export_account_postings(validated_account, filename)
    else:
        print(f"Compte '{account_input}' introuvable!")


