#include <iostream>
#include <iomanip>
#include <complex>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
#include <utility>
#include <map>
using namespace std;
const double EPS = 1e-6;
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

bool intersectSS(const L& a, const L& b){
    return ( ccw(a[0],a[1],b[0]) *ccw(a[0],a[1],b[1]) <= 0 ) &&
        ( ccw(b[0],b[1],a[0]) *ccw(b[0],b[1],a[1]) <= 0 );
}
bool intersectSP(const L& s, const P &p){
    return abs(cross(s[0]-p, s[1]-p))<EPS  && dot(s[0]-p, s[1]-p)<EPS;
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

VP convex(VP v){
    VP ret;
    int n = v.size();
    sort(v.begin(), v.end());
    for(int i=0; i<n; i++){
        while((int)ret.size()>1 && cross(ret.back()-ret[ret.size()-2], v[i]-ret.back()) < EPS){
            ret.pop_back();
        }
        ret.push_back(v[i]);
    }
    int t = ret.size();
    for(int i=n-2; i>=0; i--){
        while((int)ret.size()>t && cross(ret.back()-ret[ret.size()-2], v[i]-ret.back()) < EPS){
            ret.pop_back();
        }
        ret.push_back(v[i]);
    }
    if((int)ret.size() > 1) ret.pop_back();
    return ret;
}

pair<vector<vector<double> >, VP> arrangementEX(const vector<L> &l, const VP &p){
    vector<VP> cp(l.size());
    VP plist = p;
    for(int i=0; i<(int)l.size(); i++){
        for(int j=i+1; j<(int)l.size(); j++){
            if(!isParallel(l[i], l[j]) && intersectSS(l[i], l[j])){
                P cpij = crosspointLL(l[i], l[j]);
                cp[i].push_back(cpij);
                cp[j].push_back(cpij);
                plist.push_back(cpij);
            }
        }
        for(int j=0; j<(int)p.size(); j++){
            if(intersectSP(l[i], p[j])){
                cp[i].push_back(p[j]);
            }
        }
        cp[i].push_back(l[i][0]);
        cp[i].push_back(l[i][1]);
        plist.push_back(l[i][0]);
        plist.push_back(l[i][1]);
        sort(cp[i].begin(), cp[i].end());
        cp[i].erase(unique(cp[i].begin(), cp[i].end()), cp[i].end());
    }
    sort(plist.begin(), plist.end());
    plist.erase(unique(plist.begin(), plist.end()), plist.end());

    int n = plist.size();
    map<P, int> conv;
    for(int i=0; i<n; i++){
        conv[plist[i]] = i;
    }
    vector<vector<double> > adj(n, vector<double>(n, INF));
    for(int i=0; i<(int)cp.size(); i++){
        for(int j=0; j<(int)cp[i].size()-1; j++){
            int jidx = conv[cp[i][j]];
            int jp1idx = conv[cp[i][j+1]];
            adj[jidx][jp1idx] = adj[jp1idx][jidx] = 0;
        }
    }
    return make_pair(adj, plist);
}

int main(){
    while(1){
        //input
        int n,m;
        cin >> n >> m;
        if(n == 0) break;

        vector<VP> poly(n);
        vector<double> h(n);
        for(int i=0; i<n; i++){
            int nv;
            cin >> nv >> h[i];
            poly[i].resize(nv);
            for(int j=0; j<nv; j++){
                int x,y;
                cin >> x >> y;
                poly[i][j] = P(x, y);
            }
        }
        vector<L> lines(m);
        for(int i=0; i<m; i++){
            int xs,ys,xt,yt;
            cin >> xs >> ys >> xt >> yt;
            lines[i] = L(P(xs, ys), P(xt, yt));
        }

        double th,phi;
        cin >> th >> phi;
        th *= PI/180; phi *= PI/180;
        P dir = P(cos(th+PI), sin(th+PI)) /tan(phi);
        for(int i=0; i<n; i++){
            VP tmp = poly[i];
            P idir = dir *h[i];
            for(int j=0; j<(int)poly[i].size(); j++){
                tmp.push_back(poly[i][j] +idir);
            }
            poly[i] = convex(tmp);
        }

        VP sg(2);
        int sx,sy,tx,ty;
        cin >> sx >> sy >> tx >> ty;
        sg[0] = P(sx, sy);
        sg[1] = P(tx, ty);

        //calc costs of edges
        auto ret = arrangementEX(lines, sg);
        auto &adj = ret.first;
        VP &plist = ret.second;
        int pn = plist.size();
        int sidx = lower_bound(plist.begin(), plist.end(), sg[0]) -plist.begin();
        int gidx = lower_bound(plist.begin(), plist.end(), sg[1]) -plist.begin();
        for(int i=0; i<pn; i++){
            for(int j=i+1;j<pn; j++){
                if(adj[i][j] == INF) continue;
                L e(plist[i], plist[j]);
                VP cp(2);
                cp[0] = e[0];
                cp[1] = e[1];
                for(int k=0; k<n; k++){
                    int vn = poly[k].size();
                    for(int l=0; l<vn; l++){
                        L edge(poly[k][l], poly[k][(l+1)%vn]);
                        if(!isParallel(e, edge) && intersectSS(e, edge)){
                            cp.push_back(crosspointLL(e, edge));
                        }
                    }
                }
                sort(cp.begin(), cp.end());
                cp.erase(unique(cp.begin(), cp.end()), cp.end());
                double cost = 0;
                for(int k=0; k<(int)cp.size()-1; k++){
                    P mid = (cp[k] +cp[k+1]) /2.0;
                    bool in = false;
                    for(int l=0; l<n; l++){
                        if(in_poly(mid, poly[l]) >= 0){
                            in = true;
                            break;
                        }
                    }
                    if(!in){
                        cost += abs(cp[k+1] -cp[k]);
                    }
                }
                adj[i][j] = adj[j][i] = cost;
            }
        }

        for(int k=0; k<pn; k++){
            for(int i=0; i<pn; i++){
                for(int j=0; j<pn; j++){
                    adj[i][j] = min(adj[i][j], adj[i][k] +adj[k][j]);
                }
            }
        }
        cout << fixed << setprecision(4);
        cout << adj[sidx][gidx] << endl;
    }
    return 0;
}

