def main():
    total_sum = 0  # Global sum for all products
    print("Enter product details. To finish, type '0'.")

    while True:
        product_name = input("Product name (or '0' to finish): ")
        if product_name == '0':
            break

        try:
            price = float(input("Product price: "))
            quantity = float(input("Product quantity: "))
        except ValueError:
            print("Input error! Please enter numeric values for price and quantity.")
            continue

        # Calculate the total cost for the current product
        product_total = price * quantity
        total_sum += product_total

        print(f"Total for '{product_name}': {product_total:.2f}")

    print(f"Final total for all products: {total_sum:.2f}")


if __name__ == "__main__":
    main()
