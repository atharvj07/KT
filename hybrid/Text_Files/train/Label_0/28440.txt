#include<bits/stdc++.h>
#define MAX 1000
#define inf 1<<29
#define linf 1e16
#define eps (1e-8)
#define mod 1000000007
#define pi acos(-1)
#define phi (1.0+sqrt(5))/2.0
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) (a).begin(),(a).end()
#define pd(a) printf("%.10f\n",(double)(a))
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define RFOR(i,a,b) for(int i=(a)-1;(b)<=i;i--)
#define equals(a,b) (fabs((a)-(b))<eps)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<int,double> pid;
typedef pair<double,int> pdi;
typedef vector<int> vi;
typedef vector<pii> vpi;
const int dx[8]={1,0,-1,0,1,1,-1,-1};
const int dy[8]={0,1,0,-1,1,-1,1,-1};

class Point{
public:
  double x,y;
  Point(double x=0,double y=0):x(x),y(y){}

  Point operator+(Point p){ return Point(x+p.x,y+p.y);}
  Point operator-(Point p){ return Point(x-p.x,y-p.y);}
  Point operator*(double k){ return Point(x*k,y*k);}
  Point operator/(double k){ return Point(x/k,y/k);}
  bool operator<(Point p)const{ return x!=p.x ? x<p.x : y<p.y; }
  bool operator==(Point p)const{ return equals(x,p.x) && equals(y,p.y);}

  double abs(){ return sqrt(norm());}
  double norm(){ return (x*x+y*y);}
};
typedef Point Vector;
typedef vector<Point> Polygon;

class Segment{
public:
  Point p1,p2;
  Segment(Point p1=Point(),Point p2=Point()):p1(p1),p2(p2){}
};
typedef Segment Line;

double norm(Vector a){ return (a.x*a.x+a.y*a.y);}
double abs(Vector a){ return sqrt(norm(a));}
double dot(Vector a,Vector b){ return (a.x*b.x+a.y*b.y);}
double cross(Vector a,Vector b){ return (a.x*b.y-a.y*b.x);}

int ccw(Point p0,Point p1,Point p2){
  Vector a=p1-p0;
  Vector b=p2-p0;
  if(cross(a,b)>eps)return 1;
  if(cross(a,b)<-eps)return -1;
  if(dot(a,b)<-eps)return 2;
  if(a.norm()<b.norm())return -2;
  return 0;
}

bool intersect(Point p1,Point p2,Point p3,Point p4){
  return (ccw(p1,p2,p3)*ccw(p1,p2,p4)<=0 &&
          ccw(p3,p4,p1)*ccw(p3,p4,p2)<=0);
}

bool intersect(Segment s1,Segment s2){
  return intersect(s1.p1,s1.p2,s2.p1,s2.p2);
}

bool intersectLS(Line L,Segment s){
  return cross(L.p2-L.p1,s.p1-L.p1)*cross(L.p2-L.p1,s.p2-L.p1)<-eps;
}

Point getCrossPointLL(Line a,Line b){
  double A=cross(a.p2-a.p1,b.p2-b.p1);
  double B=cross(a.p2-a.p1,a.p2-b.p1);
  if(abs(A)<eps || abs(B)<eps)return b.p1;
  return b.p1+(b.p2-b.p1)*(B/A);
}

double getPolygonArea(Polygon p){
  double area=0.0;
  int n=p.size();
  for(int i=0;i<n;i++)area+=cross(p[i%n],p[(i+1)%n]);
  return area/2;
}

int contains(Polygon g,Point p){
  int n=g.size();
  bool x=false;
  for(int i=0;i<n;i++){
    Vector a=g[i]-p,b=g[(i+1)%n]-p;
    if(abs(cross(a,b))<eps && dot(a,b)<eps)return 1;
    if(a.y>b.y)swap(a,b);
    if(a.y<eps && eps<b.y && cross(a,b)>eps)x=!x;
  }
  if(x)return 2;
  return 0;
}

bool contains(Polygon a,Polygon b){
  Point m;
  FOR(i,0,b.size())m=m+b[i];
  m=m/b.size();
  if(contains(a,m)==0)return false;
  return true;
}

Polygon convex_cut(Polygon p,Line l){
  Polygon ans;
  for(int i=0;i<p.size();i++){
    Point A=p[i],B=p[(i+1)%p.size()];
    if(ccw(l.p1,l.p2,A)!=-1)ans.push_back(A);
    if(intersectLS(l,Segment(A,B)))
      ans.push_back(getCrossPointLL(l,Segment(A,B)));
  }
  return ans;
}

vector<Polygon> cut(Polygon p,Line L){
  vector<Polygon> res;
  Polygon a=convex_cut(p,L);
  Polygon b=convex_cut(p,Line(L.p2,L.p1));
  if(2<a.size() && eps<getPolygonArea(a))res.pb(a);
  if(2<b.size() && eps<getPolygonArea(b))res.pb(b);
  return res;
}

typedef vector<vector<int> > Graph;

Graph SegmentArrangement(vector<Segment> v,vector<Point> &ps){
  for(int i=0;i<v.size();i++){
    ps.push_back(v[i].p1);
    ps.push_back(v[i].p2);
  }
  sort(ps.begin(),ps.end());
//  ps.erase(unique(ps.begin(),ps.end()),ps.end());
  Graph g(ps.size());
  for(int i=0;i<v.size();i++){
    vector<pair<double,int> > list;
    for(int j=0;j<ps.size();j++)
      if(ccw(v[i].p1,v[i].p2,ps[j])==0)
        list.push_back(mp(norm(v[i].p1-ps[j]),j));
    sort(list.begin(),list.end());
    for(int j=0;j<list.size()-1;j++){
      int a=list[j].s,b=list[j+1].s;
      g[a].push_back(b);
    }
  }
  return g;
}

vector<Point> getTriangle(Point a,Point b,Point c){
  vector<Point> t(3);
  t[0]=a;t[1]=b;t[2]=c;
  return t;
}

bool ok(int a,int b,int c,Polygon p){
  if(ccw(p[a],p[b],p[c])<0)return false;
  Polygon t=getTriangle(p[a],p[b],p[c]);
  for(int i=0;i<p.size();i++){
    if(i==a || i==b || i==c)continue;
    if(contains(t,p[i])!=0)return false;
  }
  return true;
}

vector<Polygon> triangulate(Polygon p){
  int n=p.size(),i=0;
  vector<Polygon> res;
  vector<int> L,R;
  for(int i=0;i<n;i++){
    L.push_back((i-1+n)%n);
    R.push_back((i+1+n)%n);
  }
  while(res.size()<n-2){
    i=R[i];
    if(ok(L[i],i,R[i],p)){
      res.push_back(getTriangle(p[L[i]],p[i],p[R[i]]));
      L[R[i]]=L[i];
      R[L[i]]=R[i];
    }
  }
  return res;
}

bool same(Polygon a,Polygon b){
  if(!(equals(getPolygonArea(a),getPolygonArea(b))))return false;
  if(a.size()!=b.size())return false;
  sort(all(a));
  sort(all(b));
  FOR(i,0,a.size())if(!(a[i]==b[i]))return false;
  return true;
}

bool same(Segment a,Segment b){
  if(a.p1==b.p1 && a.p2==b.p2)return true;
  if(a.p1==b.p2 && a.p2==b.p1)return true;
  return false;
}

void Print(Polygon p){
  cout<<endl;
  FOR(i,0,p.size())cout<<p[i].x<<" "<<p[i].y<<endl;
}

vector<Polygon> unique(vector<Polygon> vp){
  vector<Polygon> res;
  FOR(i,0,vp.size()){
    bool flag=true;
    FOR(j,i+1,vp.size()){
      if(same(vp[i],vp[j]))flag=false;
    }
    if(flag)res.pb(vp[i]);
  }
  return res;
}

vector<Segment> unique(vector<Segment> v){
  vector<Segment> res;
  FOR(i,0,v.size()){
    bool flag=true;
    FOR(j,i+1,v.size())
      if(v[i].p1==v[j].p1 && v[i].p2==v[j].p2)flag=false;
    if(flag)res.pb(v[i]);
  }
  return res;
}

int n;
vector<Polygon> P;
vector<Polygon> ev;
int deg[MAX]={};
bool isout[MAX]={};
vector<pii> g[MAX];
vector<Segment> vvs;
vector<Point> vp;
bool used[MAX]={};
Graph e;
vector<Segment> vs;
vector<vector<Polygon> > t;

Polygon rec(int index){
  Polygon res;
  if(used[index])return res;
  used[index]=true;
//  cout<<e[index].size()<<endl;
  if(e[index].size()==0)return res;
  res = rec(e[index][0]);
  res.pb(vp[index]);
  return res;
}

vector<Polygon> makePolygon(){
  vector<Polygon> res;
  e=SegmentArrangement(vvs,vp);
  FOR(i,0,vp.size()){
    if(used[i])continue;
    Polygon p=rec(i);
    if(getPolygonArea(p)>eps)res.pb(p);
  }
  return res;
}

void add_edge(int from,int to,int cost){
  g[from].pb(mp(to,cost));
  g[to].pb(mp(from,cost));
}

bool check(Segment s){
  Point m=s.p1+(s.p2-s.p1)/2.0;
  int c=0;
  FOR(i,0,ev.size())c+=contains(ev[i],m);
  return c==1;
}

bool check(Polygon p){
  FOR(i,0,p.size()){
    Segment s(p[i],p[(i+1)%p.size()]);
    if(check(s))return true;
  }
  return false;
}

bool check(Polygon a,Polygon b){
  FOR(i,0,a.size()){
    Segment s1(a[i],a[(i+1)%a.size()]);
    FOR(j,0,b.size()){
      Segment s2(b[j],b[(j+1)%b.size()]);
      if(same(s1,s2))return true;
    }
  }
  return false;
}

void make(){
  FOR(i,0,n)t.pb(triangulate(P[i]));
  FOR(i,0,t.size()){
    FOR(j,0,t[i].size()){
      Polygon p=t[i][j];
      FOR(k,0,p.size())vs.pb(Segment(p[k],p[(k+1)%p.size()]));
    }
  }
  FOR(i,0,t.size()){
    queue<Polygon> cand;
    FOR(j,0,t[i].size())cand.push(t[i][j]);
    FOR(j,0,vs.size()){
      queue<Polygon> tmp;
      while(cand.size()){
        Polygon p=cand.front();
        cand.pop();
        vector<Polygon> pp=cut(p,vs[j]);
        FOR(l,0,pp.size())tmp.push(pp[l]);
      }
      while(tmp.size()){ 
        cand.push(tmp.front());
        tmp.pop();
      }
    }
    while(!cand.empty()){
      ev.pb(cand.front());
      cand.pop();
    }
  }
  ev=unique(ev);
  FOR(i,0,ev.size()){
    Polygon p=ev[i];
    FOR(j,0,p.size()){
      Segment s(p[j],p[(j+1)%p.size()]);
      if(check(s))vvs.pb(s);
    }
  }
  FOR(i,0,vvs.size()){
    FOR(j,0,vvs.size()){
      if(i==j)continue;
      if(same(vvs[i],vvs[j])){
       cout<<vvs[i].p1.x<<" "<<vvs[i].p1.y<<" ";
       cout<<vvs[i].p2.x<<" "<<vvs[i].p2.y<<endl;
      }
    }
  }
//  vvs = unique(vvs);
  vector<Polygon> res=makePolygon();
  FOR(i,0,res.size())ev.pb(res[i]);
  FOR(i,0,ev.size()){
    bool flag=true;
    Polygon p=ev[i];
    FOR(j,0,n)if(contains(P[j],p))deg[i]++;
    if(check(ev[i]))isout[i]=true;
  }
  FOR(i,0,ev.size()){
    FOR(j,0,ev.size()){
      if(check(ev[i],ev[j]))add_edge(i,j,abs(deg[i]-deg[j]));
      else if(isout[i] && isout[j])add_edge(i,j,deg[i]+deg[j]);
    }
  }
}

int dijkstra(Point a,Point b){
  vector<int> s;
  set<int> t;
  FOR(i,0,ev.size()){
    if(contains(ev[i],a))s.pb(i);
    if(contains(ev[i],b))t.insert(i);
  }
  if(s.empty() && t.empty())return 0;
  if(s.empty()){
    s.pb(ev.size());
    FOR(i,0,ev.size())if(isout[i])add_edge(i,ev.size(),deg[i]);
  }
  if(t.empty()){
    t.insert(ev.size()+1);
    FOR(i,0,ev.size())if(isout[i])add_edge(i,ev.size()+1,deg[i]);
  }
  int d[MAX];
  fill(d,d+MAX,inf);
  priority_queue<pii,vector<pii>,greater<pii> > pq;
  FOR(i,0,s.size()){
    pq.push(mp(0,s[i]));
    d[s[i]]=0;
  }
  while(pq.size()){
    pii u=pq.top();
    pq.pop();

    if(d[u.s]<u.f)continue;
    if(t.find(u.s)!=t.end())return u.f;

    FOR(i,0,g[u.s].size()){
      int next=g[u.s][i].f;
      int cost=d[u.s]+g[u.s][i].s;
      if(cost<d[next]){
        d[next]=cost;
        pq.push(mp(cost,next));
      }
    }
  }
  return -1;
}
  
int main()
{
  int m,x,y,a,b,c,d;
  cin>>n;
  FOR(i,0,n){
    cin>>m;
    Polygon p;
    FOR(j,0,m){
      cin>>x>>y;
      p.pb(Point(x,y));
    }
    if(getPolygonArea(p)<eps)reverse(all(p));
    P.pb(p);
  }
  make();
  cin>>m;
  FOR(i,0,m){
    cin>>a>>b>>c>>d;
    cout<<dijkstra(Point(a,b),Point(c,d))<<endl;
  }
  return 0;
}