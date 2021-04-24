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
<<<<<<< HEAD
=======
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
>>>>>>> 21bad35889b84ac00f49d4ccdbd3257cb22fa571
    return 0;
}
