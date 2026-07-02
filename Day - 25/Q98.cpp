#include <iostream>
#include <string>
using namespace std;

int main() {
    string str1, str2;

    cout << "Enter first string: ";
    getline(cin, str1);

    cout << "Enter second string: ";
    getline(cin, str2);

    bool printed[256] = {false};

    cout << "Common characters: ";

    for (char c : str1) {
        if (str2.find(c) != string::npos && !printed[(unsigned char)c]) {
            cout << c << " ";
            printed[(unsigned char)c] = true;
        }
    }

    return 0;
}