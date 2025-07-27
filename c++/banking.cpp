#include<iostream>
void showbalance(double balance)
{
    std::cout<<"\nYour balance is Rs."<<balance<<"/-\n";
    getchar();
}
double withdraw(double balance)
{
    double amount;
    std::cout <<"Enter the amount you want to withdraw: ";
    std::cin>>amount;
    if(amount>balance)
    {
        std::cout<<"Your account does have sufficient balance.";
        return 0;
    }
    else if(amount<0){
        std::cout<<"Please enter valid amount";
        return 0;
    }
    else{
        return amount;
    }
    
}
double deposit()
{
    double amount ;
    std::cout<<"Enter the amount you want to deposit: ";
    std::cin>>amount;
    if(amount>0){
        return amount;
    }
    else{
        std::cout<<"Please enter valid amount.\n";
        return 0;
    }
}
int main()
{
    std::cout<<"Welcome ABC Bank.\n";
    double balance=0;
    int choice;
    do
    {
        std::cout<<"-----------------------------------------------------------------------------------------------\n";
        std::cout<<"\nPlease select the operation you want to do and write the correspounding number to select it";
        std::cout<<"\n1.Check balance.";
        std::cout<<"\n2.Deposit money.";
        std::cout<<"\n3.Withdraw money.";
        std::cout<<"\n4.Exit.\n";
        std::cin>>choice;
        switch(choice)
        {
            case 1:showbalance (balance);
                break;
            case 2:balance += deposit();
                showbalance(balance);
                break;
            case 3:balance -= withdraw(balance);
                showbalance(balance);
                break;
            case 4:std::cout<<"Thank you for visiting";
                break;
            default:std::cout<<"Invalid entry";
                break;
        }

    } while (choice !=4);
    
    return 0;
}