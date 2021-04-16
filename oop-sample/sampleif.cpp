#include <iostream>
#include <algorithm>
#include <vector>

#define max(a,b) a>b?a:b

//int a,b,m-->a format in use

int main(int argc,char **argv)
{
  if(10==12) {std::cout<<"This is an if statement"<<std::endl;}
  int a=1;
  int another=101;
  int v=9;
  int x=12;
  int y=91;
  std::cout<<"Y:"<<y<<std::endl;
  std::cout<<"X:"<<x<<std::endl;
  int *pa=&a;
  std::string k="hello world";
  std::cout<<*pa<<std::endl;
  std::cout<<"String variable:"<<k<<std::endl;
  std::cout<<v<<std::endl;
  std::string k="hello world";
  int mx=max(x,y);
  std::cout<<mx<<std::endl;
  if (x==5) {}
  else if(x==4) {}
  else if(x==7 && x>1) {}
  std::vector <int> vtc{1,2,34,5,6,7,8};
  std::cout<<std::count_if(vtc.begin(),vtc.end(),[](int &l) {return l==5;});
  

  bool k=true;
  int p=1;
  if(1)
  {

  }

  return 0; 
  
}