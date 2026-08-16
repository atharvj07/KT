#include<bits/stdc++.h>
#define rep(i,n) for(int i=0; i<n; i++)
using namespace std;
int main(){
  int n,Max=0;
  int t[100000];
  cin >> n;
  rep(i,n){
    cin >> t[i];
    Max = max(t[i],Max);
  }
  vector<int> v;
  for(int i=1; i<=Max; i++){
    if(Max%i == 0) v.push_back(i);
  }
  int ans = 0;
  rep(i,n){
    rep(j,v.size()){
      if(t[i]<=v[j]){
        ans += v[j]-t[i];
        break;
      }
    }
  }
  cout << ans << endl;
  return 0;
}

