#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string sentence, words[100], temp;

    cout << "Enter a sentence: ";
    getline(cin, sentence);

    stringstream ss(sentence);

    int n = 0;

    while (ss >> words[n])
        n++;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (words[i].length() > words[j].length()) {
                temp = words[i];
                words[i] = words[j];
                words[j] = temp;
            }
        }
    }

    cout << "Words sorted by length:\n";

    for (int i = 0; i < n; i++)
        cout << words[i] << " ";

    return 0;
}
