#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main(){
  int N,K;
  cin>>N>>K;
  vector<int> A(N);
  for(int &i:A)cin>>i;
  int ans=100000000000;
  for(int i=0;i<(1<<N);i++){
    if(__builtin_popcount(i)<K)continue;
    int cnt=0,mx=0;
    for(int j=0;j<N;j++){
      if(i>>j&1){
        if(mx>=A[j])mx++,cnt+=mx-A[j];
      }
      mx=max(mx,A[j]);
    }
    ans=min(ans,cnt);
  }
  cout<<ans<<endl;
}