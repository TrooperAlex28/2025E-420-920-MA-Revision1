"""Module pour les opérations de recherche"""
def get_transactions_by_date_range(data, start_date, end_date):
    filtered_transactions = []
    for transaction in data:
        # Use correct key name "Date" instead of "date"
        if start_date <= transaction["Date"] <= end_date:
            filtered_transactions.append(transaction)
    return filtered_transactions

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
        for transaction in filtered_data:
            print(f"  {transaction['Date']} - {transaction['Compte']}: {transaction['Montant']}$")
