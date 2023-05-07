#include <iostream>
#include <regex>
#include <string>
using namespace std;

int main() {
    // liczba binarna, którą chcemy sprawdzić

    string IpAdress;
    cin >> IpAdress;

    // wyrażenie regularne
    regex powerOfTwoRegex("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)){3}");
    //Pierwszy cykl sprawdza pierwszą grupę adresu ip. Przedział jest od 0-255. Kolejno: Jeżeli jest od 250-255 bądź jeżeli jest od 200 do 249 bądź jeżeli jest od 0(w tym 000) do 199 to wyrażenie jest poprawne. Następnie kod jest skopiowany i powtórzony 3 razy, czyli tyle ile zostało oktetów

    // sprawdzenie dopasowania
    if (regex_match(IpAdress, powerOfTwoRegex)) {
        cout << IpAdress << " Adres IP jest poprawny " << "" << endl;
    }
    else {
        cout << IpAdress << " IpAdress jest niepoprawny." << endl;
    }

    return 0;
}