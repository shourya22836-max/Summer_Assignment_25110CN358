#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);

    bool palindrome = true;

    for (int i = 0, j = str.length() - 1; i < j; i++, j--) {
        if (str[i] != str[j]) {
            palindrome = false;
            break;
        }
    }

    if (palindrome)
        cout << "Palindrome";
    else
        cout << "Not Palindrome";

    return 0;
}