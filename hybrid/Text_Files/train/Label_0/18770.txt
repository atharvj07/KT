#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-8;
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
    C(const P& p, const double& r): p(p),r(r) {}
    C(){}
};
namespace std{
    bool operator <(const P& a, const P& b){
        return !EQ(a.X,b.X) ? a.X<b.X : a.Y+EPS<b.Y;
    }
    bool operator ==(const P& a, const P& b){
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
    if(cross(b,c) > EPS) return +1;
    if(cross(b,c) < -EPS) return -1;
    if(dot(b,c) < EPS) return +2;
    if(dot(b,b-c) < EPS) return -2;
    return 0;
}
P unit(const P &p){
    return p/abs(p);
}
P rotate(const P &p, double rad){
    return p *P(cos(rad), sin(rad));
}

bool strictItsSS(const L& a, const L& b){
    return ( ccw(a[0],a[1],b[0]) *ccw(a[0],a[1],b[1]) == -1 ) and
        ( ccw(b[0],b[1],a[0]) *ccw(b[0],b[1],a[1]) == -1);
}
bool intersectSP(const L& s, const P &p){
    return abs(cross(s[0]-p, s[1]-p))<EPS and dot(s[0]-p, s[1]-p)<EPS;
}
P projection(const L& l, const P& p) {
    double t = dot(p-l[0], l[0]-l[1]) / norm(l[0]-l[1]);
    return l[0] + t*(l[0]-l[1]);
}
double distanceLP(const L &l, const P &p) {
    return abs(cross(l[1]-l[0], p-l[0])) /abs(l[1]-l[0]);
}
bool isParallel(const P &a, const P &b){
    return abs(cross(a,b)) < EPS;
}
bool isInConvex(const P &p, const VP &poly){
    int n = poly.size();
    for(int i=0; i<n; i++){
        if(cross(poly[(i+1)%n]-poly[i], p-poly[i]) < EPS){
            return false;
        }
    }
    return true;
}

P crosspointLL(const L &l, const L &m) {
    double A = cross(l[1]-l[0], m[1]-m[0]);
    double B = cross(l[1]-l[0], l[1]-m[0]);
    return m[0] + B /A *(m[1]-m[0]);
}
VP crosspointCL(const C &c, const L &l){
    VP res;
    P mid = projection(l, c.p);
    double d = distanceLP(l, c.p);
    if(EQ(d, c.r)){
        res.push_back(mid);
    }else if(d < c.r){
        double len = sqrt(c.r*c.r -d*d);
        res.push_back(mid +len*unit(l[1]-l[0]));
        res.push_back(mid -len*unit(l[1]-l[0]));
    }
    return res;
}
VP crosspointCC(C a, C b){
    VP res;
    if(a.r < b.r) swap(a,b);
    double dist = abs(b.p-a.p);
    P dir = a.r*unit(b.p-a.p);
    if(EQ(dist, a.r+b.r) or EQ(dist, a.r-b.r)){
        res.push_back(a.p +dir);
    }else if(a.r-b.r < dist and dist < a.r+b.r){
        double cos = (a.r*a.r +dist*dist -b.r*b.r)/(2*a.r*dist);
        double sin = sqrt(1 -cos*cos);
        res.push_back(a.p +dir*P(cos, sin));
        res.push_back(a.p +dir*P(cos, -sin));
    }
    return res;
}

struct DA{
    C c;
    P v[2];
    DA(C c, P s, P t): c(c) { v[0]=s; v[1]=t; }
    DA(){}
};
VP crosspointSDA(const L &l, const DA &da){
    VP cp = crosspointCL(da.c, l);
    VP res;
    for(P &p: cp){
        P v = p - da.c.p;
        if(intersectSP(l, p) and cross(v, da.v[0])*cross(v, da.v[1]) < EPS){
            res.push_back(p);
        }
    }
    return res;
}

void input_P(P &in){
    double x,y;
    cin >> x >> y;
    in = P(x, y);
}
VP make_rect(L l, P e, P d){
    return VP{l[0]-e+d, l[0]-e-d, l[1]+e-d, l[1]+e+d};
}
template<class T>
void insertvec(vector<T> &a, const vector<T> &b){
    a.insert(a.end(), b.begin(), b.end());
}

// from here
const double weps =1e-5;
int rot, n;
double l;
P s, g;
VP dir;
vector<L> wall;
vector<vector<VP>> slide_rect;
vector<vector<VP>> nonrotate_rect;
vector<vector<DA>> nonrotate_da;
vector<VP> cand_rot;
vector<vector<vector<pair<int, int>>>> graph;

void input(){
    cin >> l >> rot;
    l += weps;
    input_P(s);
    input_P(g);
    cin >> n;
    wall.resize(n);
    for(int i=0; i<n; i++){
        for(P &p: wall[i]){
            input_P(p);
        }
    }
}

void misc(){
    dir.resize(rot+1);
    for(int i=0; i<rot+1; i++){
        dir[i] = rotate(P(l, 0), PI/rot *i);
    }
}

void make_slide_rect(){
    slide_rect.resize(rot);
    for(int r=0; r<rot; r++){
        for(L &w: wall){
            P vw = w[1] -w[0];
            if(isParallel(vw, dir[r])){
                slide_rect[r].push_back(make_rect(w, l *unit(vw), weps *unit(rotate(vw, PI/2))));
            }else{
                slide_rect[r].push_back(make_rect(w, weps *unit(vw), (cross(vw, dir[r]) > 0)? dir[r]: -dir[r]));
            }   
        }
    }
}

void make_nonrot_area(){
    nonrotate_rect.resize(rot);
    nonrotate_da.resize(rot);
    for(int r=0; r<rot; r++){
        for(int i=0; i<n; i++){
            nonrotate_rect[r].push_back(slide_rect[r][i]);
            nonrotate_rect[r].push_back(slide_rect[(r+1)%rot][i]);
            P vert = rotate(wall[i][1] -wall[i][0], PI/2);
            if(cross(vert, dir[r]) * cross(vert, dir[r+1]) < -EPS){
                nonrotate_rect[r].push_back(make_rect(wall[i], P(0, 0), l*unit(vert)));
            }
            nonrotate_da[r].emplace_back(C(wall[i][0], l), dir[r], dir[r+1]);
            nonrotate_da[r].emplace_back(C(wall[i][1], l), dir[r], dir[r+1]);
        }
    }
}

void enum_rotate_candidate(){
    cand_rot.resize(rot);
    for(int r=0; r<rot; r++){
        vector<L> w;
        for(VP v: nonrotate_rect[r]){
            int n = v.size();
            for(int i=0; i<n; i++){
                w.emplace_back(v[i], v[(i+1)%n]);
            }
        }
        auto &arc = nonrotate_da[r];
        auto &cand = cand_rot[r];
        int n = w.size();
        int m = arc.size();
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(strictItsSS(w[i], w[j])){
                    cand.push_back(crosspointLL(w[i], w[j]));
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                insertvec(cand, crosspointSDA(w[i], arc[j]));
            }
        }
        for(int i=0; i<m; i++){
            for(int j=i+1; j<m; j++){
                insertvec(cand, crosspointCC(arc[i].c, arc[j].c));
            }
        }
        sort(cand.begin(), cand.end());
        cand.erase(unique(cand.begin(), cand.end()), cand.end());
    } 
}

void eliminate_nonrot_point(){
    vector<VP> res(rot);
    for(int r=0; r<rot; r++){
        auto &cand = cand_rot[r];
        for(P p: cand){
            bool enable = true;
            for(VP &rect: nonrotate_rect[r]){
                if(isInConvex(p, rect)){
                    enable = false;
                }
            }
            for(DA &da: nonrotate_da[r]){
                if((abs(p -da.c.p) +EPS < l) and (cross(p -da.c.p, da.v[0]) * cross(p -da.c.p, da.v[1]) < EPS)){
                    enable = false;
                }
            }
            if(enable){
                res[r].push_back(p);
            }
        }
    }
    cand_rot = res;
}

bool cansee(P s, P g, const vector<VP> &rects){
    P mid = (s + g) /2.0;
    for(VP rect: rects){
        if(isInConvex(mid, rect)) return false;
        for(int i=0; i<4; i++){
            if(strictItsSS(L(rect[i], rect[(i+1)%4]), L(s, g))){
                return false;
            }
        }
    }
    return true;
}

void make_visible_graph(){
    graph = vector<vector<vector<pair<int, int>>>>(rot);
    vector<VP> vlist(rot, VP{s,g});
    for(int r=0; r<rot; r++){
        auto &v = vlist[r];
        for(VP rect: slide_rect[r]){
            insertvec(v, rect);
        }
        insertvec(v, cand_rot[r]);
        insertvec(v, cand_rot[(r-1+rot)%rot]);
    }
    for(int r=0; r<rot; r++){
        auto &v = vlist[r];
        graph[r].resize(v.size());
        for(size_t i=0; i<v.size(); i++){
            for(size_t j=i+1; j<v.size(); j++){
                if(cansee(v[i], v[j], slide_rect[r])){
                    graph[r][i].emplace_back(r, j);
                    graph[r][j].emplace_back(r, i);
                }
            }
        }
        for(size_t i=0; i<cand_rot[r].size(); i++){
            graph[r][i +4*n +2].emplace_back((r+1)%rot, i +4*n +2 +cand_rot[(r+1)%rot].size());
        }
    }
}

int shortest_path(){
    const int inf = 1e9;
    using pii = pair<int, int>;
    deque<pii> wait;
    vector<vector<int>> mincost(rot, vector<int>(10000, inf));
    mincost[0][0] = 0;
    wait.push_front(pii(0, 0));
    while(!wait.empty()){
        pii curr = wait.front();
        wait.pop_front();
        int cr=curr.first, ci=curr.second;
        if(ci == 1) return mincost[cr][ci];
        for(auto next: graph[cr][ci]){
            int nr=next.first, ni=next.second;
            int cost = (cr==nr)? 0: 1;
            if(mincost[cr][ci] + cost < mincost[nr][ni]){
                mincost[nr][ni] = mincost[cr][ci] + cost;
                if(cost == 0) wait.push_front(pii(nr, ni));
                else wait.push_back(pii(nr, ni));
            }
        }
    }
    return -1;
}

int main(){
    input();
    misc();
    make_slide_rect();
    make_nonrot_area();
    enum_rotate_candidate();
    eliminate_nonrot_point();
    make_visible_graph();
    cout << shortest_path() << endl;
    return 0;
}

