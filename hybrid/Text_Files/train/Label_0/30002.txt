#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
//#include<list>
#include<queue>
#include<deque>
#include<algorithm>
//#include<numeric>
#include<utility>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef long double Real;

Real eps = 1e-12;

Real add(Real a, Real b) {
    if (abs(a+b) < eps * (abs(a)+abs(b))) return 0;
    return a+b;
}

bool equal(Real a, Real b) {
    return add(a, -b) == 0;
}

struct P {
    Real x, y;
    P() {}
    P(Real x, Real y) : x(x), y(y) {}
    P operator+(P p) const {return P(add(x, p.x), add(y, p.y));}
    P operator-(P p) const {return P(add(x, -p.x), add(y, -p.y));}
    P operator*(Real d) const {return P(x*d, y*d);}
    Real dot(P p) const {return add(x*p.x, y*p.y);} // ??????
    Real det(P p) const {return add(x*p.y, -y*p.x);} // ??????
    Real dist(P p) const {return sqrt((x-p.x)*(x-p.x) + (y-p.y)*(y-p.y));} // ?????¢
    void normalize() {Real d = sqrt(x*x+y*y); x /= d; y /= d;} // ??£??????
    bool operator<(const P& rhs) const {
        if (x != rhs.x) return x < rhs.x;
        return y < rhs.y;
    }
    bool operator==(const P& rhs) const {
        return equal(x, rhs.x) && equal(y, rhs.y);
    }
};

// ??????p1-p2?????????q???????????????????????????
bool on_seg(P p1, P p2, P q) {
    return (p1-q).det(p2-q) == 0 && (p1-q).dot(p2-q) <= 0;
}

// ??´???p1-p2??¨??´???q1-q2??????????????????????????????
bool parallel(P p1, P p2, P q1, P q2) {
    P a = p2-p1;
    P b = q2-q1;
    return a.det(b) == 0;
}

const int MAXN = 55;
P pnts[MAXN];
int n;

void solve() {
    if (n % 2 == 1) {
        cout << "NA" << endl;
        return;
    }
    Real ax = 0, ay = 0;
    for (int i = 0; i < n; i++) {
        ax += pnts[i].x;
        ay += pnts[i].y;
    }
    ax /= n; ay /= n;
    P a(ax, ay);
    for (int i = 0; i < n/2; i++) {
        if (!on_seg(pnts[i], pnts[i+n/2], a) || a.dist(pnts[i]) != a.dist(pnts[i+n/2])) {
            cout << "NA" << endl;
            return;
        }
    }
    printf("%.10Lf %.10Lf\n", ax, ay);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> pnts[i].x >> pnts[i].y;
    solve();
    return 0;
}