#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
  string s;
  getline(cin,s);
  stringstream ss;
  ss << s;
  bool ck=false;
  while(ss >> s) {
    if(s[s.size()-1]==',' || s[s.size()-1]=='.') {
      s=s.substr(0,s.size()-1);
    }
    if(s.size()>2 && s.size()<7) {
      if(ck) cout << " ";
      cout << s;
      if(!ck) ck=true;
    }
  }
  cout << endl;
  return 0;
}
