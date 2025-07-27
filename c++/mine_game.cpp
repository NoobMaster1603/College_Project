#include<iostream>
int main()
{
    bool minefields[5][5]={
        {0,1,0,0,0},
        {1,0,1,0,0},
        {0,1,0,0,1},
        {0,0,1,0,0},
        {1,0,0,1,0}
    };
    int hits=0;
    int nofturns=0;
    int xaxis;
    int yaxis;
    while (hits<8)
    {
        std::cout<<"************************************************************\n";
        std::cout<<"Select the point where you want dig (in a 5x5 area): \n\n";
        std::cout<<"Enter the X coordinate to dig: \n";
        std::cin>> xaxis;
        std::cout<<"Enter the Y coordinate to dig: \n";
        std::cin>> yaxis;
        if (minefields[xaxis][yaxis])
        {
            minefields[xaxis][yaxis]=0;
            hits++;
            std::cout <<"Mine denoted sucessfully!!\n";
            std::cout<<8-hits<<" Mines are remaining.\n\n"; 
        }
        else
        {
            std::cout<<"Miss!!\n";
        }
        nofturns++;
    }
    std::cout<<"Victory\n";
    std::cout<<"You won in "<<nofturns<<"turns\n\n";
    return 0;
}