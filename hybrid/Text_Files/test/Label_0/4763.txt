#include<iostream>
#include<numeric>
#include<vector>
using namespace std;
using ll = long long;

int main(){
    ll n;
    cin>>n;
    vector<ll> a(n);
    for(ll i=0;i<n;i++) cin>>a[i];
    ll sum=accumulate(a.begin(),a.end(),0LL);

    ll ans=sum,t=0;
    for(int i=0;i<n;i++){
        t+=a[i];
        ans=min(ans,abs(t-(sum-t)));
    }
    cout<<ans<<endl;
}