#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007
typedef long long ll;
typedef unsigned long long ull;
const long long INF=1e18;



signed main(){
  ll n;
  cin>>n;
  vector<ll> a(n);
  for(int i=0;i<n;i++){cin>>a[i];}
  sort(a.begin(),a.end());
  map<ll,ll> M;
  for(int i=0;i<n;i++){M[a[i]]=i;}
  vector<vector<ll>> dp(n,vector<ll>(n,1));
  ll mx=2;
  for(int i=0;i<n;i++){
    for(int t=0;t<i;t++){
      dp[i][t]=2;
      ll A=a[i]-a[t];
      if(M.count(a[t]-A)){
	dp[i][t]=1+dp[t][M[a[t]-A]];
	mx=max(mx,dp[i][t]);
      }
    }
  }
  cout<<mx<<endl;
  
  return 0;
}
