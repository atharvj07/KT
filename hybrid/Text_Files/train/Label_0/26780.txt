#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < j; ++i)
#define FOR(i, j, k) for(int i = j; i < k; ++i)
#define P pair<int, int>

map<string, char> m;

void set_m(){
  m["11"] = 'a';
  m["12"] = 'b';
  m["13"] = 'c';
  m["14"] = 'd';
  m["15"] = 'e';
  m["21"] = 'f';
  m["22"] = 'g';
  m["23"] = 'h';
  m["24"] = 'i';
  m["25"] = 'j';
  m["31"] = 'k';
  m["32"] = 'l';
  m["33"] = 'm';
  m["34"] = 'n';
  m["35"] = 'o';
  m["41"] = 'p';
  m["42"] = 'q';
  m["43"] = 'r';
  m["44"] = 's';
  m["45"] = 't';
  m["51"] = 'u';
  m["52"] = 'v';
  m["53"] = 'w';
  m["54"] = 'x';
  m["55"] = 'y';
  m["61"] = 'z';
  m["62"] = '.';
  m["63"] = '?';
  m["64"] = '!';
  m["65"] = ' ';
}

bool has_key(string s){
  return ((m.find(s) == m.end()) ? false : true);
}

int main() {
  set_m();
  string str;
  while(cin >>str){
    string ans = "";
    if(str.length() % 2 != 0) ans = "NA";
    for(int i = 0; ans != "NA" && i < str.size(); i += 2){
      string now = str.substr(i, 2);
      if(!has_key(now)) ans = "NA";
      else ans += m[now];
    }
    cout <<ans <<endl;
  }
  return 0;
}