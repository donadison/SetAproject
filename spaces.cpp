#include <iostream>
#include <fstream>

int main() {
    char current, next;
    std::ifstream file;

    file.open("../spacje.txt");

    current = file.get();

    while (file.good()) {
        std::cout << current;
        if (current == '.' || current == ','){
            next = file.get();
            if (next != ' ') {
                std::cout << ' ';
            }
            std::cout << next;
        }
        current = file.get();
    }

    file.close();

    return 0;
}
