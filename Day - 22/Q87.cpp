#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    char ch;

    cout << "Enter a string: ";
    getline(cin, str);

    cout << "Enter character: ";
    cin >> ch;

    int count = 0;

    for (char c : str) {
        if (c == ch)
            count++;
    }

    cout << "Frequency of '" << ch << "' = " << count;

    return 0;
}