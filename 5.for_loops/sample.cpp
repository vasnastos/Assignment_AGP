#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <ostream>
#include <iterator>
#include <algorithm>

int main()
{
    std::vector <int> v{1,2,3,4,5,6,7,8,9,10};
    std::ostream_iterator <int> out=std::ostream_iterator <int>(std::cout,"\t");
    std::copy(v.begin(),v.end(),out);
    std::cout<<"Counter:"<<std::count_if(v.begin(),v.end(),[](int &a) {return a>5;});
    
    std::map <std::string,double> coins{
        {"AB",1.21},
        {"BC",2.21},
        {"CD",3.31},
        {"DE",4.41}
    };
    
    for(auto &kv:coins)
    {
        std::cout<<kv.first<<"\t"<<kv.second<<std::endl;
    }

    for(auto &x:{4,5,6,7,8,9,9,12})
    {
        std::cout<<x<<std::endl;
    }

    for(int i=0;i<10;i++)
    {
        std::cout<<i<<std::endl;
    }
    
    for(std::vector <int>::iterator i=v.begin();i!=v.end();i++)
    {
        std::cout<<*i<<std::endl;
    }
    
    for(auto i=v.begin();i!=v.end();i++)
    {
        std::cout<<*i<<std::endl;
    }
    
    for(;;)
    {
       break;
    }
    
    for(std::map <std::string,double>::iterator itr=coins.begin();itr!=coins.end();itr++)
    {
        std::cout<<itr->first<<"\t"<<itr->second<<std::endl;
    }
    
    for(auto &c:{56.8,89.1,4.5,2.3,8.9,4.1})
    {
        std::cout<<c<<std::endl;
    }
    return 0;
}