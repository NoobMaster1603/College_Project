#include<iostream>
using namespace std;

int main ()
{
    int i; 
    int j = 10 ;

    i = (j++,j+100,999+j);
    cout<<i;
    return 0;
}