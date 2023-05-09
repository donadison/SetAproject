#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;


string toLowercase(string str) {
    for (char& c : str) {
        c = tolower(c);
    }
    return str;
}



int main() {
    ifstream file("zara.txt");

    // Tworzymy mapę słów i ich częstości występowania
    unordered_map<string, int> licznik;

    // Wczytujemy tekst Biblii z pliku i dzielimy na słowa
    string word, text;
    while (file >> word) {
    	
    	while (ispunct(word.back())) {
            word.pop_back();
        }
        //word = kebabremover(word);
        word = toLowercase(word);
        if (word.empty() || word.length() < 3) {
            continue;
        }
        licznik[word]++;
    }

    // Tworzymy wektor par (słowo, liczba wystąpień)
    vector<pair<string, int>> lista(licznik.begin(), licznik.end());

    // Sortujemy wektor malejąco po liczbie wystąpień
    sort(lista.begin(), lista.end(),
         [](const pair<string, int>& a, const pair<string, int>& b) {
             return a.second > b.second;
         });

    // Wyświetlamy 10 najczęstszych słów
    cout<< "Tak mowi Pismo Swiete:"<<endl;
    for (int i = 0; i < 10 && i < lista.size(); i++) {
        cout << lista[i].first << " - " << lista[i].second << " razy" << endl;
    }
    
    
    //cout << licznik;

    return 0;
}
