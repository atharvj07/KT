#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int k,t;
    cin>>k>>t;
    int a[109];
    for( int i=1;i<=t;i++) cin>>a[i];
    sort(a+1,a+t+1);
    int ans=a[t]-1;
    for(int i=t-1;i>=1;i--) ans=ans-a[i];
    cout<<max(ans,0);
}
