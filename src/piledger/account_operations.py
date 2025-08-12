"""Module pour les opérations sur les comptes"""

class AccountManager:
    """Gestionnaire des comptes et calculs de solde"""
    def __init__(self, data):
        self.data = data
    
    def get_all_accounts(self):
        """Récupère tous les comptes uniques"""
        if not self.data:
            return []
        
        accounts = set()
        for transaction in self.data:
            compte = transaction.get('Compte', '').strip()
            if compte:  # Ne pas ajouter les comptes vides
                accounts.add(compte)
        
        return sorted(list(accounts))
    
    def calculate_balance(self, account_name):
        """Calcule le solde d'un compte spécifique"""
        if not self.data:
            return 0.0
        
        balance = 0.0
        for transaction in self.data:
            if transaction.get('Compte', '').strip() == account_name:
                try:
                    montant = float(transaction.get('Montant', '0'))
                    balance += montant
                except (ValueError, TypeError):
                    continue
        
        return balance

def validate_account_name(accounts, account_input):
    """Valide et trouve le nom de compte correspondant"""
    if not accounts or not account_input:
        return None
    
    account_input_lower = account_input.lower().strip()
    
    # Recherche exacte (insensible à la casse)
    for account in accounts:
        if account.lower() == account_input_lower:
            return account
    
    # Recherche partielle
    matches = []
    for account in accounts:
        if account_input_lower in account.lower():
            matches.append(account)
    
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        print(f"Plusieurs comptes trouvés: {', '.join(matches)}")
        print("Veuillez être plus spécifique.")
        return None
    
    return None