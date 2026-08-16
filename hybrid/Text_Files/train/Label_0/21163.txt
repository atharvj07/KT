#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i = 0; i < (n); i++)
#define all(v) v.begin(), v.end()
#define MOD 1000000009
const long long INF = 1LL<<60;

int main() {
    int n;
    cin>>n;
    vector<int> a(n),b(n),c(n);
    rep(i,n) cin>>a[i];
    rep(i,n) cin>>b[i];
    rep(i,n) cin>>c[i];

    sort(all(a));
    sort(all(c));

    ll ans=0;
    rep(i,n){
        ll num1=lower_bound(all(a),b[i])-a.begin();
        ll num2=c.end()-upper_bound(all(c),b[i]);
        //cout<<num1<<" "<<num2<<endl;
        ans+=(num1*num2);
    }

    cout<<ans<<endl;
}
