#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);

    bool visited[256] = {false};

    cout << "String after removing duplicates: ";

    for (char c : str) {
        if (!visited[(unsigned char)c]) {
            cout << c;
            visited[(unsigned char)c] = true;
        }
    }

    return 0;
}