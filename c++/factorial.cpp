#include<iostream>
using namespace std;
int main()
{
    int n = 10;
    long long factorial = 1;
    if (n<= 0)
    {
        cout<<"Enter a valid input \n";
    }
    else
    {
        for (long long i =1; i <= n; ++i)
        {
            factorial *= i;
        }
        cout<<"Factorial of "<<n<<" is "<<factorial<<endl;

    }
    return 0;

}