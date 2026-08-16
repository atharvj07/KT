#include <iostream>
#include <iomanip>
#include <complex>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
#include <cassert>
#include <utility>
using namespace std;
const double EPS = 1e-10;
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

bool intersectSS(const L& a, const L& b){
    return ( ccw(a[0],a[1],b[0]) *ccw(a[0],a[1],b[1]) <= 0 ) &&
        ( ccw(b[0],b[1],a[0]) *ccw(b[0],b[1],a[1]) <= 0 );
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
double distanceSP(const L &s, const P &p) {
    if(dot(s[1]-s[0], p-s[0]) < EPS) return abs(p-s[0]);
    if(dot(s[0]-s[1], p-s[1]) < EPS) return abs(p-s[1]);
    return distanceLP(s, p);
}
double distanceSS(const L &s, const L &t) {
  if (intersectSS(s, t)) return 0;
  return min(min(distanceSP(s, t[0]), distanceSP(s, t[1])),
             min(distanceSP(t, s[0]), distanceSP(t, s[1])));
}

double distanceGP(const VP &g, const P &p){
    double ret = INF;
    int n = g.size();
    for(int i=0; i<n; i++){
        ret = min(ret, distanceSP(L(g[i], g[(i+1)%n]), p));
    }
    return ret;
}

bool isParallel(const P &a, const P &b){
    return abs(cross(a,b)) < EPS;
}
bool isParallel(const L &a, const L &b){
    return isParallel(a[1]-a[0], b[1]-b[0]);
}

P crosspointLL(const L &l, const L &m) {
  double A = cross(l[1]-l[0], m[1]-m[0]);
  double B = cross(l[1]-l[0], l[1]-m[0]);
  return m[0] + B/A *(m[1]-m[0]);
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

//////////////

L ppbisector(const P &a, const P &b){
    P mid = (a +b) /2.0;
    return L(mid, mid +(b-a)*P(0,1));
}
vector<L> ppbisectorll(const L &a, const L &b){
    vector<L> ret;
    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            ret.push_back(ppbisector(a[i], b[j]));
        }
    }
    return ret;
}

vector<L> llbisector(const L &a, const L &b){
    vector<L> ret;
    if(isParallel(a, b)){
        P mid = (a[0] +b[0]) /2.0;
        ret.emplace_back(mid, mid +(a[1] -a[0]));
        return ret;
    }
    P cp = crosspointLL(a, b);
    P adir = (a[0] == cp)? a[1]-cp : a[0]-cp;
    P bdir = (b[0] == cp)? b[1]-cp : b[0]-cp;
    double angle = arg(bdir /adir) /2.0;
    ret.emplace_back(cp, cp +rotate(adir, angle));
    ret.emplace_back(cp, cp +rotate(adir, angle +PI/2.0));
    return ret;
}

vector<double> solve_quadeq(double a, double b, double c){
    vector<double> ret;
    if(abs(a) < EPS){
        if(abs(b) > EPS) ret.push_back(-c/b);
        return ret;
    }
    double d = b*b -4*a*c;
    if(abs(d) < EPS) d = 0;
    if(d < 0) return ret;
    if(d < 0) d = 0;
    ret.push_back((-b +sqrt(d))/(2*a));
    ret.push_back((-b -sqrt(d))/(2*a));
    return ret;
}

struct quadratic{
    double a,b,c,d,e,f;
};

//Lを ax+by+c=0 の形に変換
vector<double> conv_coeff(const L &l){
    double x = l[1].X -l[0].X;
    double y = l[1].Y -l[0].Y;
    return vector<double>{y, x, x*l[0].Y -y*l[0].X};
}
//ax+by+c=0 と (x,y) からの距離が等しい点の軌跡(二次曲線)の係数を返す
quadratic bisecquad(double a, double b, double c, double x, double y){
    quadratic ret;
    double A = (a*a +b*b);
    ret.a = b*b;
    ret.b = -2*a*b;
    ret.c = a*a;
    ret.d = -2*(A*x +a*c);
    ret.e = -2*(A*y +b*c);
    ret.f = A*(x*x +y*y) +c*c;
    return ret;
}
//yでのquadの値
vector<double> solveCPQL(quadratic q, double y){
    return solve_quadeq(q.a, q.b*y +q.d, q.c*y*y +q.e*y +q.f);
}

bool epseq(const double &a, const double &b){
    return abs(a-b) <EPS;
}    

pair<vector<L>, vector<quadratic> >
list_volonoi_border(const vector<VP> &island){
    int m = island.size();
    vector<L> bisec;
    vector<quadratic> coeff;
    for(int i=0; i<m; i++){
        for(int j=i+1; j<m; j++){
            int si = island[i].size();
            int sj = island[j].size();
            for(int ii=0; ii<si; ii++){
                for(int ij=0; ij<sj; ij++){
                    L ei(island[i][ii], island[i][(ii+1)%si]);
                    L ej(island[j][ij], island[j][(ij+1)%sj]);
                    vector<L> ret;
                    ret = ppbisectorll(ei, ej);
                    bisec.insert(bisec.end(), ret.begin(), ret.end());
                    ret = llbisector(ei, ej);
                    bisec.insert(bisec.end(), ret.begin(), ret.end());
                    for(int d=0; d<2; d++){
                        vector<double> cl = conv_coeff(ei);
                        coeff.push_back(bisecquad(cl[0], cl[1], cl[2], ej[0].X, ej[0].Y));
                        coeff.push_back(bisecquad(cl[0], cl[1], cl[2], ej[1].X, ej[1].Y));
                        swap(ei, ej);
                    }
                }
            }
        }
    }
    return make_pair(bisec, coeff);
}

int main(){
    cout << fixed << setprecision(1);
    bool firstcase = true;
    while(1){
        int m,n;
        cin >> m >> n;
        //m: island, n: resource
        if(m == 0) break;
        if(firstcase){
            firstcase = false;
        }else{
            cout << endl;
        }
        
        double d;
        cin >> d;
        vector<VP> island(m), resource(n);
        vector<double> amount(n);
        for(int i=0; i<m; i++){
            int num;
            cin >> num;
            island[i].resize(num);
            for(int j=0; j<num; j++){
                int x,y;
                cin >> x >> y;
                island[i][j] = P(x, y);
            }
        }
        for(int i=0; i<n; i++){
            int num;
            cin >> amount[i] >> num;
            resource[i].resize(num);
            for(int j=0; j<num; j++){
                int x,y;
                cin >> x >> y;
                resource[i][j] = P(x, y);
            }
        }

        //多角形ボロノイ図の分割候補となる線分、二次曲線の係数を列挙
        auto vret = list_volonoi_border(island);
        vector<L> &bisec = vret.first;
        vector<quadratic> &coeff = vret.second;
        
        //島からの距離がdになる境界線
        vector<L> liml;
        vector<C> limc;
        for(int i=0; i<m; i++){
            int si = island[i].size();
            for(int j=0; j<si; j++){
                L edge(island[i][j], island[i][(j+1)%si]);
                P dir = unit(edge[1] -edge[0]) *d *P(0, -1);
                liml.emplace_back(edge[0] +dir, edge[1] +dir);
                limc.emplace_back(island[i][j], d);
            }
        }
        
        //ここからがメイン部分
        //直線 y=h を考え, hを細かく切って数値積分する
        double lb = 0.0, ub = 50.0;
        int splitnum = 2e3;
        double dy = (ub -lb) /splitnum;
        vector<vector<vector<double> > > len(m, vector<vector<double> >(n, vector<double>(splitnum+1, 0)));
        for(int i=0; i<=splitnum; i++){
            double y = lb +i*dy;
            L seg(P(lb, y), P(ub, y));
            //範囲外除去は今はやらない(どうせにぶたんするので)
            vector<double> cpx;
            for(const L &l: bisec){
                if(!isParallel(l, seg)){
                    P cp = crosspointLL(l, seg);
                    cpx.push_back(cp.X);
                }
            }
            for(const quadratic &quad: coeff){
                vector<double> ret = solveCPQL(quad, y);
                cpx.insert(cpx.end(), ret.begin(), ret.end());
            }
            for(const L &l: liml){
                if(!isParallel(l, seg)){
                    P cp = crosspointLL(l, seg);
                    cpx.push_back(cp.X);
                }
            }
            for(const C &c: limc){
                VP ret = crosspointCL(c, seg);
                for(const P &p: ret){
                    cpx.push_back(p.X);
                }
            }
               
            sort(cpx.begin(), cpx.end());
            cpx.erase(unique(cpx.begin(), cpx.end(), epseq), cpx.end());

            //各resourceについて
            for(int j=0; j<n; j++){
                //xの上下限
                vector<double> xlim;
                int sj = resource[j].size();
                for(int k=0; k<sj; k++){
                    L edge(resource[j][k], resource[j][(k+1)%sj]);
                    if(!isParallel(edge, seg) && intersectSS(edge, seg)){
                        P cp = crosspointLL(edge, seg);
                        xlim.push_back(cp.X);
                    }
                }
                sort(xlim.begin(), xlim.end());
                xlim.erase(unique(xlim.begin(), xlim.end(), epseq), xlim.end());
                if((int)xlim.size() < 2) continue;

                //resourceの範囲中での交点集合
                vector<double> ncpx;
                auto xbeg = lower_bound(cpx.begin(), cpx.end(), xlim[0] +EPS);
                auto xend = lower_bound(cpx.begin(), cpx.end(), xlim[1] -EPS);
                ncpx.push_back(xlim[0]);
                ncpx.insert(ncpx.end(), xbeg, xend);
                ncpx.push_back(xlim[1]);
                //各分割区間について、最も近い島に長さを加算
                for(int k=0; k<(int)ncpx.size()-1; k++){
                    double mid = (ncpx[k] +ncpx[k+1]) /2.0;
                    P midP(mid, y);
                    int closestid = -1;
                    double dist = INF;
                    for(int l=0; l<m; l++){
                        double ret = distanceGP(island[l], midP);
                        if(ret < d && ret < dist){
                            dist = ret;
                            closestid = l;
                        }
                    }
                    if(closestid != -1){
                        len[closestid][j][i] += ncpx[k+1] -ncpx[k];
                    }
                }
            }
        }

        //シンプソン公式で積分
        vector<double> ans(m, 0);
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                double val = 0;
                for(int k=2; k<splitnum; k+=2){
                    val += 2*len[i][j][k];
                }
                for(int k=1; k<splitnum; k+=2){
                    val += 4*len[i][j][k];
                }
                val += len[i][j][0] +len[i][j][splitnum];
                val *= dy/3.0;
                    
                val *= amount[j];
                ans[i] += val;
            }
        }
        for(int i=0; i<m; i++){
            cout << ans[i] << endl;
        }
    }
    return 0;
}

