#include <iostream>
#include <iomanip>
#include <complex>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
using namespace std;
const double EPS = 1e-8;
const double INF = 1e12;
const double PI = acos(-1);
#define EQ(n,m) (abs((n)-(m)) < EPS)
#define X real()
#define Y imag()

typedef complex<double> P;
typedef vector<P> VP;
struct L : array<P, 2>{
    L(const P& a, const P& b){ at(0)=a; at(1)=b; }
    L(){}
};
struct C{
    P p;
    double r;
    C(const P& p, const double& r) : p(p), r(r) {}
    C(){}
};

namespace std{
    bool operator < (const P& a, const P& b){
        return !EQ(a.X,b.X) ? a.X<b.X : a.Y+EPS<b.Y;
    }
    bool operator == (const P& a, const P& b){
        return abs(a-b) < EPS;
    }
}

double dot(P a, P b){
    return (conj(a)*b).X;
}
double cross(P a, P b){
    return (conj(a)*b).Y;
}
int ccw(P a, P b, P c){
    b -= a;
    c -= a;
    if(cross(b,c) > EPS) return +1; //ccw
    if(cross(b,c) < -EPS) return -1; //cw
    if(dot(b,c) < -EPS) return +2; //c-a-b
    if(abs(c)-abs(b) > EPS) return -2; //a-b-c
    return 0; //a-c-b
}
P unit(const P &p){
    return p/abs(p);
}
P rotate(const P &p, double rad){
    return p *P(cos(rad), sin(rad));
}

VP crosspointCC(C a, C b){
    VP ret;
    if(a.p == b.p && a.r == b.r){
        return ret;
    }
    if(a.r < b.r) swap(a,b);
    double dist = abs(b.p-a.p);
    P dir = a.r*unit(b.p-a.p);
    if(EQ(dist, a.r+b.r) || EQ(dist, a.r-b.r)){
        ret.push_back(a.p +dir);
    }else if(a.r-b.r < dist && dist < a.r+b.r){
        double cos = (a.r*a.r +dist*dist -b.r*b.r)/(2*a.r*dist);
        double sin = sqrt(1 -cos*cos);
        ret.push_back(a.p +dir*P(cos, sin));
        ret.push_back(a.p +dir*P(cos, -sin));
    }
    return ret;
}

struct edge{
    int from,to;
    double v;
    edge(int f, int t, double v):from(f),to(t),v(v){}
    edge(){};
};

vector<int> linear_division(const VP &p){
    int n = p.size();
    vector<int> ret;
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            int ccwbit = 0;
            vector<pair<P, int> > online;
            for(int k=0; k<n; k++){
                if(ccw(p[i], p[j], p[k]) == 1){
                    ccwbit |= 1<<k;
                }else if(ccw(p[i], p[j], p[k]) != -1){
                    online.emplace_back(p[k], k);
                }
            }
            sort(online.begin(), online.end());
            for(int d=0; d<2; d++){
                for(int k=0; k<(int)online.size(); k++){
                    ccwbit ^= 1<<online[k].second;
                    if((ccwbit & 1) == 0){
                        ret.push_back(ccwbit ^ ((1<<n) -1));
                    }else{
                        ret.push_back(ccwbit);
                    }
                }
            }
        }
    }
    sort(ret.begin(), ret.end());
    ret.erase(unique(ret.begin(), ret.end()), ret.end());
    return ret;
}

double solve_onewarp(const VP &p, const vector<edge> &e){
    int m = e.size();
    if(m == 0) return 0.0;

    vector<C> c(m);
    for(int i=0; i<m; i++){
        c[i] = C(p[e[i].from], abs(p[e[i].from] -p[e[i].to]));
    }
    vector<vector<double> > cpa(m);
    for(int i=0; i<m; i++){
        for(int j=0; j<m; j++){
            VP cp = crosspointCC(c[i], c[j]);
            for(const P &point: cp){
                cpa[i].push_back(arg(point -c[i].p));
            }
        }
        cpa[i].push_back(-PI);
        cpa[i].push_back(PI);
        sort(cpa[i].begin(), cpa[i].end());
    }

    VP cand;
    for(int i=0; i<m; i++){
        for(int j=0; j<(int)cpa[i].size()-1; j++){
            double angle = (cpa[i][j] +cpa[i][j+1]) /2;
            P rot = rotate(P(c[i].r, 0), angle);
            cand.push_back(c[i].p +rot +unit(rot)*EPS*10.0);
            cand.push_back(c[i].p +rot -unit(rot)*EPS*10.0);
        }
    }

    double ret = INF;
    for(const P &point: cand){
        long long int inout = 0;
        double weight = 0;
        P g(0, 0);
        for(int i=0; i<m; i++){
            if(abs(point -c[i].p) < c[i].r +EPS){
                double w = 1/e[i].v /e[i].v;
                g += w *c[i].p;
                inout |= 1LL<<i;
                weight += w;
            }
        }
        g /= weight;
        double sub = 0;
        for(int i=0; i<m; i++){
            if((1LL<<i & inout) != 0){
                sub += norm((p[e[i].from] -g) /e[i].v);
            }else{
                sub += norm((p[e[i].from] -p[e[i].to]) /e[i].v);
            }
        }
        ret = min(ret, sub);
    }
    return ret;
}

double solve_twowarp(const VP &p, const vector<edge> &e){
    vector<int> division = linear_division(p);
    double ret = INF;
    for(int bit: division){
        vector<vector<edge> > newe(2);
        for(const edge &ed: e){
            newe[(1<<ed.from & bit) != 0].push_back(ed);
        }
        ret = min(ret, solve_onewarp(p, newe[0]) +solve_onewarp(p, newe[1]));
    }
    return sqrt(ret /e.size());
}

int main(){
    while(1){
        int n,m;
        cin >> n >> m;
        if(n==0) break;

        VP p(n);
        for(int i=0; i<n; i++){
            double x,y;
            cin >> x >> y;
            p[i] = P(x, y);
        }
        vector<edge> e(m);
        for(int i=0; i<m; i++){
            cin >> e[i].from >> e[i].to >> e[i].v;
            e[i].from--; e[i].to--;
        }
        cout << fixed << setprecision(10);
        cout << solve_twowarp(p, e) << endl;
    }
    return 0;
}
