
#include <iostream>
#include <regex>
#include <string>
using namespace std;

int main() {
    // liczba binarna, którą chcemy sprawdzić
    string binaryNumber = "100"; //tutaj wpisujemy liczbe, bez spacji musi byc wszystko lacznie. Nie dziala na U2

    // wyrażenie regularne
    regex powerOfTwoRegex("^0*1(0+)*$"); //jeżeli na początku jest zero 0 albo więcej i jeżeli 1 jest w sąsiedztwie (00 albo więcej) to jeżeli cykl się powtarza zwróć 1

    // sprawdzenie dopasowania
    if (regex_match(binaryNumber, powerOfTwoRegex)) {
        cout << binaryNumber << " jest potega liczby 2 " <<""<< endl;
    } else {
        cout << binaryNumber << " nie jest potega liczby 2." << endl;
    }

    return 0;
}
