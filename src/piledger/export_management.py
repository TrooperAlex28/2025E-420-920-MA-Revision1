"""Module pour la gestion des exports"""
import csv
import os

def handle_export(data, accounts):
    """Gère l'exportation des données d'un compte"""
    print("\n--- Export des transactions ---")
    print("Comptes disponibles:")
    for account in accounts:
        print(f"  - {account}")
    
    account_name = input("\nEntrez le nom du compte à exporter: ").strip()
    if not account_name:
        print("❌ Nom de compte invalide!")
        return
    
    # Validate account name
    validated_account = None
    for account in accounts:
        if account.lower() == account_name.lower():
            validated_account = account
            break
    
    if not validated_account:
        print(f"❌ Compte '{account_name}' introuvable!")
        return
    
    filename = input("Nom du fichier de sortie (ex: export.csv): ").strip()
    if not filename:
        print("❌ Nom de fichier invalide!")
        return
    
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    try:
        export_account_transactions(data, validated_account, filename)
        print(f"✅ Export réussi vers '{filename}'")
    except Exception as e:
        print(f"❌ Erreur lors de l'exportation: {e}")

def export_account_transactions(data, account_name, filename):
    """Exporte les transactions d'un compte vers un fichier CSV"""
    # Filter transactions for the specified account
    account_transactions = []
    for transaction in data:
        # Use dictionary key access instead of attribute access
        if transaction['Compte'] == account_name:
            account_transactions.append(transaction)
    
    if not account_transactions:
        raise ValueError(f"Aucune transaction trouvée pour le compte '{account_name}'")
    
    # Write to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['No txn', 'Date', 'Compte', 'Montant', 'Commentaire']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for transaction in account_transactions:
            writer.writerow(transaction)
    
    print(f"✅ {len(account_transactions)} transactions exportées pour le compte '{account_name}'")


