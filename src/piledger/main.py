import sys
import os
import csv


# Classe Transaction
class Transaction:
    def __init__(self, no_txn, date, compte, montant, commentaire):
        self.no_txn = int(no_txn)
        self.date = date
        self.compte = compte
        self.montant = float(montant)
        self.commentaire = commentaire

class AccountManager:
    def __init__(self, transactions):
        self.transactions = transactions

    def calculate_balance(self, account_name):
        return sum(txn.montant for txn in self.transactions if txn.compte == account_name)

    def get_all_accounts(self):
        accounts = set(txn.compte for txn in self.transactions)
        return list(accounts)
    
def read_data_file():
    transactions = []
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for line_num, row in enumerate(reader, start=2):  # Start at 2 because we skip header
                if len(row) >= 5:
                    try:
                        transaction = Transaction(
                            no_txn=row[0],
                            date=row[1],
                            compte=row[2],
                            montant=row[3],
                            commentaire=row[4]
                        )
                        transactions.append(transaction)
                    except ValueError as e:
                        print(f"⚠️  Ligne {line_num} ignorée: {e}")
                        continue
                        
    except FileNotFoundError:
        print("❌ ERREUR: Le fichier data.csv est introuvable!")
        return []
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier: {e}")
        return []
    
    return transactions

class Balance: 
    def __init__(self, data):
        self.data = data

    def calculate_balance(self, account_name):
        balance = 0.0
        i = 0
        while i < len(self.data):
            transaction = self.data[i]
            if transaction.compte == account_name:
                balance += transaction.montant
            i += 1
        return balance

class GetAllAccounts:
    def __init__(self, data):
        self.data = data
    def get_all_accounts(self):
        accounts = []
        i = 0
        while i < len(self.data):
            transaction = self.data[i]
            account = transaction.compte  # Utilisation de la notation par point
            found = False
            j = 0
            while j < len(accounts):
                if accounts[j] == account:
                    found = True
                    break
                j += 1
            if not found:
                accounts.append(account)
            i += 1
        return accounts

class DisplayTransactions:
    def __init__(self, data):
        self.data = data
    def display_all_transactions(self):
        print("\n=== TOUTES LES TRANSACTIONS ===")
        for transaction in self.data:
            print(f"Transaction {transaction.no_txn} - {transaction.date}")
            print(f"  Compte: {transaction.compte}")
            print(f"  Montant: {transaction.montant:.2f}$")
        if transaction.commentaire:
            print(f"  Commentaire: {transaction.commentaire}")
        print()

    def display_transactions_by_account(self, account_name):
        print(f"\n=== TRANSACTIONS POUR LE COMPTE '{account_name}' ===")
        found_any = False
        for transaction in self.data:
            if transaction.compte == account_name:
                found_any = True
                print(f"Transaction {transaction.no_txn} - {transaction.date}")
                print(f"  Montant: {transaction.montant:.2f}$")
                if transaction.commentaire:
                    print(f"  Commentaire: {transaction.commentaire}")
                print()
        if not found_any:
            print(f"Aucune transaction trouvée pour le compte '{account_name}'")

    def display_summary(self):
        print("\n=== RÉSUMÉ DES COMPTES ===")
        accounts = GetAllAccounts(self.data).get_all_accounts()
        i = 0
        for account in accounts:
            balance = Balance(self.data).calculate_balance(account)
            print(f"{account}: {balance:.2f}$")



def get_transactions_by_date_range(self, start_date, end_date):
    filtered_transactions = []
    for transaction in self.data:
        if start_date <= transaction.date <= end_date:
            filtered_transactions.append(transaction)
    return filtered_transactions

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def find_largest_expense(self):
        largest_expense = None
        max_amount = 0
        for transaction in self.data:
            if transaction.montant > max_amount and transaction.compte != 'Compte courant' and transaction.compte != 'Revenu':
                max_amount = transaction.montant
                largest_expense = transaction
        return largest_expense
    
    def find_total_income(self):
        total = 0
        for transaction in self.data:
            if transaction.compte == 'Revenu':
                total += abs(transaction.montant)
        return total
    
    def find_total_expenses(self):
        total = 0
        for transaction in self.data:
            if transaction.compte != 'Compte courant' and transaction.compte != 'Revenu' and transaction.montant > 0:
                total += transaction.montant
        return total

class ExportTransactions:
    def __init__(self, data):
        self.data = data

    def export_account_postings(self, account_name, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("No txn,Date,Compte,Montant,Commentaire\n")
            for transaction in self.data:
                if transaction.compte == account_name:
                    line = f"{transaction.no_txn},{transaction.date},{transaction.compte},{transaction.montant},{transaction.commentaire}\n"
                    file.write(line)
        print(f"Écritures exportées vers {filename}")

    def validate_account_name(self, account_name):
        # Obtenir tous les comptes uniques
        all_accounts = GetAllAccounts(self.data).get_all_accounts()
        
        # Chercher une correspondance (insensible à la casse)
        for account in all_accounts:
            if account.lower() == account_name.lower():
                return account
        return None
        

def __init__(self, data):
    self.data = data
    self.account_manager = AccountManager(data)

class UIManager:
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

def handle_balance_inquiry(data, accounts):
    print("\n--- Consultation de solde ---")
    print("Comptes disponibles:")
    i = 0
    while i < len(accounts):
        print(f"  - {accounts[i]}")
        i += 1
    
    account_input = input("\nEntrez le nom du compte: ").strip()
    
    if not account_input:
        print("Nom de compte invalide!")
        return
    
    validated_account = ExportTransactions(data).validate_account_name(account_input)
    
    if validated_account:
        balance = Balance(data).calculate_balance(validated_account)
        print(f"\nSolde du compte '{validated_account}': {balance:.2f}$")
        
    else:
        print(f"Compte '{account_input}' introuvable!")
        print("Vérifiez l'orthographe ou choisissez un compte dans la liste.")

def handle_statistics(data):
    print("\n=== STATISTIQUES FINANCIÈRES ===")
    
    # Créer une instance de Balance
    balance_calculator = Balance(data)
    
    # Appeler la méthode via l'instance
    current_account_balance = balance_calculator.calculate_balance('Compte courant')
    print(f"\nSolde du compte courant: {current_account_balance:.2f}$")

def handle_date_search(data):
    print("\n--- Recherche par période ---")
    start_date = input("Date de début (YYYY-MM-DD): ").strip()
    end_date = input("Date de fin (YYYY-MM-DD): ").strip()
    
    if not start_date or not end_date:
        print("Dates invalides!")
        return
    
    filtered_data = get_transactions_by_date_range(data, start_date, end_date)
    
    if len(filtered_data) == 0:
        print(f"Aucune transaction trouvée entre {start_date} et {end_date}")
    else:
        print(f"\n{len(filtered_data)} écritures(s) trouvée(s) entre {start_date} et {end_date}:")
        i = 0
        while i < len(filtered_data):
            transaction = filtered_data[i]
            print(f"  {transaction.date} - {transaction.compte}: {transaction.montant:.2f}$")
            i += 1

def validate_account_name(accounts, account_name):
    """Valide un nom de compte (insensible à la casse)"""
    for account in accounts:
        if account.lower() == account_name.lower():
            return account
    return None

def handle_export(data, accounts):
    print("\n--- Exportation ---")
    print("Comptes disponibles:")
    for account in accounts:  # ✅ Plus pythonique que while
        print(f"  - {account}")
    
    account_input = input("\nEntrez le nom du compte à exporter: ").strip()
    
    if not account_input:
        print("Nom de compte invalide!")
        return
    
    # ✅ Utiliser la fonction standalone
    validated_account = validate_account_name(accounts, account_input)
    
    if validated_account:
        filename = input("Nom du fichier de sortie (ex: export.csv): ").strip()
        if not filename:
            filename = f"export_{validated_account.replace(' ', '_').lower()}.csv"
        
        # ✅ Créer une instance pour l'exportation
        exporter = ExportTransactions(data)
        exporter.export_account_postings(validated_account, filename)
    else:
        print(f"Compte '{account_input}' introuvable!")


def main():
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