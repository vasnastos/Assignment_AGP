import re
check = "if(nastos==\"here\") { for(int i=0;i<10;i++) for( auto kv : checks ) {hello=23;} for( std::vector <int>::iterator itr=v.begin();itr!=v.end();itr++)}"
r1 = re.findall("for\s*\(.*\s*;.*\s*;.*\s*\)|for\s*\(.+\s*:.+\s*\)",check)
print(r1)
#or
#pattern=re.compile('for\s*\(.*\s*;.*\s*;.*\s*\)|for\s*\(.+\s*:.+\s*\)')
#print(re.findall(check))