#include <iostream>
#include <random>
#include <chrono>

std::mt19937 mt(std::chrono::high_resolution_clock::now().time_since_epoch().count());
std::uniform_int_distribution <int> machine=std::uniform_int_distribution<int>(0,190);


class rectangle
{
    private:
      int a,b;
    public:
      static int k;
      rectangle()
      {
          rectangle::k++;
          int a_random_number=machine(mt);
          this->a=a_random_number*rectangle::k;
          this->b=a_random_number+rectangle::k;
          std::cout<<"Random number created:"<<this->a<<std::endl;
          std::cout<<"Random Number created:"<<this->b<<std::endl;
      }
      rectangle(int m,int n):a(m),b(n) {
          rectangle::k++;
          std::cout<<"object::"<<this<<":created"<<std::endl;
      }
      ~rectangle() {}
      int A()const{
          int v=machine(mt);
          std::cout<<v<<std::endl;
          return this->a;
      }

      int B()const{
          int another=machine(mt);
          std::cout<<another<<std::endl;
          return this->b;
      }

      rectangle operator+(rectangle &r)
      {
          return rectangle(this->a+r.a,this->b+r.b);
      }
      int Area()const{
          return this->a*this->b;
      }       
};

int rectangle::k=0;

int main()
{
    std::cout<<"Lets create some random nums"<<std::endl;
    int mx=10+machine(mt);
    int x=20+machine(mt);
    int y=machine(mt);
    std::cout<<x<<"\t"<<y<<"\t"<<mx<<std::endl;
    int *pa=&x;
    rectangle rec;
    rectangle rec1(x,y);
    rectangle rec2=rec+rec1;
    std::cout<<rec.A()<<std::endl;
    std::cout<<rec.B()<<std::endl;
    std::cout<<rec1.A()<<std::endl;
    std::cout<<rec1.B()<<std::endl;
    std::cout<<rec2.Area()<<std::endl;
    delete pa;
    return 0;
}