#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
int main(){
  int n,m,A[200001],B[200001],C[200001],count=0;
  long long ans=0;
  cin>>n>>m;
  priority_queue<int> Q;
  vector<pair<int,int>> D(m);
  rep(i,n) cin>>A[i],Q.push(A[i]);
  rep(i,m) cin>>B[i]>>C[i],D[i]=make_pair(C[i],B[i]);
  sort(D.begin(),D.end());
  reverse(D.begin(),D.end());
  rep(i,m){
    rep(j,D[i].second) Q.push(D[i].first),count++;
    if(count>100000) break;
  }
  rep(i,n) ans+=Q.top(),Q.pop();
  cout<<ans;
}