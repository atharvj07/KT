#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  int n,k;
  cin>>n>>k;
  int a[n];
  int ans1=0,ans2=0;
  for(int i=0;i<n;i++){
    cin>>a[i];
    if(a[i]>0)ans1+=a[i];
  }
  int p=0,m=0;
  for(int i=0;i<k;i++){
    if(a[i]>0)p+=a[i];
    else m-=a[i];
  }
  ans2=min(p,m);
  for(int i=k;i<n;i++){
    if(a[i-k]>0)p-=a[i-k];
    else m+=a[i-k];
    if(a[i]>0)p+=a[i];
    else m-=a[i];
    ans2=min(ans2,min(p,m));
  }
  cout<<ans1-ans2;

  
  return 0;
}
