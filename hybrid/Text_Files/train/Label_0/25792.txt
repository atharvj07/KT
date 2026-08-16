#include<bits/stdc++.h>
using namespace std;
using Int = long long;

signed main(){
  Int n,l,r;
  while(cin>>n>>l>>r,n||l||r){
    vector<Int> a(n);
    for(Int i=0;i<n;i++) cin>>a[i];
    auto is_uruu=[&](Int x)->Int{
      for(Int i=0;i<n;i++){
	if(x%a[i]==0) return (i%2==0);
      }
      return (n%2==0);
    };
    Int ans=0;
    for(Int i=l;i<=r;i++) ans+=is_uruu(i);
    cout<<ans<<endl;
  }
  return 0;
}

