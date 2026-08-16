#define  _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#pragma comment (linker, "/STACK:526000000")

#include "bits/stdc++.h"

using namespace std;
typedef string::const_iterator State;
#define eps 1e-5L
#define MAX_MOD 1000000007LL
#define GYAKU 500000004LL
#define seg_size 262144LL
#define MOD 998244353LL
#define pb push_back
#define mp make_pair
typedef long long ll;
#define REP(a,b) for(long long (a) = 0;(a) < (b);++(a))
#define ALL(x) (x).begin(),(x).end()

// geometry library

typedef complex<long double> Point;
typedef pair<complex<long double>, complex<long double>> Line;

typedef struct Circle {
    complex<long double> center;
    long double r;
}Circle;

//内積、 dot(a,b) = |a||b|cos()
long double dot(Point a, Point b) {
    return (a.real() * b.real() + a.imag() * b.imag());
}
//外積、cross(a,b) = |a||b|sin()
long double cross(Point a, Point b) {
    return (a.real() * b.imag() - a.imag() * b.real());
}

//線分と点の距離
long double Dist_Line_Point(Line a, Point b) {
    if (dot(a.second - a.first, b - a.first) < eps) return abs(b - a.first);
    if (dot(a.first - a.second, b - a.second) < eps) return abs(b - a.second);
    return abs(cross(a.second - a.first, b - a.first)) / abs(a.second - a.first);
}

//線分の交差判定
int is_intersected_ls(Line a, Line b) {
    return (cross(a.second - a.first, b.first - a.first) * cross(a.second - a.first, b.second - a.first) < 0) &&
        (cross(b.second - b.first, a.first - b.first) * cross(b.second - b.first, a.second - b.first) < 0);
}

//線分の交点
Point intersection_l(Line a, Line b) {
    Point da = a.second - a.first;
    Point db = b.second - b.first;
    return a.first + da * cross(db, b.first - a.first) / cross(db, da);
}

//線分と線分の距離
long double Dist_Line_Line(Line a, Line b) {
    if (is_intersected_ls(a, b) == 1) {
        return 0;
    }
    return min({ Dist_Line_Point(a,b.first), Dist_Line_Point(a,b.second),Dist_Line_Point(b,a.first),Dist_Line_Point(b,a.second) });
}

//円と円の交点
pair<Point, Point> intersection_Circle_Circle(Circle a, Circle b) {
    long double dist = abs(a.center - b.center);
    assert(dist <= eps + a.r + b.r);
    assert(dist+eps >= abs(a.r - b.r));
    Point target = b.center - a.center;
    long double pointer = target.real() * target.real() + target.imag() * target.imag();
    long double aa = pointer + a.r * a.r - b.r * b.r;
    aa /= 2.0L;
    Point l{ (aa * target.real() + target.imag() * sqrt(pointer * a.r * a.r - aa * aa))/pointer,
            (aa* target.imag() - target.real() * sqrt(pointer * a.r * a.r - aa * aa)) / pointer};
    Point r{ (aa * target.real() - target.imag() * sqrt(pointer * a.r * a.r - aa * aa)) / pointer,
        (aa * target.imag() + target.real() * sqrt(pointer * a.r * a.r - aa * aa)) / pointer };
    r = r + a.center;
    l = l + a.center;
    return mp(l, r);
}

//end of geometry

template<typename A>
A pows(A val, ll b) {
    assert(b >= 1);
    A ans = val;
    b--;
    while (b) {
        if (b % 2) {
            ans *= val;
        }
        val *= val;
        b /= 2LL;
    }
    return ans;
}

template<typename A>
class Compressor {
public:
    bool is_zipped = false;
    map<A, ll> zipper;
    map<ll, A> unzipper;
    queue<A> fetcher;
    Compressor(){
        is_zipped = false;
        zipper.clear();
        unzipper.clear();
    }
    void add(A now) {
        assert(is_zipped == false);
        zipper[now] = 1;
        fetcher.push(now);
    }
    void exec() {
        assert(is_zipped == false);
        int cnt = 0;
        for (auto i = zipper.begin(); i != zipper.end(); ++i) {
            i->second = cnt;
            unzipper[cnt] = i->first;
            cnt++;
        }
        is_zipped = true;
    }
    ll fetch() {
        assert(is_zipped == true);
        A hoge = fetcher.front();
        fetcher.pop();
        return zipper[hoge];
    }
    ll zip(A now) {
        assert(is_zipped == true);
        assert(zipper.find(now) != zipper.end());
        return zipper[now];
    }
    A unzip(ll a) {
        assert(is_zipped == true);
        assert(a < unzipper.size());
        return unzipper[a];
    }
    ll next(A now) {
        auto x = zipper.upper_bound(now);
        if (x == zipper.end()) return zipper.size();
        return (ll)((*x).second);
    }
    ll back(A now) {
        auto x = zipper.lower_bound(now);
        if (x == zipper.begin()) return -1;
        x--;
        return (ll)((*x).second);
    }
};

template<typename A>
class Matrix {
public:
    vector<vector<A>> data;
    Matrix(vector<vector<A>> a) :data(a){

    }
    Matrix operator + (const Matrix obj) {
        vector<vector<A>> ans;
        assert(obj.data.size() == this->data.size());
        assert(obj.data[0].size() == this->data[0].size());
        REP(i, obj.data.size()) {
            ans.push_back(vector<A>());
            REP(q, obj.data[i].size()) {
                A hoge = obj.data[i][q] + (this -> data[i][q]);
                ans.back().push_back(hoge);
            }
        }
        return Matrix(ans);
    }
    Matrix operator - (const Matrix obj) {
        vector<vector<A>> ans;
        assert(obj.data.size() == this->data.size());
        assert(obj.data[0].size() == this->data[0].size());
        REP(i, obj.data.size()) {
            ans.push_back(vector<A>());
            REP(q, obj.data[i].size()) {
                A hoge = this->data[i][q] - obj.data[i][q];
                ans.back().push_back(hoge);
            }
        }
        return Matrix(ans);
    }
    Matrix operator * (const Matrix obj) {
        vector<vector<A>> ans;
        assert(obj.data.size() == this->data[0].size());
        REP(i, this -> data.size()) {
            ans.push_back(vector<A>());
            REP(q, obj.data[0].size()) {
                A hoge = (this -> data[i][0]) * (obj.data[0][q]);
                for(int t = 1;t < obj.data[i].size();++t){
                    hoge += this -> data[i][t] * obj.data[t][q];
                }
                ans.back().push_back(hoge);
            }
        }
        return Matrix(ans);
    }
    Matrix &operator *= (const Matrix obj) {
        *this = (*this * obj);
        return *this;
    }
    Matrix& operator += (const Matrix obj) {
        *this = (*this + obj);
        return *this;
    }
    Matrix& operator -= (const Matrix obj) {
        *this = (*this - obj);
        return *this;
    }
};

class modint {
public:
    using u64 = std::uint_fast64_t;
    u64 value = 0;
    u64 mod;
    modint(ll a, ll b): value(((a%b) + 2 * b) % b),mod(b) {

    }
    modint operator+(const modint rhs) const{
        return modint(*this) += rhs;
    }
    modint operator-(const modint rhs) const{
        return modint(*this) -= rhs;
    }
    modint operator*(const modint rhs) const {
        return modint(*this) *= rhs;
    }
    modint operator/(const modint rhs) const{
        return modint(*this) /= rhs;
    }
    modint& operator+=(const modint rhs) {
        assert(rhs.mod == mod);
        value += rhs.value;
        if (value >= mod) {
            value -= mod;
        }
        return *this;
    }
    modint& operator-=(const modint rhs) {
        assert(rhs.mod == mod);
        if (value < rhs.value) {
            value += mod;
        }
        value -= rhs.value;
        return *this;
    }
    modint& operator*=(const modint rhs) {
        assert(rhs.mod == mod);
        value = (value *  rhs.value) % mod;
        return *this;
    }
    modint& operator/=(modint rhs) {
        assert(rhs.mod == mod);
        ll rem = mod - 2;
        while (rem) {
            if (rem % 2) {
                *this *= rhs;
            }
            rhs *= rhs;
            rem /= 2LL;
        }
        return *this;
    }
    friend ostream& operator<<(ostream& os, modint& p) {
        os << p.value;
        return (os);
    }
};

template<typename A,typename B>
class Dijkstra {
public:
    vector<vector<pair<int, A>>> vertexs;
    B Cost_Function;
    Dijkstra(int n, B cost) : Cost_Function(cost){
        vertexs = vector<vector<pair<int, A>>>(n, vector<pair<int, A>>{});
    }
    ~Dijkstra() {
        vertexs.clear();
    }
    void add_edge(int a, int b, A c) {
        vertexs[a].push_back(mp(b, c));
    }
    vector<ll> build_result(int StartPoint) {
        vector<ll> dist(vertexs.size(), 2e18);
        dist[StartPoint] = 0;
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> next;
        next.push(make_pair(0, StartPoint));
        while (next.empty() == false) {
            pair<ll, int> now = next.top();
            next.pop();
            if (dist[now.second] != now.first) continue;
            for (auto x : vertexs[now.second]) {
                ll now_cost = now.first + Cost_Function(x.second);
                if (dist[x.first] > now_cost) {
                    dist[x.first] = now_cost;
                    next.push(mp(now_cost, x.first));
                }
            }
        }
        return dist;
    }
};

void init() {
    iostream::sync_with_stdio(false);
    cout << fixed << setprecision(20);
}

unsigned long xor128() {
    static unsigned long x = 123456789, y = 362436069, z = 521288629, w = 88675123;
    unsigned long t = (x ^ (x << 11));
    x = y; y = z; z = w;
    return (w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)));
}

#define int ll
long double pw;
int n;
vector<tuple<long double, long double, long double, long double>> inputs;

long double calc(long double now) {
    long double ans = now * pw;
    REP(i, inputs.size()) {
        long double val = get<3>(inputs[i]) - get<0>(inputs[i]) * now;
        ans += max(0.0L, (val / get<2>(inputs[i])) * get<1>(inputs[i]));
    }
    return ans;
}
void solve(){
    while (true) {
        cin >> n;
        if (n == 0) return;
        cin >> pw;
        inputs.clear();
        REP(i, n) {
            long double a, b, c, d;
            cin >> a >> b >> c >> d;
            inputs.push_back(make_tuple(a, b, c, d));
        }
        long double bot = 0;
        long double top = 1e18;
        REP(tea, 200) {
            long double mid1 = (bot + bot + top) / 3.0L;
            long double mid2 = (bot + top + top) / 3.0L;
            if (calc(mid1) < calc(mid2)) {
                top = mid2;
            }
            else {
                bot = mid1;
            }
        }
        cout << calc(bot) << endl;
    }
}

#undef int
int main() {
    init();
    solve();
}
