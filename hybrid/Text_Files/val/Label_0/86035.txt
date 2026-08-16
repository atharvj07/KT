#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define db double
#define pi 2*acos(0.0)
#define mod 1000000007
#define loop(i, s, n) for(ll i=s; i<=n; i++)

typedef pair<ll, ll> pll;

ll power(ll a, ll p) {
    ll res = 1;
    while (p) {
        if (p % 2 == 0) {
            a = (a * a) % mod;
            p /= 2;
        } else {
            res = (res * a) % mod;
            p--;
        }
    }
    return res;
}

unordered_map<ll,ll> Fib;//Here 0th fib is 1, 1st fib is 2, 2nd fib is 2

ll fib(ll n)
{
    // if(n==0) return 0;
    if(n<2) return 1;
    if(Fib.find(n) != Fib.end()) return Fib[n];
    Fib[n] = (fib((n+1) / 2)*fib(n/2) + fib((n-1) / 2)*fib((n-2) / 2)) % mod;
    return Fib[n];
}


void solve(ll test){
    ll n, m; cin>> n >> m;

    string s, t; cin >> s >> t;

    vector<ll> samne;

    ll j =0;

    for(ll i=0; i<m; i++){
        char c = t[i];

        for(; j<n; j++){
            if(s[j] == c){
                samne.push_back(j);
                j++;
                break;
            }
        }
    }

    j=n-1;
    ll ans=-1;

    for(ll i=m-1; i>0; i--){

        char c = t[i];

        for(; j>-1; j--){
            if(s[j] == c){
                ans = max(ans, j-samne[i-1]);
                j--; break;
            }
        }
    }

    cout << ans << endl;
}

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    ll test=1;
    // cin >> test;

    loop(i, 1, test){
        solve(i);
    }

    return 0;
}
