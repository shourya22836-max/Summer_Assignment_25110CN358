// Find Pair with Given Sum

#include <iostream>
using namespace std;

int main() {
    int n, sum;

    cout << "Enter size: ";
    cin >> n;

    int arr[n];

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Enter required sum: ";
    cin >> sum;

    bool found = false;

    cout << "Pairs are:\n";

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == sum) {
                cout << arr[i] << " " << arr[j] << endl;
                found = true;
            }
        }
    }

    if (!found)
        cout << "No Pair Found";

    return 0;
}