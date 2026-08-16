#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt __builtin_popcountll

struct UnionFind{
  vector<int> v;
  UnionFind(int n) : v(n, -1) {}
  void init(){ for(int i = 0;i < (int)v.size();i++)v[i]=-1; }
  int find(int x) { return v[x] < 0 ? x : v[x] = find(v[x]); }
  bool unite(int x, int y) {
    x = find(x); y = find(y);
    if (x == y) return false;
    if (-v[x] < -v[y]) swap(x, y);
    v[x] += v[y]; v[y] = x;
    return true;
  }
  bool root(int x) { return v[x] < 0; }
  bool same(int x, int y) { return find(x) == find(y); }
  int size(int x) { return -v[find(x)]; }
};

typedef long double D;
typedef complex<D> P;

#define X real()
#define Y imag()

D dot(P a,P b){ return (conj(a)*b).X; }

const D eps=1e-9;
const D inf=1e12;
const D PI=acos(-1);
struct L : public vector<P> { // line and segment
  L(const P& a,const P &b){
    push_back(a);
    push_back(b);
  }
};

int N;
int sx,sy,tx,ty;
D R[110];
int sz[110];
D tot[110];
D st[110][21];
vector<P> cents[110];

int main(){
  cin>>N>>sx>>sy>>tx>>ty;
  rep(i,N){
    cin>>R[i];
    cin>>sz[i];
    rep(j,sz[i]){
      int x,y;
      cin>>x>>y;
      cents[i].push_back(P(x,y));
    }
    rep(j,sz[i])tot[i]+=abs(cents[i][j]-cents[i][(j+1)%sz[i]]);

    st[i][0]=0;
    repl(j,1,sz[i]){
      D len=abs(cents[i][j]-cents[i][j-1]);
      st[i][j]=st[i][j-1]+(len/tot[i]);
    }
  }
  sz[N]=1; cents[N].push_back(P(sx,sy));
  sz[N+1]=1; cents[N+1].push_back(P(tx,ty));

  UnionFind uf(N+2);
  rep(i,N+2){
    rep(j,i){
      if(i==N+1&&j==N)continue;
      rep(crti,sz[i]){
        int nxti=(crti+1)%sz[i];
        D ist=st[i][crti],ied=(nxti==0?1.0:st[i][nxti]);
        rep(crtj,sz[j]){
          int nxtj=(crtj+1)%sz[j];
          D jst=st[j][crtj],jed=(nxtj==0?1.0:st[j][nxtj]);

          D l=max(ist,jst),r=min(ied,jed);
          D ub=pow(R[i]+R[j],2);
          if(l>r)continue;

          P inidelta=(cents[i][crti]-(ist/(ied-ist))*(cents[i][nxti]-cents[i][crti]))-(cents[j][crtj]-(jst/(jed-jst))*(cents[j][nxtj]-cents[j][crtj]));
          P vdelta=((cents[i][nxti]-cents[i][crti])/(ied-ist))-((cents[j][nxtj]-cents[j][crtj])/(jed-jst));

          D A=norm(vdelta), B=2.0*dot(inidelta,vdelta), C=norm(inidelta);
          if(abs(A)<eps){
            if(C<=ub)uf.unite(i,j);
            continue;
          }
          if(A*l*l+B*l+C<=ub||A*r*r+B*r+C<=ub)uf.unite(i,j);
          D x=-B/(2.0*A);
          if(l<=x&&x<=r&&A*x*x+B*x+C<=ub)uf.unite(i,j);
        }
      }
    }
  }

  if(uf.same(N,N+1))cout<<"Yes"<<endl;
  else cout<<"No"<<endl;
  return 0;
}

