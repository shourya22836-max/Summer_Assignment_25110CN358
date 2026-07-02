#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);

    int freq[256] = {0};

    for (char c : str)
        freq[(unsigned char)c]++;

    int maxFreq = 0;
    char maxChar;

    for (char c : str) {
        if (freq[(unsigned char)c] > maxFreq) {
            maxFreq = freq[(unsigned char)c];
            maxChar = c;
        }
    }

    cout << "Maximum occurring character: " << maxChar << endl;
    cout << "Frequency: " << maxFreq;

    return 0;
}