#include<bits/stdc++.h>
using namespace std;
int main(void){
  string s; cin>>s;
  map<int,int> mp; mp[0]=1;
  int n=s.size(),t=1,m=0;
  while(n--){
    m+=(int)(s[n]-'0')*t;
    if(m>2018) m%=2019;
    t*=10;
    if(t>2018) t%=2019;
    ++mp[m];
  }
  n=mp.size();
  int res=0;
  for(auto& itr:mp) res+=itr.second*(itr.second-1)/2;
  cout<<res;
  return 0;
}