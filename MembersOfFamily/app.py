from dad import Dad

def main():
    robert = Dad("Robert", "45")

    print(robert.name,robert.age)

    robert.whistle()

if __name__ == "__main__":
    main()