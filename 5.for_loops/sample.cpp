#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

void nums(int k)
{
   for(int i=1;i<=k;i++)
   {
       std::cout<<i<<std::endl;
   }
   for(int j=0;j<10;j++) {std::cout<<"(hello from loop)"<<std::endl;}
   for(int m=0;m<20;m++)
   {
       for(int n=0;n<10;n++)
       {
           std::cout<<m<<"-->"<<n<<std::endl;
       }
   }
}

int main()
{
    std::vector <int> v{1,2,34,5,6,89,32,1};
    std::map <std::string,int> chars{{"A",10},{"B",11},{"C",12},{"D",13}};
    for(int i=0;i<v.size();i++)
    {
        std::cout<<v.at(i)<<std::endl;
    }
    for(std::vector<int>::iterator itr=v.begin();itr!=v.end();itr++)
    {
        std::cout<<*itr<<std::endl;
    }
    int jk$48i=0;
    std::cout<<jk$48i;
    for(auto &kv:chars)
    {
        std::cout<<kv.first<<"-->"<<kv.second<<std::endl;
    }
    for(auto itr=chars.begin();itr!=chars.end();itr++)
    {
        std::cout<<itr->first<<"-->"<<itr->second<<std::endl;
    }
        for(  auto & vs : v )   for(auto & n: v)
        {
            continue;
        }
    std::for_each(v.begin(),v.end(),[](int &k) {k+=1;});
    std::cout<<v[3]<<std::endl;
    nums(10);
    return 0;
}