#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#define MOD 1000000007
typedef long long ll;
using namespace std;

map<pair<int,int>,int> mp;

int main(){
  ll h,w;
  int n;
  cin>>h>>w>>n;
  ll ans[10]={};
  ll sum=0;

  for(int i=0;i<n;i++){
    int a,b;
    cin>>a>>b;
    for(int j=0;j<=2;j++){
      if(a-j<=0||a-j+2>h) continue;
      for(int k=0;k<=2;k++){
        if(b-k<=0||b-k+2>w) continue;
        mp[make_pair(a-j,b-k)]++;
      }
    }
  }

  for(auto z:mp){
    ans[z.second]++;
    sum++;
  }
  ans[0]=(w-2)*(h-2)-sum;
  for(int i=0;i<=9;i++) cout<<ans[i]<<endl;
  return 0;
}
