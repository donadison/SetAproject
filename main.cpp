#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;


//znaki sa male, znaki sa duze, ale zrównamy wszystkie w jeden lud! maly lud
string toLowercase(string str) {
    for (char& c : str) {
        c = tolower(c);
    }
    return str;
}

//taka tam funkcja aby posortowalo nam po wartosciach w parze w wektorze 
bool sortByVal(const pair<string, int> &a,const pair<string, int> &b){
	return (a.second>b.second);
}

int main() {
    ifstream file("bible.txt"); //moze być wszystko, mam też Biblię 1klecia po Polsku, ale nie zczytuje poslkich znaków :( 

    // Tworzymy mapę słów i ich częstości występowania. Mapy nie da sie posortować, więc potem do tego wrocimy
    map<string, int> mapka; 


    // Wczytujemy tekst Biblii z pliku i dzielimy na słowa
    string word, text;
    while (file >> word) { 
    	
    	while (ispunct(word.back())) { //pomijanie interpunkcji
            word.pop_back();
        }
        //word = kebabremover(word);
        word = toLowercase(word); 
        mapka[word]++;
    }

    // Tworzymy wektor par bo map nie da sie zsortowac
    vector<pair<string, int>> lista;
    map<string, int> :: iterator it2; //iterator, posluzy nam jako takie "i" do wskazywania kolejnych przebiegow petli
    for (it2=mapka.begin(); it2!=mapka.end(); it2++){ 
    	lista.push_back(make_pair(it2->first,it2->second));
	}

    // Sortujemy wektor malejąco po liczbie wystąpień
    sort(lista.begin(), lista.end(), sortByVal);

    // Wyświetlamy 10 najczęstszych słów
    cout<< "Tak mowi Pismo Swiete:"<<endl;
    for (int i = 0; i < 10 && i < lista.size(); i++) {
        cout << lista[i].first << " - " << lista[i].second << " razy" << endl;
    }
    
	cout<< "I niepojete slowa w Nim tkwia..."<<endl;

    
    //cout << licznik;

    return 0;
}
