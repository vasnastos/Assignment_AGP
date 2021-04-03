#include <iostream>

#define max(a,b) a>b?a:b

//int a,b,m-->a format in use

int main(int argc,char **argv)
{
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
  return 0;
}