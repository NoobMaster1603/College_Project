#include <iostream>
class calculator{
    public:
    int factor_of_number (int p)
    {
        
        if (p<=1)
        {
            std::cout<<"Input is either 1 or 0.\n";
            return 0;
        }
        int b=0;
        int a[b];
        int i=2;
        while (i<=p)
        {
            if (p%i==0)
            {
                a[b]=i;
                return 0;
            }
            a[b]=i;
            i++;
        }
        std::cout<<"Factors of number are: \n";
        for (int i = 0; i <= b; i++)
        {
            std::cout<<a[i];
        }
        
        return 0 ;
    }
    bool Prime_Number (int p)
    {
        if (p<=1)
        {
            return false;
        }
        for (int i = 2; i <=p; i++)
        {
            if (p%i==0)
            {
                return false;
            }
        }
        return true ;
    }
    // Function to calculate GCD using Euclidean algorithm
    int gcd_lcm(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        // Calculate LCM using the relationship with GCD
        return (a / gcd_lcm(a, b)) * b;
    }
};
int main ()
{
    class calculator c1;
    int choice;
    do
    {
        std::cout<<"Select the option from below:";//<<std::endl;
        std::cout<<std::endl<<"1. LCM"<<std::endl;
        std::cout<<"2. Prime number"<<std::endl;
        std::cout<<"3. Factor of the number"<<std::endl;
        std::cout<<"4. EXITT"<<std::endl;
        std::cin>>choice;
        switch (choice)
        {
            case 1:{
                int x1,x2;
                std::cout<<"Enter two number to get there LCM:";
                std::cin>>x1,x2;
                c1.gcd_lcm(x1,x2);
                break;
            }
            case 2:{
                int x;
                std::cout<<"Enter a numnber to check whether it is a PRIME NUMBER OR NOT= ";
                std::cin>>x;
                int y=c1.Prime_Number(x);
                if (c1.Prime_Number(x)){
                    std::cout<<"It is a prime number."<<std::endl;
                }
                else
                {
                    std::cout<<"It's not a prime number."<<std::endl;
                }
                break;
            }
            case 3:{
                int p ;
                std::cout<<"Enter a number to find it's factors: ";
                std::cin>>p;
                c1.factor_of_number(p);
                break;
            }
            default:{
                std::cout<<"error";
                break;
            }
        }
    } while (choice!=4);
}