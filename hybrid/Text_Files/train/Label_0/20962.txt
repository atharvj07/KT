#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using VI = vector<int>;
using VL = vector<ll>;
#define FOR(i,a,n) for(int (i)=(a);(i)<(n);(i)++)
#define eFOR(i,a,n) for(int (i)=(a);(i)<=(n);(i)++)
#define rFOR(i,a,n) for(int (i)=(n)-1;(i)>=(a);(i)--)
#define erFOR(i,a,n) for(int (i)=(n);(i)>=(a);(i)--)
#define SORT(i) sort((i).begin(),(i).end())
#define rSORT(i,a) sort((i).begin(),(i).end(),(a))
#define all(i) (i).begin(),(i).end()
constexpr ll INF = 1000000000;
constexpr ll LLINF = 1LL << 60;
constexpr ll mod = 1000000007;
constexpr ll MOD = 998244353;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; }return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; }return 0; }
inline void init() { cin.tie(nullptr); cout.tie(nullptr); ios::sync_with_stdio(false); cout << fixed << setprecision(15); }
template<class T> inline istream& operator>>(istream& input, vector<T>& v) { for (auto& elemnt : v)input >> elemnt; return input; }

int main() {
    init();

    int n;
    cin >> n;
    VI t(n);
    cin >> t;
    SORT(t);
    VI r;
    for (int i = 1; i * i <= t.back(); i++) {
        if (!(t.back() % i)) {
            r.push_back(i);
            if (i * i != t.back()) {
                r.push_back(t.back() / i);
            }
        }
    }
    SORT(r);
    for (int i = 2; i * t.back() <= 10000; i++)r.push_back(i * t.back());

    int ans = 0;
    FOR(i, 0, n) {
        ans += *lower_bound(all(r), t[i]) - t[i];
    }
    cout << ans << "\n";
}
