#Code Alpha Stock Portfolio Tracker
def calculate_portfolio():
# Stock prices dictionary
    stock_prices = {
        "Apple": 180,
        "Tesla": 250,
        "Google": 140,
        "Amazon": 130,
        "Microsoft": 400
    }

    portfolio_summary = []
    grand_total = 0

    print("="*50)
    print("📈 Welcome to CodeAlpha Stock Portfolio Tracker")
    print("="*50)

    while True:

        print("\nMENU")
        print("1️⃣  View Available Stocks")
        print("2️⃣  Buy Stock")
        print("3️⃣  View Portfolio")
        print("4️⃣  Save Portfolio to File")
        print("5️⃣  Exit")

        choice = input("\nEnter your choice: ")

        # VIEW STOCKS
        if choice == "1":
            print("\nAvailable Stocks")
            print("-"*30)

            for stock, price in stock_prices.items():
                print(f"🟢 {stock} : ${price}")

        # BUY STOCK
        elif choice == "2":

            stock_name = input("Enter stock name: ").strip().title()

            if stock_name in stock_prices:

                try:
                    quantity = int(input("Enter quantity: "))

                    if quantity <= 0:
                        print("❌ Quantity must be positive.")
                        continue

                    price = stock_prices[stock_name]
                    total_investment = price * quantity

                    portfolio_summary.append({
                        "name": stock_name,
                        "qty": quantity,
                        "inv": total_investment
                    })

                    grand_total += total_investment

                    print(f"✅ {stock_name} stock added successfully!")

                except ValueError:
                    print("❌ Please enter numbers only.")

            else:
                print("❌ Stock not available.")

        # VIEW PORTFOLIO
        elif choice == "3":

            if len(portfolio_summary) == 0:
                print("📭 No stocks purchased yet.")
                continue

            print("\n📊 YOUR PORTFOLIO")
            print("-"*50)

            header = f"{'Stock':<15}{'Qty':<10}{'Investment':<15}"
            print(header)
            print("-"*50)

            for item in portfolio_summary:
                row = f"{item['name']:<15}{item['qty']:<10}${item['inv']:<15}"
                print(row)

            print("-"*50)
            print(f"💰 Total Investment: ${grand_total}")

        # SAVE TO FILE
        elif choice == "4":

            if len(portfolio_summary) == 0:
                print("Nothing to save.")
                continue

            with open("portfolio_data.txt", "w") as file:

                file.write("PORTFOLIO SUMMARY\n")
                file.write("="*50 + "\n")

                header = f"{'Stock':<15}{'Qty':<10}{'Investment':<15}"
                file.write(header + "\n")
                file.write("-"*50 + "\n")

                for item in portfolio_summary:
                    row = f"{item['name']:<15}{item['qty']:<10}${item['inv']:<15}"
                    file.write(row + "\n")

                file.write("-"*50 + "\n")
                file.write(f"Total Investment: ${grand_total}")

            print("💾 Portfolio saved in portfolio_data.txt")

        # EXIT
        elif choice == "5":
            print("👋 Thank you for using the tracker!")
            break

        else:
            print("❌ Invalid choice. Try again.")

#main function
if __name__ == "__main__":
    calculate_portfolio()