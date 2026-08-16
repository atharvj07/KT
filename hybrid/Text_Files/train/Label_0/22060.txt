#include <bits/stdc++.h>
#define rep(i,n) for (int i=0; i<(n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main(){
    int n;
    cin>>n;
    vector<int>a(n),b(n);
    ll x=0;
    rep(i,n)cin>>a[i],x+=a[i];
    rep(i,n)cin>>b[i],x-=b[i];
    if(x<0){cout<<-1<<endl; return 0;}
    ll sum=0;
    int ans=0;
    priority_queue<int>q;
    rep(i,n){
        if(a[i]<b[i])sum+=a[i]-b[i],ans++;
        else q.emplace(a[i]-b[i]);
    }
    while(1){
        if(sum>=0)break;
        sum+=q.top();
        q.pop();
        ans++;
    }
    cout<<ans<<endl;
    return 0;
}