#include <iostream>
#include <tuple>
#include <string>
#include <vector>
struct employee
{
   std::string name;
   double sal;
   employee(std::string i="",double sal=0.0)
   {
       this->name=i;
       this->sal;
       std::cout<<"Object created:"<<this<<std::endl;
   }
   friend std::ostream &operator<<(std::ostream &os,const employee &e)
   {
       return os<<e.name<<"--"<<e.sal<<std::endl;
   }
};

size_t hashing(std::string ptr_pos)
{
   size_t j=0;
   uintptr_t pointercast=reinterpret_cast<uintptr_t>(&ptr_pos);
   for(int i=0;i<ptr_pos.length();i++)
   {
        j+=pointercast*ptr_pos.at(i);
   }
   return j;
}

struct ast
{
   ast(double a,int b,std::string c)
   {
       std::cout<<a<<"---"<<b<<"---"<<c<<std::endl;
   }
};

int main(int argc,char **argv)
{
    if(argc!=2)
    {
        std::cerr<<"You did not provide the right amount of arguments"<<std::endl;
        return -1;
    }
    for(int i=0;i<std::stoi(argv[1]);i++)
    {
        auto tuple=std::make_tuple(1.3*i,1+i,std::to_string(i+1)+"insertion");
        std::make_from_tuple<ast>(std::move(tuple));
    }
    std::hash <std::string> h=std::hash <std::string>();
    employee emps[5];
    employee *e1=new employee("nikos pappas#"+std::to_string(hashing("Employee one")),1600);
    employee *e2=new employee("nikos pappas#"+std::to_string(hashing("Employee two")),1900);
    employee *e3=new employee("nikos pappas#"+std::to_string(hashing("Employee three")),2100);
    employee *e4=new employee("nikos pappas#"+std::to_string(hashing("Employee four")),2600);
    employee *e5=new employee("nikos pappas#"+std::to_string(hashing("Employee five")),15600);
    emps[0]=std::move(*e1);
    emps[1]=std::move(*e2);
    emps[2]=std::move(*e3);
    emps[3]=std::move(*e4);
    emps[4]=std::move(*e5);
    for(auto &x:emps)
    {
        std::cout<<x<<std::endl;
    }
    delete e1;
    delete e2;
    delete e3;
    delete e4;
    delete e5;
    return 0;
}