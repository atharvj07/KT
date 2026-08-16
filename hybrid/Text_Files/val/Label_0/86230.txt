#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<assert.h>

using namespace std;
#define repeat(i,n) for(int i=0;i<(n);i++)

int main(){

  int n, l; cin>> n>> l;
  vector<string> s(n);
  repeat(i, n) cin>> s[i];

  map<string, int> mp;
  for(auto t: s){
    mp[t]++;
  }

  sort(s.begin(), s.end());

  string ans="";
  for(auto t: s)if(mp[t]){
    string u=t;
    reverse(u.begin(), u.end());
    if(u==t){
      if(mp[t]>=2){mp[t]-=2; ans+=t;}
    }else{
      if(mp[u]>=1){mp[t]-=1; mp[u]-=1; ans+=t;}
    }
  }

  string A=ans;
  for(auto e: mp)if(e.second){
    string t=e.first;
    reverse(t.begin(), t.end());
    if(t==e.first){
      A+=t;
      break;
    }
  }

  reverse(ans.begin(), ans.end());
  cout<< A+ans<< endl;

  return 0;
}