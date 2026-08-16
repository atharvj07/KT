#include <bits/stdc++.h>
typedef long long ll;
#define rep(i,n) for (ll i=0;i<n;i++)
using namespace std;
 
ll n;
ll a[330000];
 
int main() {
  cin>>n;
  rep(i,3*n) cin>>a[i];
  sort(a,a+3*n);
  reverse(a,a+3*n);
  ll ans=0;
  rep(i,n) ans+=a[i*2+1];
  cout<<ans<<endl;
  return 0;
}