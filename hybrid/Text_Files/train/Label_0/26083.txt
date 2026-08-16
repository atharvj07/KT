#include <cassert>// c
#include <ctime>
#include <iostream>// io
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>// container
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <algorithm>// other
#include <complex>
#include <numeric>
#include <functional>
#include <random>
#include <regex>

using namespace std;
typedef long long ll;

#define ALL(c) (c).begin(),(c).end()
#define FOR(i,l,r) for(int i=(int)l;i<(int)r;++i)
#define REP(i,n) FOR(i,0,n)
#define FORr(i,l,r) for(int i=(int)r-1;i>=(int)l;--i)
#define REPr(i,n) FORr(i,0,n)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define IN(l,v,r) ((l)<=(v) && (v)<(r))
#define UNIQUE(v) v.erase(unique(ALL(v)),v.end())
//debug
#define DUMP(x)  cerr << #x << " = " << (x)
#define LINE()    cerr<< " (L" << __LINE__ << ")"

template<typename T,typename U> T pmod(T x,U M){return (x%M+M)%M;}

stringstream ss;

// must template
typedef long double D;
const D INF = 1e12,EPS = 1e-8;

typedef complex<D> P;
#define X real()
#define Y imag()
istream& operator >> (istream& is,complex<D>& p){
    D x,y;is >> x >> y;p=P(x,y);return is;
}

int sig(D a,D b=0){return a<b-EPS?-1:a>b+EPS?1:0;}
template<typename T> bool eq(const T& a,const T& b){return sig(abs(a-b))==0;}
bool compX (const P& a,const P& b){return !eq(a.X,b.X)?sig(a.X,b.X)<0:sig(a.Y,b.Y)<0;}
namespace std{
    bool operator <  (const P& a,const P& b){return compX(a,b);}
    bool operator == (const P& a,const P& b){return eq(a,b);}
};
// a×b
D cross(const P& a,const P& b){return imag(conj(a)*b);}
// a・b
D dot(const P& a,const P& b) {return real(conj(a)*b);}
int ccw(const P& a,P b,P c){
    b -= a; c -= a;
    if (cross(b,c) > EPS)   return +1;       // counter clockwise
    if (cross(b,c) < -EPS)   return -1;       // clockwise
    if (dot(b,c) < 0)     return +2;       // c--a--b on line
    if (norm(b) < norm(c)) return -2;       // a--b--c on line
    return 0; //a--c--b on line (c==b,c==a)
}
// //must template
//直線・線分
struct L : public vector<P> {
    P vec() const {return this->at(1)-this->at(0);}
    L(const P &a, const P &b){push_back(a); push_back(b);}
    L(){push_back(P());push_back(P());}
};
istream& operator >> (istream& is,L& l){P s,t;is >> s >> t;l=L(s,t);return is;}

bool isIntersectLL(const L &l, const L &m) {
    return sig(cross(l.vec(), m.vec()))!=0 || // non-parallel
    sig(cross(l.vec(), m[0]-l[0])) ==0;   // same line
}
bool isIntersectLS(const L &l, const L &s) {
    return sig(cross(l.vec(), s[0]-l[0])*       // s[0] is left of l
        cross(l.vec(), s[1]-l[0]))<=0; // s[1] is right of l
}
bool isIintersectLP(const L &l, const P &p) {return sig(cross(l[1]-p, l[0]-p))==0;}

// verified by ACAC003 B
// http://judge.u-aizu.ac.jp/onlinejudge/creview.jsp?rid=899178&cid=ACAC003
bool isIntersectSS(const L &s, const L &t) {
    return ccw(s[0],s[1],t[0])*ccw(s[0],s[1],t[1]) <= 0 &&
        ccw(t[0],t[1],s[0])*ccw(t[0],t[1],s[1]) <= 0;
}
bool isIntersectSP(const L &s, const P &p) {
    return sig(abs(s[0]-p)+abs(s[1]-p),abs(s[1]-s[0])) <=0; // triangle inequality
}

// 交点計算
// verified by AOJLIB
// http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1092231
P crosspoint(const L &l, const L &m) {
    D A = cross(l.vec(), m.vec());
    D B = cross(l.vec(), l[1] - m[0]);
    if (sig(A)==0 && sig(B)==0) return m[0]; // same line
    if (sig(A)==0) assert(false); //交点を持たない．
    return m[0] + B / A * (m[1] - m[0]);
}

typedef D Cost; Cost CINF=1e20;
struct Edge{
    int f,t;Cost c;D th;
    Edge(int f,int t,Cost c,D th) : f(f),t(t),c(c),th(th){
    };
    bool operator<(const Edge& r) const{return th<r.th;}
};
typedef vector<vector<Edge> >  Graph;

Graph segmentArrangement(vector<L> ss, vector<P> &ps) {
    vector<vector<D>> vs(ss.size());
    REP(i,ss.size()){vs[i].push_back(0);vs[i].push_back(abs(ss[i][1]-ss[i][0]));}
    REP(i,ss.size())REP(j,ps.size())if(isIntersectSP(ss[i], ps[j]))
        vs[i].push_back(abs(ps[j]-ss[i][0]));
    
    REP(i,ss.size())FOR(j,i+1,ss.size()){
        L& a=ss[i],b=ss[j];
        if(isIntersectSS(a,b)){
            P p = crosspoint(a,b);
            vs[i].push_back(abs(p-a[0]));vs[j].push_back(abs(p-b[0]));              
        }
    }
    REP(i,vs.size()){sort(ALL(vs[i]));vs[i].erase(unique(ALL(vs[i]),eq<D>),vs[i].end());}
    REP(i,vs.size())REP(j,vs[i].size())ps.push_back(ss[i][0]+vs[i][j]*ss[i].vec()/abs(ss[i].vec()));
    sort(ALL(ps));UNIQUE(ps);

    Graph g(ps.size());
    REP(i,vs.size()){
        vector<D>& cut=vs[i];
        REP(j,cut.size()-1){
            P a = ss[i][0] + vs[i][j]*ss[i].vec()/abs(ss[i].vec()),b = ss[i][0] + vs[i][j+1]*ss[i].vec()/abs(ss[i].vec());
            int f=distance(ps.begin(),lower_bound(ALL(ps),a)), t=distance(ps.begin(),lower_bound(ALL(ps),b));
            g[f].emplace_back(f,t,abs(b-a),arg(b-a));
            g[t].emplace_back(t,f,abs(a-b),arg(a-b));
        }
    }
    return g;
}

typedef vector<P> Poly,ConvexPoly;

enum { OUT, ON, IN };
int contains(const Poly& ps, const P& p) {
    bool in = false;int n=ps.size();
    REP(i,n){
        P a = ps[i] - p, b = ps[pmod(i+1,n)] - p;
        if (a.Y > b.Y) swap(a, b);
        if (a.Y <= 0 && 0 < b.Y)
        if (cross(a, b) < 0) in = !in;
            if (cross(a, b) == 0 && dot(a, b) <= 0) return ON;
    }
    return in ? IN : OUT;
}

vector<Poly> find_polys(const vector<P>& ps,Graph& g){
    const int n=g.size();
    vector<vector<bool>> used(n);
    REP(i,n)used[i]=vector<bool>(g[i].size());
    
    REP(i,n)sort(ALL(g[i]));

    vector<Poly> res;
    REP(i,n)REP(j,g[i].size()){
        int v=i,e_idx=j;
        Poly qs;
        while(true){
            if(used[v][e_idx])break;
            used[v][e_idx] =true;
            Edge& e=g[v][e_idx];
            qs.push_back(ps[v]);
            REP(k,g[e.t].size())if(g[e.t][k].t==v){
                e_idx =(k+1)%g[e.t].size();
                v=e.t;
                break;
            }
        }
        if(qs.size()>=3)res.push_back(move(qs));
    }

    // cerr << res.size() <<endl;

    //remove ccw poly
    int idx = 0;
    while(idx < res.size()) {
        const P diff = res[idx][1] - res[idx][0];
        const P p = res[idx][0] + diff * 0.5L + diff * P(0,-1) * (2.0L * EPS /abs(diff));
        if(contains(res[idx], p))++idx;
        else res.erase(res.begin() + idx);
    }
    return res;
}

struct UnionFind{
    vector<int> par,rank,ss;int size;
    UnionFind(int n){
        REP(i,n) par.push_back(i);
        rank = vector<int>(n);ss=vector<int>(n,1);size=n;
    }
    int root(int x){
        if(par[x] == x)return x;
        return par[x] = root(par[x]);
    }
    bool same(int x,int y){
        return root(x) == root(y);
    }
    void unite(int x,int y){
        x = root(x);y = root(y);
        if(x==y)return;
        if(rank[x] < rank[y]){
            par[x] = y;ss[y]+=ss[x];
        }else{
            par[y] = x;ss[x]+=ss[y];
        }
        if(rank[x] == rank[y]) rank[x]++;
        size--;
    }
    int getS(int x){
        return ss[root(x)];
    }
};

int main(){
    cin.tie(0); ios::sync_with_stdio(false);
    ss   <<fixed <<setprecision(20);
    cout <<fixed <<setprecision(20);
    cerr <<fixed <<setprecision(20);

    int N;cin >>N;
    vector<L> ls(N);REP(i,N) cin >> ls[i];
    vector<P> ps;
    Graph g=segmentArrangement(ls,ps);
    vector<Poly>  face=find_polys(ps,g);
    // cerr << ps.size() <<endl;
    // cerr << face.size() <<endl;
    UnionFind uf(face.size());
    REP(i,face.size()){
        // cerr << i <<endl;
        // REP(l,face[i].size())cerr << face[i][l] << endl;
       
        REP(j,face.size())if(i!=j){
            bool isin=true;
            REP(k,face[j].size())
                if(contains(face[i],face[j][k])!=IN)isin=false;
            
            bool iscross=false;
            REP(k,face[j].size())REP(l,face[i].size()){
                L l1(face[j][k],face[j][pmod(k+1,face[j].size())]);
                L l2(face[i][l],face[i][pmod(l+1,face[i].size())]);

                if(isIntersectSS(l1,l2) && sig(cross(l1.vec(),l2.vec()))==0
                    && max(l1[0],l1[1])!= min(l2[0],l2[1])
                    && max(l2[0],l2[1])!= min(l1[0],l1[1])){
                    // cerr <<"!!"<<endl;
                    // cerr << l1[0]<<" " << l1[1] <<endl;
                    // cerr << l2[0]<<" " << l2[1] <<endl;
                    iscross=true;
                }
            }
            // cerr << i <<" " << j <<endl;
            // cerr << isin <<" " << iscross <<endl;
            if(isin || iscross)uf.unite(i,j);
        }
    }
    cout << uf.size <<endl;

    return 0;
 }