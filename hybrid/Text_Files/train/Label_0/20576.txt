#include<bits/stdc++.h>
#define MAX 2500
#define inf 1<<29
#define linf 1e18
#define eps (1e-8)
#define mod 1000000007
#define pi M_PI
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
typedef pair<double,int> pdi;
typedef pair<int,double> pid;
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
  bool operator<(Point p)const{ return (x!=p.x ? x<p.x : y<p.y);}
  bool operator==(Point p)const{ return fabs(x-p.x)<eps && fabs(y-p.y)<eps;}

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

bool isParallel(Vector a,Vector b){
  return equals(cross(a,b),0.0);
}

bool isParallel(Segment s,Segment t){
  return equals(cross(s.p1-s.p2,t.p1-t.p2),0.0);
}

int ccw(Point p0,Point p1,Point p2){
  Vector a=p1-p0;
  Vector b=p2-p0;
  if(cross(a,b)>eps)return 1;
  if(cross(a,b)<-eps)return -1;
  if(dot(a,b)<-eps)return 2;
  if(a.norm()<b.norm())return -2;
  return 0;
}

Point getCrossPointLL(Line a,Line b){
  double A=cross(a.p2-a.p1,b.p2-b.p1);
  double B=cross(a.p2-a.p1,a.p2-b.p1);
  if(abs(A)<eps || abs(B)<eps)return b.p1;
  return b.p1+(b.p2-b.p1)*(B/A);
}

vector<Point> unique(vector<Point> vp){
  sort(vp.begin(),vp.end());
  vector<Point> res;
  res.push_back(vp[0]);
  for(int i=1;i<vp.size();i++){
    if(!(vp[i]==res.back()))res.push_back(vp[i]);
  }
  return res;
}

class State{
  public:
    int index,bit,num;
    double dis;
    State(int index,int bit,int num,double dis):
      index(index),bit(bit),num(num),dis(dis){}
    bool operator<(State s)const{
      return s.num!=num ? s.num<num : s.dis-dis<-eps; 
     }
};

int n;
vector<Point> vp,sp;
vector<pii> e[MAX];
pid d[MAX][1<<10];

void init(){
  vp.clear();
  sp.clear();
  FOR(i,0,MAX){
    e[i].clear();
    FOR(j,0,1<<10)d[i][j]=mp(inf,inf);
  }
}

bool comp(pid a,pid b){
  return a.f!=b.f ? a.f<b.f : a.s-b.s<-eps;
}

pid dijkstra(){
  priority_queue<State> pq;
  FOR(i,0,MAX)FOR(j,0,1<<n)d[i][j]=mp(inf,inf);
  FOR(i,0,sp.size()){
    d[i][0]=mp(0,0);
    pq.push(State(i,0,0,0));
  }

  while(pq.size()){
    State u=pq.top();
    pq.pop();
    if(u.bit==((1<<n)-1))return mp(u.num,u.dis);
    if(comp(d[u.index][u.bit],mp(u.num,u.dis)))continue; 

    FOR(i,0,e[u.index].size()){
      if(i==u.index)continue;
      pii next=e[u.index][i];
      int nbit=(u.bit|next.s);
      double cost=abs(sp[u.index]-sp[next.f]);
      if(comp(mp(d[u.index][u.bit].f+1,d[u.index][u.bit].s+cost),
           d[next.f][nbit])){
        d[next.f][nbit]=mp(d[u.index][u.bit].f+1,
                      d[u.index][u.bit].s+cost);
        pq.push(State(next.f,nbit,d[next.f][nbit].f,d[next.f][nbit].s));
      }
    }
  }
  return mp(inf,inf);
}

pid solve(){
  vector<Line> vl; 
  FOR(i,0,n)FOR(j,i+1,n)vl.pb(Line(vp[i],vp[j]));
  FOR(i,0,n)sp.pb(vp[i]);
  FOR(i,0,vl.size()){
    FOR(j,i+1,vl.size()){
      if(isParallel(vl[i],vl[j]))continue;
      sp.pb(getCrossPointLL(vl[i],vl[j]));
    }
  }
  sp=unique(sp);
  FOR(i,0,sp.size()){
    FOR(j,0,sp.size()){
      if(i==j)continue;
      int bits=0;
      int c=0;
      FOR(k,0,n){
        if(ccw(sp[i],sp[j],vp[k])==0){
          bits+=(1<<k);
          c++;
        }
      }
      if(c>=2)e[i].pb(mp(j,bits));
    }
  }
  return dijkstra();
}

int main()
{
  while(1){
    cin>>n;
    init();
    if(n==0)break;
    FOR(i,0,n){
      int x,y;
      cin>>x>>y;
      vp.pb(Point(x,y));
    }
    pid ans=solve();
    cout<<ans.f-1<<" ";
    pd(ans.s);
  }
  return 0;
}