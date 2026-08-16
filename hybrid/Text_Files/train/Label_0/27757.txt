#include<bits/stdc++.h>
#define ll long long
#define ull unsigned long long
ll mod=1000000007;
using namespace std;
void solve()
{
    int n,k;
cin>>n>>k;
int a[n];
for(int i=0;i<n;i++)cin>>a[i];
int ans=-1;
while(k--){
int f=0;
for(int i=0;i<n-1;i++){
    if(a[i]<a[i+1]){
        a[i]++;
        f=1;
        ans=i+1;
        break;
    }
}
if(!f){cout<<-1<<"\n";
return ;
}
 
 
 
}
cout<<ans<<"\n";
}
int main()
{
ios_base::sync_with_stdio(false);
cin.tie(0);cout.tie(0);
int t=1;cin>>t;
while(t--)
{
solve();
}
return 0;
}