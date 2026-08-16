#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
  ll n,k;
  cin>>n>>k;
  vector<ll> a(n),b(n+1,0),c(n+1,0);
  for(ll i=0;i<n;i++) cin>>a[i];
  for(ll i=0;i<n;i++){
    b[i+1]=b[i]+(a[i]>0?a[i]:0);
    c[i+1]=c[i]+a[i];
  }
  ll ans=0,tmp=0;
  for(int i=0;i<=n-k;i++){
    tmp=b[n]-b[i+k]+b[i];
    ans=max(ans,tmp);
    tmp+=c[i+k]-c[i];
    ans=max(ans,tmp);
  }
  cout<<ans<<endl;
  return 0;
}
