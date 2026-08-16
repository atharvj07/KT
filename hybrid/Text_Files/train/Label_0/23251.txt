#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<(int)(n); ++i)
using namespace std;

typedef vector<int> Node;
typedef vector<Node> Graph;

typedef unsigned long long ULL;

inline int trail0(ULL s) { return (s ? __builtin_ctzll(s) : 64); }


using namespace std;
typedef complex<double> P;
typedef vector<P> Pol;
typedef vector<P> L;
P vec(L l){return l[1] - l[0];}

P next(const Pol& pol, int k) {
    if(k == pol.size() - 1) {
        return pol[0];
    } else {
        return pol[k + 1];
    }
}
const double EPS = 1e-6;
int sign(double x){ return x > EPS ? 1 : x < -EPS ? -1 : 0; }

double dot(P a, P b){return real(conj(a) * b);}
double cross(P a, P b){return imag(conj(a) * b);}
int ccw(P a, P b, P c) {
    b -= a; c -= a;
    if (cross(b, c) > +EPS)   return +1; 
    if (cross(b, c) < -EPS)   return -1; 
    if (sign(dot(b, c)) <= 0)     return +2; 
    if (sign(norm(b) - norm(c)) <= 0) return -2; 
    return 0;                        
}
bool paralell(L l, L m){return sign(cross(vec(l), vec(m))) == 0;}
bool equalLL(L l, L m){return paralell(l, m) && sign(cross(vec(l), m[0] - l[0])) == 0;}

bool iSS(L s, L t) {
    if(!equalLL(s, t)) return false;
    P unit = (s[1] - s[0]) / abs(s[1] - s[0]);
    double a = dot(unit, t[0] - s[0]);
    double b = dot(unit, t[1] - s[0]);
    double c = 0;
    double d = dot(unit, s[1] - s[0]);
    if(a > b) swap(a, b);
    if(c > d) swap(c, d);
    if(sign(b - c) <= 0 || sign(d - a) <= 0) return false;
    return true;
}

int n;
bool d[50][50];
int deg[50];
bool a[50];
bool no[50];

int color[50];
bool bip_dfs(int u, int c) {
    if(color[u] != -1 && color[u] != c) return false;
    if(color[u] == c) return true;
    color[u] = c;
    REP(i, n) if(d[u][i] && !a[i]) {
        bool res = bip_dfs(i, c ^ 1);
        if(!res) return false;
    }
    return true;
}

bool bip() {
    REP(i, n) color[i] = -1;
    REP(i, n) if(color[i] == -1 && !a[i]) if(!bip_dfs(i, 0)) return false;
    return true;
}

bool BronKerbosch(const vector<ULL>& g, ULL cur, ULL allowed, ULL forbidden){
    if (allowed == 0 && forbidden == 0) {
        REP(i, n) a[i] = (cur >> i & 1);
        return bip();
    }
    if (allowed == 0) return false;
    int pivot = trail0(allowed | forbidden);
    ULL z = allowed & ~g[pivot];
    for (int u = trail0(z); u < g.size(); u += trail0(z >> (u + 1)) + 1) {
        if(BronKerbosch(g, cur | (1ULL << u), allowed & g[u], forbidden & g[u])) return true;
        allowed ^= 1ULL << u;
        forbidden |= 1ULL << u;
    }
    return false;
}

bool run(){
    assert(n < 64);
    vector<ULL> g(n);
    REP(i, n) REP(j, n) if(i != j) g[i] |= (1ULL << j);
    REP(i, n) REP(j, n) if(i != j && d[i][j]) g[i] ^= (1ULL << j);
    return BronKerbosch(g, 0, (1ULL << n) - 1, 0);
}

int solve() {
    memset(a, 0, sizeof(a));
    memset(no, 0, sizeof(no));

    bool exist = false;
    REP(i, n) REP(j, n) if(d[i][j]) exist = true;

    if(!exist) {
        return 1;
    } else if(bip()) {
        return 2;
    } else if(run()) {
        return 3;
    } else {
        return 4;
    }
}

void max_1() {
    n = 35;
    REP(i, n) REP(j, n) d[i][j] = false;
    assert(solve() == 1);
}

void max_2() {
    n = 35;
    REP(i, n) REP(j, n) d[i][j] = (i % 2 != j % 2);
    assert(solve() == 2);
}

int color_slow[35];
bool slow(int k) {
    if(k == n) {
        REP(i, n) REP(j, n) if(d[i][j] && color_slow[i] == color_slow[j]) return false;
        return true;
    }
    REP(i, 3) {
        color_slow[k] = i;
        if(slow(k + 1)) return true;
    }
    return false;
}


void test() {
    n = 10;
    double pos = 1.0 * rand() / RAND_MAX;
    REP(i, n) REP(j, i) d[i][j] = d[j][i] = (1.0 * rand() / RAND_MAX > pos);

    int ans = (slow(0) ? 3 : 4);
    int act = solve();
    cout << act << endl;
    if(!(act <= 2 || act == ans)) {
        cout << "actual: " << act << endl;
        cout << "assert: " << ans << endl;
        REP(j, n) REP(i, j) if(d[i][j]) cout << i << " <-> " << j << endl;
        assert(false);
    }
}


int main(){
    while(cin >> n && n > 0) {
        vector<Pol> pols(n);
        REP(i, n) {
            int m;
            cin >> m;
            REP(_, m) {
                double x, y;
                cin >> x >> y;
                pols[i].push_back({x, y});
            }
        }

        REP(i, n) REP(j, n) d[i][j] = false;
        REP(i, n) deg[i] = 0;

        for(int i = 0; i < n; i++) {
            for(int k = 0; k < pols[i].size(); k++) {
                L l = {pols[i][k], next(pols[i], k)};
                for(int j = i + 1; j < n; j++) {
                    for(int h = 0; h < pols[j].size(); h++) {
                        L m = {pols[j][h], next(pols[j], h)};
                        if(iSS(l, m)) {
                            d[i][j] = d[j][i] = true;
                            deg[i]++;
                            deg[j]++;
                            break;
                        }
                    }
                }
            }
        }


        cout << solve() << endl;

    }
    return 0;
}