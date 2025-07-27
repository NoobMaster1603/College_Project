#include<iostream>
#include<cstdlib>
#include<ctime>
int computer_num(){
    srand(time(0));
    int cnum=rand()%10+1;
    std::cout<<"Computer's choice: "<<cnum<<std::endl;

    return cnum;
}
int player_num(){
    int pnum;
    std::cout<<"\nChoose number (1 to 10): \n";
    std::cin>>pnum;
    if(pnum>0 && pnum<11){
        std::cout<<"Player's choice: "<<pnum<<std::endl;
        return pnum;
    }
    else{
        std::cout<<"Invalid number enter between 1 to 10.\n";
        return 0;
    }
}
int main(){
    std::cout<<"\n\nHand Cricket Game\n";
    std::cout<<"******************************************************************************\n";
    std::cout<<"Things to remeber:\n";
    std::cout<<"Use numbers between 1 to 10.\n";
    std::cout<<"When computer number macthes to yours number, the one batting gets out. \n";
    std::cout<<"******************************************************************************\n";
    int run1=0;
    int run2=0;
    int c_num,p_num;
    std::cout<<"Let's start the match.\n";
    std::cout<<"Now, player will bat first and computer will  ball.\n";
    do
    {
        
        p_num=player_num();
        c_num=computer_num();
        run1=run1+p_num;
        std::cout<<"Runs scored: "<<run1<<std::endl;
    } while (p_num!=c_num);
    std::cout<<"Last innings, computer will bat and you (player) will ball. \n";
    do
    {
        
        p_num=player_num();
        c_num=computer_num();
        run2=run2+p_num;
        std::cout<<"Runs scored: "<<run1<<std::endl;
        if (run1<run2){
            std::cout<<"Computer won the maatch!!! ";
        }else if(p_num==c_num){
            std::cout<<"Player won the maatch!!! ";
        }else{
            continue;
        }
    } while (run1<run2 || p_num!=c_num);
    
    return 0;
}