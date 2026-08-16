#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
  ll a,b,n,ans=(1e18);
  cin>>a>>b>>n;
  for(int i=1;i<=n;i++){
    for(int j=1;j<=n;j++)
      if(b%i==0)ans=min(ans,llabs(a-b/i*j));
  }
  cout<<ans<<endl;
  return 0;
}