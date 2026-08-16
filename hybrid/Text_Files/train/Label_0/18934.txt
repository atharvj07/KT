#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main(){
  int n;
  char s[9];
  long l,m;
  cin>>n;
  while(n--){
    cin>>s;
    sort(s,s+sizeof(s)-1);
    l=atol(s);
    sort(s,s+sizeof(s)-1,greater<char>());
    m=atol(s);
    cout<<m-l<<endl;
  }
  return 0;
}