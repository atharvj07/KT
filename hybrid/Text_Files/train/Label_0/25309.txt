#include<bits/stdc++.h>
#define ll long long
#define P pair<ll, ll>
using namespace std;

const ll inf = 1e18;

int main(){
    int n, k;
    cin >> n >> k;
    vector<ll>a(n);
    for(int i=0;i<n;i++) cin >> a[i];

    ll ans = inf;

    for(int tmp=0;tmp<(1<<15);tmp++){
        bitset<15>s(tmp);
        int cnt = 0;
        for(int i=0;i<n;i++) if(s.test(i)) cnt++;
        if(cnt < k) continue;

        ll ma = 0;
        ll sum = 0;
        for(int i=0;i<n;i++){
            if(!s.test(i)){
                ma = max(ma, a[i]);
                continue;
            }
            if(a[i] > ma){
                ma = a[i];
                continue;
            }
            sum += ma - a[i] + 1;
            ma++;
        }
        
        ans = min(ans, sum);
    }

    cout << ans << endl;
}
