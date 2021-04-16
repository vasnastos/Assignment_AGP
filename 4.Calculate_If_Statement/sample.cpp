#include <iostream>
#include <vector>
#include <algorithm>


int main()
{
    int x=19;
    if ( x== 14 )
    {
        std::cout<<"equality"<<std::endl;
    }
    else if ( x == 19 )
    {
        std::cout<<"19 equality"<<std::endl;
    }
    
    int n=20;

    if ( n== 19 && x>12 )
    {
        std::cout<<"Another equality"<<std::endl;
    }
    bool justaboolean=true;
    n=1000;
    std::vector <int> vct{1,2,3,4,5,6,7};
    std::replace_if(vct.begin(),vct.end(),12,[](int &k) {return k<3;});
if(10) {    if(20) { if ( n ) { if ( justaboolean )
{} } } }
    std::cout<<std::count_if(std::vector <int>({1,2,3,4,5,6,7}).begin(),std::vector <int>({1,2,3,4,5,6,7}).end(),[](int &z) {return z>10});
    return 0;
}