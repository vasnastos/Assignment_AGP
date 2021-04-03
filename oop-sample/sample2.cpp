#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <map>

namespace fs=std::filesystem;
std::string green="Color 0A";
std::string blue="Color 01";
std::string red="Color 04";
std::string yellow="Color 06";
std::string white="Color 07";



std::vector <std::string> getFiles(std::string masterfolder)
{
    std::vector <std::string> files;
  for(auto &x:fs::recursive_directory_iterator(masterfolder))
  {
     files.push_back(x.path().string());
  }
  return files;
}

int main()
{
    std::vector <std::string> all_files=getFiles("oop-master");
    int x=0;
    int y=0;
    int another=0;
    int v=0;
    int a=0;
    for(const auto &n:all_files)
    {

        if(n.substr(n.length()-std::string(".cpp").length(),n.length())==".cpp")
        {
          x++; 
        }
        else if(n.substr(n.length()-std::string(".hpp").length(),n.length())==".hpp")
        {
            y++;
        }
        else if(n.substr(n.length()-std::string(".h").length(),n.length())==".h")
        {
          v++;
        }
        else if(n.substr(n.length()-std::string(".c").length(),n.length())==".c")
        {
          a++;
        }
        else{
          another++;
        }
    }
    std::cout<<"\t\tSummary"<<std::endl;
    system(green.c_str());
    //system(white.c_str());
    //system(blue.c_str());
    //system(red.c_str());
    //system(yellow.c_str());
    std::cout<<x<<std::endl;
    std::cout<<y<<std::endl;
    std::cout<<v<<std::endl;
    std::cout<<a<<std::endl;
    std::cout<<another<<std::endl;
}