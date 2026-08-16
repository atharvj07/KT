const long long MOD = 1e9 + 7;
const long long INF = 1e9;
const long long INFLL = 1e18;

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vll;
typedef complex<double> cd;

#define forn(i, n) for (int (i) = 0; (i) != (n); (i)++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define popcount(x) __builtin_popcount(x)
#define popcountll(x) __builtin_popcountll(x)
#define fi first
#define se second
#define re return
#define pb push_back
#define uniq(x) sort(all(x)); (x).resize(unique(all(x)) - (x).begin())

#ifdef LOCAL
#define dbg(x) cerr << __LINE__ << " " << #x << " " << x << endl
#define ln cerr << __LINE__ << endl
#else
#define dbg(x) void(0)
#define ln void(0)
#endif // LOCAL

int cx[4] = {-1, 0, 1, 0};
int cy[4] = {0, -1, 0, 1};
string Yes[2] = {"No\n", "Yes\n"};
string YES[2] = {"NO\n", "YES\n"};
string Possible[2] = {"Impossible\n", "Possible\n"};
string POSSIBLE[2] = {"IMPOSSIBLE\n", "POSSIBLE\n"};

int ok(int x, int n)
{
    return 0 <= x && x < n;
}

ll log10(ll x)
{
    if (x < 10) re 1;
    re 1 + log10(x / 10);
}

ll ds(ll x)
{
    if (x < 10) return x;
    re x % 10 + ds(x / 10);
}

double sqr(double x)
{
    return x * x;
}

bool inmask(int bit, int mask)
{
    return (mask & (1 << bit)) > 0;
}

void Del(vector<int> &v, int pos)
{
    swap(v[pos], v[v.size() - 1]);
    v.pop_back();
}

long long g(vector<long long> &p, int pos)
{
    if (ok(pos, p.size())) return p[pos];
    if (pos < 0 || p.size() == 0) return 0;
    return p.back();
}

int g(vector<int> &p, int pos)
{
    if (ok(pos, p.size())) return p[pos];
    if (pos < 0 || p.size() == 0) return 0;
    return p.back();
}

ll inq(ll x, ll y)
{
    if (!y) re 1 % MOD;
    ll l = inq(x, y / 2);
    if (y % 2) re l * l % MOD * x % MOD;
    re l * l % MOD;
}

ll rev(ll x)
{
    return inq(x, MOD - 2);
}

int __precomputed_combinatorics = 0;
vector<ll> __fact, __ufact, __rev;

inline void __precompute_combinatorics(int __n)
{
    if (__precomputed_combinatorics >= __n)
        return;
    __fact.resize(__n);
    __ufact.resize(__n);
    __rev.resize(__n);
    __rev[1] = 1;
    for (int i = max(2, __precomputed_combinatorics); i < __n; i++)
        __rev[i] = MOD - __rev[MOD % i] * (MOD / i) % MOD;
    __fact[0] = 1, __ufact[0] = 1;
    for (int i = max(1, __precomputed_combinatorics); i < __n; i++)
        __fact[i] = __fact[i - 1] * i % MOD, __ufact[i] = __ufact[i - 1] * __rev[i] % MOD;
    __precomputed_combinatorics = __n;
}

ll fact(int x)
{
    if (__precomputed_combinatorics <= x)
        __precompute_combinatorics(x + 1);
    return __fact[x];
}

ll cnk(int n, int k)
{
    if (k < 0 || k > n)
        return 0;
    if (__precomputed_combinatorics <= n)
        __precompute_combinatorics(n + 1);
    return __fact[n] * __ufact[n - k] % MOD * __ufact[k] % MOD;
}

ll inq(ll x, ll y, ll mod)
{
    if (y == 0) return 1 % mod;
    ll l = inq(x, y / 2, mod);
    if (y % 2) return l * l % mod * x % mod;
    return l * l % mod;
}

void dfs(int v, int par, vector<int> &h, vector<int> &edge_in, vector<int> &a, vector<int> &b)
{
    if (v == par) h[v] = 0;
    else h[v] = h[par] + 1;
    for (int i = 0; i < h.size() - 1; i++)
    {
        if (a[i] == v || b[i] == v)
        {
            int u = a[i] + b[i] - v;
            if (u != par)
            {
                edge_in[u] = i;
                dfs(u, v, h, edge_in, a, b);
            }
        }
    }
}

int mark(int v, int u, vector<int> &h, vector<int> &edge_in, vector<int> &a, vector<int> &b)
{
    int mask = 0;
    while (h[v] > h[u])
    {
        mask += 1 << edge_in[v];
        int f = a[edge_in[v]] + b[edge_in[v]] - v;
        v = f;
    }
    while (h[v] < h[u])
    {
        mask += 1 << edge_in[u];
        int f = a[edge_in[u]] + b[edge_in[u]] - u;
        u = f;
    }
    while (v != u)
    {
        mask += 1 << edge_in[v];
        int f = a[edge_in[v]] + b[edge_in[v]] - v;
        v = f;
        mask += 1 << edge_in[u];
        f = a[edge_in[u]] + b[edge_in[u]] - u;
        u = f;
    }
    return mask;
}

ll supersigmacnt(ll i, ll k, ll n)
{
    ll ans = 0;
    for (int j = k; j <= n; j++)
    {
        ans = (ans + (n - j + i) * cnk(j, k)) % MOD;
    }
    return ans;
}

signed main()
{
    srand(time(NULL));
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;
    vector<int> a(m), b(m);
    for (int i = 0; i < m; i++)
    {
        cin >> a[i] >> b[i];
        a[i]--, b[i]--;
    }
    vector<int> h(n), edge_in(n);
    dfs(0, 0, h, edge_in, a, b);
    vector<int> suba(m);
    for (int i = n - 1; i < m; i++)
    {
        int z = mark(a[i], b[i], h, edge_in, a, b);
        suba[i] = z;
    }
    int M = 1 << (n - 1);
    {
        vector<ll> on_right(M, 0);
        for (int mask = 1; mask < M; mask++)
        {
            for (int i = n - 1; i < m; i++)
            {
                if (suba[i] & mask)
                {
                    on_right[mask]++;
                }
            }
            on_right[mask] += __builtin_popcount(mask) - 1;
        }
        vector<ll> dp(M);
        vector<ll> EV(M);
        vector<ll> ans(M);
        on_right[0] = -1;
        dp[0] = 1;
        for (int mask = 1; mask < M; mask++)
        {
            ll summ_right = 0, cnt_left = 0, cnt_right = 0;
            for (int p = 0; p < n - 1; p++)
            {
                if (mask & (1 << p))
                {
                    int pmask = mask - (1 << p);
                    if (pmask == 0)
                    {
                        dp[mask] = fact(on_right[mask]);
                        EV[mask] = 1;
                        ans[mask] = fact(on_right[mask]) * (m - on_right[mask]) % MOD;
                        continue;
                    }
                    int cnt = on_right[mask] - on_right[pmask] - 1;
                    for (int here = 0; here <= cnt; here++)
                    {
                        int there = cnt - here;
                        ll ways = fact(cnt) % MOD * cnk(on_right[mask] - here - 1, on_right[pmask]) % MOD;
                        ll dpways = ways * dp[pmask] % MOD;

                        cnt_right = (cnt_right + (on_right[pmask] + 1 + there) * dpways) % MOD;
                        //cnt_left = (cnt_left + (here + 1) * dpways) % MOD;

                        summ_right = (summ_right + (EV[pmask] + 1) * (on_right[pmask] + 1 + there) % MOD * dpways) % MOD;

                        ans[mask] = (ans[mask] + ans[pmask] * ways + (m - on_right[mask]) * dpways
                                       - there * EV[pmask] % MOD * dpways) % MOD;
                        if (ans[mask] < 0) ans[mask] += MOD;
                    }
                    ll ways = cnk(on_right[mask], on_right[pmask] + 1) * fact(on_right[mask] - on_right[pmask] - 1) % MOD;
                    ll dpways = dp[pmask] * ways % MOD;
                    dp[mask] = (dp[mask] + dpways) % MOD;
                    ll Z = supersigmacnt(1, on_right[pmask], on_right[mask] - 1);
                    cnt_left = (cnt_left + Z * fact(cnt) % MOD * dp[pmask]) % MOD;
                }
            }
            if (__builtin_popcount(mask) > 1)
            {
                //cout << mask << " " << summ_left << " " << summ_right << " " << cnt_left << " " << cnt_right << "\n";
                EV[mask] = (cnt_left + summ_right) * inq(cnt_left + cnt_right, MOD - 2) % MOD;
            }
            //cout << mask << " " << dp[mask] << " " << EV[mask] << " " << ans[mask] << "\n";
        }
        //cout << dp[M - 1] << "\n";
        cout << ans[M - 1] << "\n";
    }
}

/* Note:
Check constants at the beginning of the code (MOD, INF, INFLL)
Check corner cases.
    N = 1
No def int long long for now.
Add something here.
*/
