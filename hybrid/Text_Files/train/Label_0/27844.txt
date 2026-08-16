#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <random>
#include <vector>
#include <array>
#include <bitset>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <complex>
#include <cmath>

using namespace std;
using uint = unsigned int;
using ll = long long;
using ull = unsigned long long;
constexpr ll TEN(int n) { return (n==0) ? 1 : 10*TEN(n-1); }
template<class T> using V = vector<T>;
template<class T> using VV = V<V<T>>;


using R = long double;
using P = complex<R>;

const R EPS = 1e-10;
const R PI = acos(R(-1));

int sgn(R a) {
    if (abs(a) <= EPS) return 0;
    return (a < 0) ? -1 : 1;
}

int sgn(R a, R b) {
    return sgn(b-a);
}

bool near(P a, P b) {
    return !sgn(abs(a-b));
}

bool lessP(P l, P r) {
    if (sgn(l.real(), r.real())) return l.real() < r.real();
    if (sgn(l.imag(), r.imag())) return l.imag() < r.imag();
    return false;
}

R cross(P a, P b) { return a.real()*b.imag() - a.imag()*b.real(); }
R dot(P a, P b) { return a.real()*b.real() + a.imag()*b.imag(); }

/*
  1->cclock
 -1->clock
  0->on
  2->back
 -2->front
 */
int ccw(P a, P b, P c) {
    assert(!near(a, b));
    if (near(a, c) || near(b, c)) return 0;
    int s = sgn(cross(b-a, c-a));
    if (s) return s;
    if (dot(b-a, c-a) < 0) return 2;
    if (dot(a-b, c-b) < 0) return -2;
    return 0;
}

struct L {
    P x, y;
    L() {}
    L(P x, P y) :x(x), y(y) {}
    P vec() { return y-x; }
};

struct T {
    P d[3];
    T() {}
    T(P x, P y, P z) {
        d[0] = x; d[1] = y; d[2] = z;
    }
    P& operator[](int p) {
        return d[p];
    }
    const P& operator[](int p) const {
        return d[p];
    }
    int size() const {
        return 3;
    }
};

using Pol = V<P>;

struct C {
    P p; R r;
    C() {}
    C(P p, R r) : p(p), r(r) {}
};

C circumCircle(T t) {
    P a = t.d[0], b = t.d[1], c = t.d[2];
    b -= a; c -= a;
    R s = 2*cross(b, c);
    R x = norm(b-c), y = norm(c), z = norm(b);
    R S = x+y+z;
    P r = (y*(S-2*y)*b+z*(S-2*z)*c)/(s*s);
    return C(r + a, abs(r));
}

C smallestEnclosingCircle(Pol &p, int ps, T q = T(), int qs = 0) {
    if (!ps) {
        switch (qs) {
            case 0:
                return C(P(0, 0), -1);
            case 1:
                return C(q.d[0], 0);
            case 2:
                return C((q.d[0]+q.d[1])/R(2.0), abs(q.d[0]-q.d[1])/R(2.0));
            case 3:
                return circumCircle(q);
        }
        assert(false);
    }
    C c = smallestEnclosingCircle(p, ps-1, q, qs);
    if (sgn(c.r, abs(p[ps-1]-c.p)) == 1) {
        q.d[qs] = p[ps-1];
        return smallestEnclosingCircle(p, ps-1, q, qs+1);
    }
    return c;
}

const int MN = 14;
const int MM = 14;
int n, m;
P p[MN];
R pre[1<<MN];
R dp[MM+1][1<<MN];
bool vis[MM+1][1<<MN];

R solve(int f, int m) {
    if (f == 0) return 0;
    if (m == 0) return 1e100;
    if (vis[m][f]) return dp[m][f];
    vis[m][f] = true;
    R ans = 1e100;
    int g = 0;
    do {
        ans = min(ans, max(pre[g], solve(f^g, m-1)));
        g = ((g|~f)+1) & f;
    } while (g);
    return dp[m][f] = ans;
}
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout << setprecision(20);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        R x, y;
        cin >> x >> y;
        p[i] = P(x, y);
    }
    for (int f = 0; f < (1<<n); f++) {
        V<P> v;
        for (int i = 0; i < n; i++) {
            if (!(f & (1<<i))) continue;
            v.push_back(p[i]);
        }
        pre[f] = smallestEnclosingCircle(v, int(v.size())).r;

//        cout << f << " " << pre[f] << endl;
    }

    cout << solve((1<<n) - 1, m) << endl;
    return 0;
}

