class Bank:
    # Class variable: List of bank names
    available_banks = ["ABL", "HBL", "UBL", "SBL"]
    
    # Default bank name
    bank_name = available_banks[0]

    @classmethod
    def change_bank_name(cls, name):
        if name in cls.available_banks:
            cls.bank_name = name
            print(f"Bank name changed to: {cls.bank_name}")
        else:
            print(f"{name} is not a valid bank. Available options: {', '.join(cls.available_banks)}")

    @classmethod
    def show_available_banks(cls):
        print("Available Banks:")
        for bank in cls.available_banks:
            print(f"- {bank}")

# Example usage:
bank1 = Bank()
bank2 = Bank()

# Show default bank name
print(f"Bank 1: {bank1.bank_name}")
print(f"Bank 2: {bank2.bank_name}")

# Show list of available banks
Bank.show_available_banks()

# Change bank name
Bank.change_bank_name("HBL")

# Show updated bank name for both instances
print(f"Bank 1 after change: {bank1.bank_name}")
print(f"Bank 2 after change: {bank2.bank_name}")
