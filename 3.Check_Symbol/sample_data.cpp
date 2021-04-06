#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <memory>
#include <utility>
#include <list>

struct employee
{
    std::string name;
    double salary;
    employee(std::string n,double s):name(n),salary(s) {}
    void print()
    {
        std::cout<<this->name<<"\t"<<this->salary<<std::endl;
    }
};

int main(int argc,char **argv)
{
    //auto pointers
    auto ptr=new auto(4.56);
    auto  ptr1=new auto('L');
    std::cout<<*ptr<<std::endl;
    std::cout<<*ptr1<<std::endl;
    delete ptr;
    delete ptr1;
    std::cout<<std::endl;
    //Maps 
    std::map <std::string,int> nums{{"One",1},{"two",2},{"three",3}};
    std::map <std::string,int> vars{{std::string("A"),65},{std::string("B"),66},{std::string("C"),67}};
    nums.merge(vars);
    for(auto &kv:nums)
    {
        std::cout<<kv.first<<"\t"<<kv.second<<std::endl;
    }

    //smart pointers
    std::unique_ptr <int> ptr_p;
    ptr_p.reset(new int(17));
    std::cout<<"Pointer ptr_p:"<<*ptr_p<<std::endl;
    std::unique_ptr <int> move_ptr_p(std::move(ptr_p));
    std::cout<<std::boolalpha;
    std::cout<<"Ptr_p has related object:"<<static_cast<bool>(ptr_p)<<std::endl;
    std::cout<<"New value pointer:"<<*move_ptr_p<<std::endl;
    std::list <employee*> emp;
    emp.push_back(new employee("emp1",1000));
    emp.push_back(new employee("emp2",2000));
    emp.push_back(new employee("emp3",3000));
    for(auto &e:emp)
    {
        std::unique_ptr<employee> ptr_emplace_emp=std::unique_ptr <employee>(std::move(e));
        std::cout<<"Object "<<e<<" related to content:"<<static_cast<bool>(e)<<std::endl;
        std::cout<<"content move-->"<<&ptr_emplace_emp<<std::endl;
        std::cout<<"Content"<<std::endl;
        ptr_emplace_emp->print();
        std::cout<<"************************************************************"<<std::endl;
    }
    return 0;

}