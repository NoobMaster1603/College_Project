#include<iostream>
#include<unordered_map>

using namespace std;

char first_non_repating_character(string str) {
    unordered_map<char, int> char_count;

    for (char c : str) {
        char_count[c]++;
    }

    for (int i = 0; i < str.length(); i++) {
        if (char_count[str[i]] == 1) {
            return str[i]; // Return the first non-repeating character
        }
    }

    return '\0'; // If no non-repeating character found
}
int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;

    char result = first_non_repating_character(str);
    if (result != '\0') {
        cout << "The first non-repeating character is: " << result << endl;
    } else {
        cout << "No non-repeating character found." << endl;
    }

    return 0;
}
