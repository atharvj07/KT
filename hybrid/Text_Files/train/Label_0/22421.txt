#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 1000000007;

signed main() {
int n;
cin>>n;
int a[n],b[n];
for(int i=0;i<n;i++)cin>>a[i];
for(int i=0;i<n;i++)cin>>b[i];
queue<int> que;
for(int i=0;i<n;i++){
    if(b[i]>a[i]&&(b[i]-a[i])>=b[(n+i-1)%n]+b[(i+1)%n])que.push(i);
}
int ans=0,i;
while(!que.empty()){
    i=que.front();
    que.pop();
    ans+=(b[i]-a[i])/(b[(n+i-1)%n]+b[(i+1)%n]);
    b[i]=a[i]+(b[i]-a[i])%(b[(n+i-1)%n]+b[(i+1)%n]);
    i=(n+i-1)%n;
    if(b[i]>a[i]&&(b[i]-a[i])>=b[(n+i-1)%n]+b[(i+1)%n])que.push(i);
    i=(i+2)%n;
    if(b[i]>a[i]&&(b[i]-a[i])>=b[(n+i-1)%n]+b[(i+1)%n])que.push(i);
}
for(int i=0;i<n;i++){
    if(a[i]!=b[i]){
        cout<<-1;
        return 0;
    }
}
cout<<ans;





return 0;
}
