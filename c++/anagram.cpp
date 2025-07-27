#include<iostream>

using namespace std;
bool isAnagram(string str1, string str2) {
    if (str1.length() != str2.length()) {
        return false;
    }

    int count[256] = {0}; // Assuming ASCII characters

    for (char c : str1) {
        count[c]++;
    }

    for (char c : str2) {
        count[c]--;
        if (count[c] < 0) {
            return false;
        }
    }

    return true;
}
int main() {
    string str1, str2;
    cout << "Enter first string: ";
    cin >> str1;
    cout << "Enter second string: ";
    cin >> str2;

    if (isAnagram(str1, str2)) {
        cout << "The strings are anagrams." << endl;
    } else {
        cout << "The strings are not anagrams." << endl;
    }

    return 0;
}