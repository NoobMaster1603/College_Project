#include <iostream>
#include <cmath> // for sqrt function

using namespace std;

// Function to check if a number is prime
bool isPrime(int n) {
    // Handling special cases
    if (n <= 1) {
        return false;
    }
    // Check from 2 to sqrt(n) for divisibility
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false; // Found a divisor, hence not prime
        }
    }
    return true; // If no divisor found, number is prime
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (isPrime(num)) {
        cout << num << " is a prime number." << endl;
    } else {
        cout << num << " is not a prime number." << endl;
    }

    return 0;
}