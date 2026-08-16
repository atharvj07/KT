#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

#define EACH(i,a) for(auto&i:a)
#define FOR(i,a,b) for(ll i = (a); i < (b); ++i)
#define RFOR(i,a,b) for(ll i = (b)-1; i >= (a); --i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,0,n)
#define pb push_back
#define ALL(a) (a).begin(),(a).end()

const ll linf = 1e18;
const int inf = 1e9;
const double eps = 1e-12;
const double pi = acos(-1);

template<typename T>
istream& operator>>(istream& is, vector<T>& vec) {
    EACH(x, vec) is >> x;
    return is;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll A, B, N; cin >> A >> B >> N;
    ll ans = linf;
    FOR(C, 1, N+1) FOR(D, 1, N+1) {
        if (C * B % D == 0) {
            ans = min(ans, abs(A - C*B/D));
        }
    }
    cout << ans << endl;
}