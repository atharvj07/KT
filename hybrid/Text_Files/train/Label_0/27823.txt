#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;


int main(void){
  int n,i,a[100005];
  
  cin >> n;
  for (i=0;i<n;i++) cin >> a[i];
  
  sort(a,a+n,greater<int>());
  
  if (n%2==0){
    
    ll ans=0;
    for (i=0;i<n/2-1;i++) ans+=a[i]*2;
    ans+=a[n/2-1]-a[n/2];
    for (i=n/2+1;i<n;i++) ans-=a[i]*2;
    
    cout << ans << endl;
    
  }else{
    
    ll ans1=0,ans2=0;
    for (i=0;i<(n-3)/2;i++) ans1+=a[i]*2;
    ans1+=a[(n-3)/2]+a[(n-1)/2];
    for (i=(n+1)/2;i<n;i++) ans1-=a[i]*2;
    
    for (i=0;i<(n-1)/2;i++) ans2+=a[i]*2;
    ans2-=a[(n-1)/2]+a[(n+1)/2];
    for (i=(n+3)/2;i<n;i++) ans2-=a[i]*2;
    
    cout << max(ans1,ans2) << endl;
    
  }
  
  return 0;
}