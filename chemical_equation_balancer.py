def equation_balancer():
    print("Chemical Equation Balancer\n")

    n = int(input("How many elements to check? "))
    balanced = True

    for i in range(n):
        element = input(f"\nEnter element {i+1} symbol: ")
        reactant_count = int(input(f"Count of {element} on reactant side: "))
        product_count = int(input(f"Count of {element} on product side: "))

        if reactant_count == product_count:
            print(f"{element}: Balanced ✓")
        else:
            print(f"{element}: Not balanced ✗ ({reactant_count} ≠ {product_count})")
            balanced = False

    print("\n" + "="*30)
    if balanced:
        print("✅ Equation is BALANCED!")
    else:
        print("❌ Equation is NOT balanced!")

equation_balancer()
