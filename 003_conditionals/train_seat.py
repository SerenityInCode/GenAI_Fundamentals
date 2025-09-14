seat_type = input("Enter your preferred seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air Conditioned, comfy bed")
    case "general":
        print("General - Cheapest, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Unknown seat type!")        