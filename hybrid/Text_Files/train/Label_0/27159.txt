#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define DEBUG(...) debug(#__VA_ARGS__, __VA_ARGS__);
#else
#define DEBUG(...) 6;
#endif

template<typename T, typename S> ostream& operator << (ostream &os, const pair<T, S> &p) {return os << "(" << p.first << ", " << p.second << ")";}
template<typename C, typename T = decay<decltype(*begin(declval<C>()))>, typename enable_if<!is_same<C, string>::value>::type* = nullptr>
ostream& operator << (ostream &os, const C &c) {bool f = true; os << "["; for (const auto &x : c) {if (!f) os << ", "; f = false; os << x;} return os << "]";}
template<typename T> void debug(string s, T x) {cerr << s << " = " << x << "\n";}
template<typename T, typename... Args> void debug(string s, T x, Args... args) {cerr << s.substr(0, s.find(',')) << " = " << x << " | "; debug(s.substr(s.find(',') + 2), args...);}

int n, a[200005], st[800005];

void build(int p, int l, int r) {
    if (l == r) {
        st[p] = a[l];
        return;
    }
    int m = (l + r) / 2;
    build(2*p, l, m);
    build(2*p+1, m+1, r);
    st[p] = max(st[2*p], st[2*p+1]);
}

void update(int p, int l, int r, int i, int v) {
    if (l == r) {
        st[p] = v;
        return;
    }
    int m = (l + r) / 2;
    if (i <= m)
        update(2*p, l, m, i, v);
    else
        update(2*p+1, m+1, r, i, v);
    st[p] = max(st[2*p], st[2*p+1]);
}

int queryMax(int p, int l, int r, int i, int j) {
    if (i > r || j < l)
        return INT_MIN;
    if (i <= l && r <= j)
        return st[p];
    int m = (l + r) / 2;
    return max(queryMax(2*p, l, m, i, j), queryMax(2*p+1, m+1, r, i, j));
}

int queryJ(int p, int l, int r, int i, int v) {
    if (i > r || st[p] < v)
        return n;
    if (l == r)
        return l;
    int m = (l + r) / 2, ret = queryJ(2*p, l, m, i, v);
    if (ret == n)
        ret = queryJ(2*p+1, m+1, r, i, v);
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int q;
    cin >> n >> q;
    for (int i=0; i<n; i++)
        cin >> a[i];

    build(1, 0, n-1);
    for (int i=0; i<q; i++) {
        int t, x, y;
        cin >> t >> x >> y;
        x--;
        if (t == 1)
            update(1, 0, n-1, x, y);
        else if (t == 2)
            cout << queryMax(1, 0, n-1, x, y-1) << "\n";
        else
            cout << queryJ(1, 0, n-1, x, y) + 1 << "\n";
    }

    return 0;
}
