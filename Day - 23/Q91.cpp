#include <iostream>
#include <string>
using namespace std;

int main() {
    string str1, str2;

    cout << "Enter first string: ";
    getline(cin, str1);

    cout << "Enter second string: ";
    getline(cin, str2);

    if (str1.length() != str2.length()) {
        cout << "Not Anagrams";
        return 0;
    }

    int count[256] = {0};

    for (char c : str1)
        count[(unsigned char)c]++;

    for (char c : str2)
        count[(unsigned char)c]--;

    for (int i = 0; i < 256; i++) {
        if (count[i] != 0) {
            cout << "Not Anagrams";
            return 0;
        }
    }

    cout << "Anagrams";

    return 0;
}