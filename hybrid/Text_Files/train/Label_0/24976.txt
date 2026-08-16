#include <bits/stdc++.h>
using namespace std;
int main(){
  int c;
string s;
  cin>>s;
  if(s=="RSR"||s=="RSS"||s=="SSR"||s=="SRS")c=1;
  else if(s=="RRR"){c=3;}
  else if(s=="SSS"){c=0;}
  else c=2;
  cout<<c;

return 0;
}