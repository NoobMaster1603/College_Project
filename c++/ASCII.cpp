#include <iostream>
using namespace std;

int main() {
  for (int human_code = 32;human_code <= 126;human_code++)
  {
    char computer_code = human_code;
    cout<<human_code<<" = "<< computer_code<<endl;
  }
  return 0;
}