#include <iostream>
#include <fstream>

int main() {
    std::string line;
    std::ifstream file;
    int num = 0;

    file.open("../recepcja.js");

    while (std::getline(file, line)) {
        num++;
        std::cout.width(6);
        std::cout << std::left << num << line << std::endl;
    }

    file.close();

    return 0;
}
