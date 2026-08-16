#include <bits/stdc++.h>

#define ll long long
#define ii pair<int, int>
#define pll pair<ll, ll>
#define dd pair<double, double>
#define vi vector<int>
#define vl vector<ll>
#define vd vector<double>
#define vii vector<ii>
#define vll vector<pll>
#define vdd vector<dd>
#define vvi vector<vi>
#define vvl vector<vl>
#define vvd vector<vd>
#define vvii vector<vii>
#define vvll vector<vll>
#define vvdd vector<vdd>
#define fi first
#define se second
#define uni(v) v.erase(unique(v.begin(), v.end()), v.end())
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) (ll) a / __gcd(a, b) * b

using namespace std;

void print();
template <typename T, typename... Args>
void print(T x, Args... args);

void solve(int T) {
    string s;
    cin >> s;

    set<int> b1, b2, b3, b4;
    for (int i = 0; i < int(s.size()); ++i) {
        if (s[i] == '(') b1.insert(i);
        if (s[i] == ')') b2.insert(i);
        if (s[i] == '[') b3.insert(i);
        if (s[i] == ']') b4.insert(i);
    }

    int res = 0;
    for (auto& x : b1) {
        if (b2.upper_bound(x) != b2.end()) {
            res++;
            b2.erase(b2.upper_bound(x));
        }
    }
    for (auto& x : b3) {
        if (b4.upper_bound(x) != b4.end()) {
            res++;
            b4.erase(b4.upper_bound(x));
        }
    }

    cout << res << '\n';
}
int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int t = 1;
    cin >> t;
    for (int i = 0; i++ < t;) solve(i);

    return 0;
}

void print() { cout << "\n"; }
template <typename T, typename... Args>
void print(T x, Args... args) {
    if (sizeof...(args)) {
        cout << x << ' ';
        print(args...);
    } else {
        cout << x << endl;
    }
}