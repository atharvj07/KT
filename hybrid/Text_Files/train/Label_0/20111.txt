#include <bits/stdc++.h>
using namespace std;
 
#define REP(i, n) for (ll i = 0; i < n; i++)
#define REPR(i, n) for (ll i = n; i >= 0; i--)
#define FOR(i, m, n) for (ll i = m; i < n; i++)
#define FORR(i, m, n) for (ll i = m; i >= n; i--)
#define REPO(i, n) for (ll i = 1; i <= n; i++)
#define ll long long
#define INF (ll)1 << 60
#define MINF (-1 * INF)
#define ALL(n) n.begin(), n.end()
#define MOD 1000000007
#define P pair<ll, ll>

ll n, q;
vector<ll> l, v[400][26], cnt(400);
string s;
int main() {
    cin >> n >> q >> s;
    for(int i = 1; i <= sqrt(n); i++){
        if(n % i == 0){
            l.push_back(i);
            if(i != n / i)l.push_back(n / i);
        }
    }
    sort(ALL(l), greater<ll>());
    REP(i, l.size()){
        REP(j, l[i]){
            REP(k, 26){
                v[i][k].push_back(0);
            }
        }
    }
    REP(i, n){
        REP(j, l.size()){
            v[j][s[i] - 'a'][i % l[j]]++;
            if(v[j][s[i] - 'a'][i % l[j]] == n / l[j])cnt[j]++;
        }
    }
    //REP(i, l.size())cout << cnt[i]<<endl;
    REP(i, q){
        ll a;
        char c;
        cin >> a >> c;
        a--;
        REP(j, l.size()){
            if(v[j][s[a] - 'a'][a % l[j]] == n / l[j])cnt[j]--;
            v[j][s[a] - 'a'][a % l[j]]--;
        }
        REP(j, l.size()){
            v[j][c - 'a'][a % l[j]]++;
            if(v[j][c - 'a'][a % l[j]] == n / l[j])cnt[j]++;
        }
        ll ans = 0;
        REP(j, l.size()){
            if(cnt[j] == l[j])ans = l[j];
        }
        cout << ans << endl;
        s[a] = c;
    }
}

