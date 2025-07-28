#include<iostream>
using namespace std;
int main()
{
    string s ;
    
    cout<<"enter the sentence with spaces "<<endl;
    // cin>>s;
    getline(cin, s);

    cout<<s;
    return 0;
}