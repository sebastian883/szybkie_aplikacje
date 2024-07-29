def przelicz_walute(kwota, kurs_z, kurs_na):
    return kwota * (kurs_na / kurs_z)
def wybierz_walute(kursy):
    print(f"dostepne waluty: EUR, USD, PLN")
    waluta = input(" wybierz walute (EUR/USD/PLN): ").upper()
    while waluta not in kursy:
        print("niepoprawna waluta! spróbuj ponownie.")
        waluta = input("wybierz walute (EUR/USD/PLN): ").upper()
        return waluta
def main():
    kursy = {'EUR': 4.60, 'USD': 4.00, 'PLN': 1.00}
    print("witaj w przeliczniku walut")
    waluta_z = wybierz_walute(kursy)
    waluta_na = wybierz_walute(kursy)
    kwota = float(input(f"podaj kwote w {waluta_z}: "))
    kurs_z = kursy[waluta_z]
    kurs_na = kursy[waluta_na]
    przeliczona_kwota = przelicz_walute(kwota, kurs_z, kurs_na)
    print(f"{kwota} {waluta_z} to {przeliczona_kwota:.2f} {waluta_na}")


main()

































