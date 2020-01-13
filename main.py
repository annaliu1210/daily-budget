def daily_budget():
    budget = {'Shopping': [], 'Food': [], 'Other': []}
    for key in budget.keys():
        print(key + " Budget:")
        done = False
        while done is False:
            buy = input("Did you buy anything? (yes/no): ")
            if buy == "no":
                break
            elif buy == "yes":
                repeat = False
                while repeat is False:
                    description = input("What did you buy?: ")
                    price = input("How much did it cost?: ")
                    item = {'item': description, 'price': price}
                    budget[key].append(item)
                    print(description.title() + " was added to your " + key.lower() + " budget.")
                    more = False
                    while more is False:
                        add_more = input("Did you buy anything else? (yes/no): ").lower()
                        if add_more == "yes":
                            done, more, repeat = False, True, False
                        elif add_more == "no":
                            done, more, repeat = True, True, True
                            print(key + " budget completed.")
                        else:
                            print("Please enter yes or no.")
            else:
                print("Please enter yes or no.")
    print(budget)


daily_budget()
