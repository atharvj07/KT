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

bool intersectSP(const L& s, const P &p){
    return abs(cross(s[0]-p, s[1]-p))<EPS  && dot(s[0]-p, s[1]-p)<EPS;
}

P projection(const L& l, const P& p) {
    double t = dot(p-l[0], l[0]-l[1]) / norm(l[0]-l[1]);
    return l[0] + t*(l[0]-l[1]);
}

double distanceLP(const L &l, const P &p) {
    return abs(cross(l[1]-l[0], p-l[0])) /abs(l[1]-l[0]);
}

VP crosspointCL(const C &c, const L &l){
    VP ret;
    P mid = projection(l, c.p);
    double d = distanceLP(l, c.p);
    if(EQ(d, c.r)){
        ret.push_back(mid);
    }else if(d < c.r){
        double len = sqrt(c.r*c.r -d*d);
        ret.push_back(mid +len*unit(l[1]-l[0]));
        ret.push_back(mid -len*unit(l[1]-l[0]));
    }
    return ret;
}
VP crosspointCS(const C &c, const L &s){
    VP ret;
    VP cp = crosspointCL(c,s);
    for(int i=0; i<(int)cp.size(); i++){
        if(intersectSP(s, cp[i])){
            ret.push_back(cp[i]);
        }
    }
    return ret;
}

double getarea(const VP &poly){
    double ret = 0;
    for (int i=0; i<(int)poly.size(); i++){ 
        ret += cross(poly[i], poly[(i+1)%poly.size()]);
    }
    return ret*0.5;
}
int in_poly(const P &p, const VP &poly){
    int n = poly.size();
    int ret = -1;
    for(int i=0; i<n; i++){
        P a = poly[i]-p;
        P b = poly[(i+1)%n]-p;
        if(a.Y > b.Y) swap(a,b);
        if(intersectSP(L(a,b), P(0,0))) return 0;
        if(a.Y<=0 && b.Y>0 && cross(a,b)<0) ret = -ret;
    }
    return ret;
}

bool epseq(const double &a, const double &b){
    return abs(a-b) < EPS;
}

int main(){
    double r;
    int n;
    cin >> r >> n;
    VP p(n);
    for(int i=0; i<n; i++){
        double x,y;
        cin >> x >> y;
        p[i] = P(x, y);
    }
    C c(P(0, 0), r);
    if(getarea(p) < 0){
        reverse(p.begin(), p.end());
    }

    vector<VP> cp(n);
    vector<double> angle;
    angle.push_back(-PI);
    for(int i=0; i<n; i++){
        cp[i].push_back(p[i]);
        cp[i].push_back(p[(i+1)%n]);
        VP ret = crosspointCS(c, L(p[i], p[(i+1)%n]));
        for(P p: ret){
            cp[i].push_back(p);
            angle.push_back(arg(p));
        }
        sort(cp[i].begin(), cp[i].end());
        cp[i].erase(unique(cp[i].begin(), cp[i].end()), cp[i].end());
        if(cp[i][0] != p[i]){
            reverse(cp[i].begin(), cp[i].end());
        }
    }
    sort(angle.begin(), angle.end());
    angle.erase(unique(angle.begin(), angle.end(), epseq), angle.end());
    if(epseq(angle.back(), PI)){
        angle.pop_back();
    }

    int idx, sidx;
    bool poly;
    P pmin = *min_element(p.begin(), p.end());
    if(P(-r, 0) == pmin || P(-r, 0) < pmin){
        idx = 0;
        poly = false;
        pmin = P(-r, 0);
    }else{
        idx = min_element(p.begin(), p.end()) -p.begin();
        sidx = 0;
        poly = true;
    }

    P curr = pmin;
    double ans = 0;
    do{
        if(poly){
            //次の辺に切り替わる
            if(sidx == (int)cp[idx].size()-1){
                idx = (idx +1)%n;
                sidx = 0;
                continue;
            }
            P mid = (cp[idx][sidx] +cp[idx][sidx+1]) /2.0;
            //円に切り替わる
            if(abs(mid) < r){
                double a = arg(cp[idx][sidx]);
                if(epseq(PI, a)){
                    a = -PI;
                }
                for(int i=0; i<(int)angle.size(); i++){
                    if(epseq(angle[i], a)){
                        idx = i;
                        break;
                    }
                }
                poly = false;
                continue;
            }
            ans += abs(cp[idx][sidx+1] -cp[idx][sidx]);
            sidx++;
            curr = cp[idx][sidx];
        }else{
            int m = angle.size();
            double ai1 = (idx == m-1)? PI: angle[idx+1];
            P mid = rotate(P(r, 0), (angle[idx] +ai1)/2);
            //多角形に切り替わる
            if(in_poly(mid, p) > 0){
                for(int i=0; i<n; i++){
                    for(int j=0; j<(int)cp[i].size(); j++){
                        if(cp[i][j] == curr){
                            idx = i;
                            sidx = j;
                            i = n;
                            break;
                        }
                    }
                }
                poly = true;
                continue;
            }
            ans += r *(ai1 -angle[idx]);
            idx = (idx+1)%m;
            curr = rotate(P(r, 0), angle[idx]);
        }
    }while(!(curr == pmin));

    cout << fixed << setprecision(10);
    cout << ans << endl;
    return 0;
}
