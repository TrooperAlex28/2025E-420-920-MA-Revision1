"""Module pour les statistiques"""

from piledger.account_operations import AccountManager


class Statistics:
    """Gestionnaire des statistiques"""
    def __init__(self, data):
        self.data = data
    
    def find_total_income(self):
        """Calcule le total des revenus"""
        total = 0.0
        for transaction in self.data:
            # Use dictionary key access instead of attribute access
            if transaction['Compte'] == 'Revenu':
                # Convert string to float and make negative values positive for income
                amount = float(transaction['Montant'])
                if amount < 0:
                    total += abs(amount)  # Convert negative to positive
                else:
                    total += amount
        return total
    
    def find_total_expenses(self):
        """Calcule le total des dépenses"""
        total = 0.0
        expense_accounts = ['Épicerie', 'Transport', 'Divertissement', 'Loyer']
        
        for transaction in self.data:
            # Use dictionary key access instead of attribute access
            if transaction['Compte'] in expense_accounts:
                amount = float(transaction['Montant'])
                if amount > 0:  # Positive amounts are expenses
                    total += amount
        return total


def handle_statistics(data):
    """Gère l'affichage des statistiques"""
    stats = Statistics(data)
    
    print("\n=== STATISTIQUES ===")
    total_income = stats.find_total_income()
    total_expenses = stats.find_total_expenses()
    net_result = total_income - total_expenses
    
    print(f"Total des revenus: {total_income:.2f}$")
    print(f"Total des dépenses: {total_expenses:.2f}$")
    print(f"Résultat net: {net_result:.2f}$")
    
    if net_result > 0:
        print("✅ Vous avez un excédent!")
    elif net_result < 0:
        print("⚠️ Vous avez un déficit!")
    else:
        print("⚖️ Vous êtes à l'équilibre!")
