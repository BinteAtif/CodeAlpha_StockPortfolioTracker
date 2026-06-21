# Advanced Stock Portfolio Tracker - Expanded Stock List
import json
from datetime import datetime

def main():
    print("=== Stock Portfolio Tracker ===\n")
    
    # Expanded hardcoded stock database (50+ popular stocks)
    stock_prices = {
        "AAPL": 280.0, "TSLA": 420.0, "GOOGL": 330.0, "MSFT": 460.0,
        "AMZN": 235.0, "NVDA": 190.0, "META": 620.0, "AMD": 220.0,
        "NFLX": 950.0, "AVGO": 350.0, "COST": 980.0, "JPM": 320.0,
        "V": 340.0, "MA": 550.0, "UNH": 550.0, "XOM": 120.0,
        "PG": 165.0, "JNJ": 205.0, "HD": 380.0, "DIS": 120.0,
        "LLY": 1050.0, "BRK-B": 500.0, "WMT": 115.0, "ORCL": 190.0,
        "ABBV": 225.0, "TSM": 310.0, "CAT": 620.0, "CRM": 290.0,
        "ADBE": 520.0, "INTC": 45.0, "CSCO": 75.0, "BAC": 55.0,
        "GE": 320.0, "PLTR": 170.0, "MU": 400.0, "NOW": 900.0,
        "PANW": 190.0, "UBER": 85.0, "KO": 70.0, "PEP": 170.0,
        "TMUS": 220.0, "LIN": 430.0, "MRK": 110.0, "CVX": 160.0,
        "NEE": 80.0, "PM": 130.0, "IBM": 300.0, "RTX": 140.0,
        "SPGI": 520.0, "BKNG": 5200.0, "AMAT": 300.0, "LRCX": 380.0,
    }
    
    portfolio = {}
    total_value = 0.0
    
    print("Enter your stocks (type 'done' when finished):")
    
    while True:
        stock = input("\nStock symbol (e.g., AAPL): ").strip().upper()
        if stock.lower() == 'done':
            break
            
        if stock in stock_prices:
            price = stock_prices[stock]
            print(f"Current price for {stock}: ${price:.2f}")
        else:
            try:
                price = float(input(f"Enter current price for {stock}: $"))
            except ValueError:
                print("Invalid price. Skipping.")
                continue
        
        try:
            qty = float(input(f"Quantity for {stock}: "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Invalid quantity.")
            continue
        
        value = qty * price
        portfolio[stock] = {
            "quantity": qty,
            "price": price,
            "value": value
        }
        total_value += value
        print(f"✓ Added {qty} shares of {stock} → Value: ${value:,.2f}")
    
    if not portfolio:
        print("No stocks entered.")
        return
    
    # === Display Portfolio ===
    print("\n" + "="*80)
    print(f"PORTFOLIO SUMMARY - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*80)
    print(f"{'Symbol':<6} {'Quantity':>10} {'Price':>12} {'Value':>15} {'Allocation':>10}")
    print("-"*80)
    
    for stock, data in sorted(portfolio.items(), key=lambda x: x[1]['value'], reverse=True):
        allocation = (data['value'] / total_value * 100) if total_value > 0 else 0
        print(f"{stock:<6} {data['quantity']:10.2f} ${data['price']:11.2f} ${data['value']:14,.2f} {allocation:9.2f}%")
    
    print("-"*80)
    print(f"{'TOTAL PORTFOLIO VALUE':<40} ${total_value:14,.2f}")
    print("="*80)
    
    # Save options (same as before)
    save_choice = input("\nSave portfolio? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (e.g., portfolio.json or .csv): ").strip() or f"portfolio_{datetime.now().strftime('%Y%m%d')}.json"
        
        if filename.endswith('.json'):
            data_to_save = {
                "date": datetime.now().isoformat(),
                "total_value": total_value,
                "stocks": portfolio
            }
            with open(filename, 'w') as f:
                json.dump(data_to_save, f, indent=2)
            print(f"✅ Saved as JSON: {filename}")
        elif filename.endswith('.csv'):
            with open(filename, 'w') as f:
                f.write("Symbol,Quantity,Price,Value,Allocation(%)\n")
                for stock, data in portfolio.items():
                    alloc = (data['value'] / total_value * 100) if total_value > 0 else 0
                    f.write(f"{stock},{data['quantity']},{data['price']},{data['value']:.2f},{alloc:.2f}\n")
                f.write(f"TOTAL,,,${total_value:,.2f},\n")
            print(f"✅ Saved as CSV: {filename}")
        else:
            # Text file
            with open(filename, 'w') as f:
                f.write(f"Stock Portfolio - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write("="*60 + "\n\n")
                for stock, data in portfolio.items():
                    alloc = (data['value'] / total_value * 100) if total_value > 0 else 0
                    f.write(f"{stock}: {data['quantity']:.2f} shares @ ${data['price']:.2f} = ${data['value']:,.2f} ({alloc:.2f}%)\n")
                f.write(f"\nTotal: ${total_value:,.2f}\n")
            print(f"✅ Saved as text: {filename}")

if __name__ == "__main__":
    main()