#include<iostream>
using namespace std;

void duplicate(int& a, int& b, int& c)
{
    a *=2;
    b *=2;
    c *=2;
}
int main()
{
    int x=2,y=3,z=4;
    duplicate(x,y,z);
    cout<<x<<y<<z;
    return 0;
}