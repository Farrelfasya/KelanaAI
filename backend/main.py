"""
KelanaAI - Trip Summary Generator
Sesi 1: Console app untuk mencatat & menampilkan ringkasan rencana perjalanan.
"""


def get_trip_input():
    """Meminta input interaktif dari pengguna dan mengembalikannya sebagai dict."""
    destination = input("Destination: ")
    country = input("Country: ")
    days = int(input("Days: "))
    budget = float(input("Budget: "))
    currency = input("Currency: ")
    travel_month = input("Travel Month: ")

    return {
        "destination": destination,
        "country": country,
        "days": days,
        "budget": budget,
        "currency": currency,
        "travel_month": travel_month,
    }


def print_trip_summary(destination, country, days, budget, currency, travel_month):
    """Mencetak ringkasan perjalanan dalam format yang rapi dan terstruktur."""
    print("\n========================")
    print("      KelanaAI")
    print("========================")
    print(f"Destination : {destination}")
    print(f"Country     : {country}")
    print(f"Days        : {days}")
    print(f"Budget      : {budget:.0f} {currency}")
    print(f"Currency    : {currency}")
    print(f"Travel Month: {travel_month}")
    print("========================\n")


def main():
    trip = get_trip_input()
    print_trip_summary(
        destination=trip["destination"],
        country=trip["country"],
        days=trip["days"],
        budget=trip["budget"],
        currency=trip["currency"],
        travel_month=trip["travel_month"],
    )


if __name__ == "__main__":
    main()
