#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); i++) 
#define all(v) begin(v),end(v)
using ll = long long;

int main() {
  int n;string s;cin>>n>>s;
  int ans=0;
  for(int i=1;i<n;i++){
    vector<int> l(26),r(26);
    rep(j,i)l[s[j]-'a']++;
    for(int j=i;j<n;j++)r[s[j]-'a']++;
    int cnt=0;
    rep(i,26){
      if(l[i]>0&&r[i]>0)cnt++;
    }
    ans=max(ans,cnt);
  }
  cout<<ans<<endl;
}