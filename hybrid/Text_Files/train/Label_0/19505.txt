#include<bits/stdc++.h>
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
double arg(Vector p){ return atan2(p.y,p.x);}

Point project(Segment s,Point p){
  Vector base=(s.p2-s.p1);
  double r=(dot(p-s.p1,base)/base.norm());
  return (s.p1+base*r);
}

Point reflect(Segment s,Point p){
  return p+(project(s,p)-p)*2;
}

bool isParallel(Vector a,Vector b){
  return equals(cross(a,b),0.0);
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

bool intersect(Point p1,Point p2,Point p3,Point p4){
  return (ccw(p1,p2,p3)*ccw(p1,p2,p4)<=0 &&
          ccw(p3,p4,p1)*ccw(p3,p4,p2)<=0);
}

bool intersect(Segment s1,Segment s2){
  return intersect(s1.p1,s1.p2,s2.p1,s2.p2);
}

Point getCrossPointSS(Segment s1,Segment s2){
  Vector base=s2.p2-s2.p1;
  double d1=abs(cross(base,s1.p1-s2.p1));
  double d2=abs(cross(base,s1.p2-s2.p1));
  double t=d1/(d1+d2);
  return (s1.p1+(s1.p2-s1.p1)*t);
}

Point getCrossPointLL(Line a,Line b){
  double A=cross(a.p2-a.p1,b.p2-b.p1);
  double B=cross(a.p2-a.p1,a.p2-b.p1);
  if(abs(A)<eps || abs(B)<eps)return b.p1;
  return b.p1+(b.p2-b.p1)*(B/A);
}

Line getPerpendicularBisector(Segment s){
  Point m=s.p1+(s.p2-s.p1)/2.0;
  Vector v1=s.p1-m,v2=s.p2-m;
  swap(v1.x,v1.y);
  v1.x=-v1.x;
  swap(v2.x,v2.y);
  v2.x=-v2.x;
  return Line(m+v1,m+v2);
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

Polygon convex_cut(Polygon p,Line l){
  Polygon ans;
  for(int i=0;i<p.size();i++){
    Point A=p[i],B=p[(i+1)%p.size()];
    if(ccw(l.p1,l.p2,A)!=-1)ans.push_back(A);
    if(ccw(l.p1,l.p2,A)*ccw(l.p1,l.p2,B)<0)
      ans.push_back(getCrossPointLL(l,Segment(A,B)));
  }
  return ans;
}

double getCircumference(Polygon p){
  double res=0;
  int n=p.size();
  for(int i=0;i<n;i++)res+=abs(p[i]-p[(i+1)%n]);
  return res;
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

Polygon erase(Polygon vp){
  Polygon res;
  int n=vp.size();
  for(int i=0;i<n;i++){
    Point p0=vp[i],p1=vp[(i+1)%n],p2=vp[(i+2)%n];
    if(ccw(p0,p2,p1)!=0)res.push_back(p1);
  }
  return res;
}

Polygon getReflectionofPolygon(Polygon p,Line L){
  Polygon res;
  for(int i=0;i<p.size();i++)res.push_back(reflect(L,p[i]));
  reverse(res.begin(),res.end());
  return res;
}

Polygon PolygonFolding(Polygon p,Line L){
  Polygon p1=convex_cut(p,L),p2=convex_cut(p,Line(L.p2,L.p1));
  p2=getReflectionofPolygon(p2,L);
  Polygon res,sets;
  for(int i=0;i<p1.size();i++){
    Segment s1(p1[i],p1[(i+1)%p1.size()]);
    for(int j=0;j<p2.size();j++){
      Segment s2(p2[j],p2[(j+1)%p2.size()]);
      if(isParallel(s1.p1-s1.p2,s2.p1-s2.p2))continue;
      if(intersect(s1,s2)){
	      Point p=getCrossPointLL(s1,s2);
	      if(s1.p1==p || s1.p2==p || s2.p1==p || s2.p2==p)continue;
	      sets.push_back(p);
      }
    }
  }
  for(int i=0;i<p1.size();i++){
    int c=ccw(L.p1,L.p2,p1[i]);
    if(c==0 || c==-2 || c==2){
      res.push_back(p1[i]);
    }
  }
  Point tmp=res[0]+(res[1]-res[0])/2.0;
  res.clear();
  for(int i=0;i<p1.size();i++)sets.push_back(p1[i]);
  for(int i=0;i<p2.size();i++)sets.push_back(p2[i]);
  sets=unique(sets);
  vector<pair<double,Point> > vp;
  for(int i=0;i<sets.size();i++){
    double targ=arg(sets[i]-tmp);
    if(targ<0)targ+=2*pi;
    vp.push_back(mp(targ,sets[i]));
  }
  sort(vp.begin(),vp.end());
  for(int i=0;i<vp.size();i++){
    if(contains(p1,vp[i].s)!=2 && contains(p2,vp[i].s)!=2)res.push_back(vp[i].s);
  }
  res=erase(res);
  return res;
}

bool comp(pid a,pid b){
  if(a.f!=b.f)return a.f<b.f;
  return (a.s-b.s)<eps;
}

int main()
{
  int n,x,y;

  while(1){
    cin>>n;
    if(n==0)break;
    Polygon p;
    FOR(i,0,n){
      cin>>x>>y;
      p.pb(Point(x,y));
    }
    pid ans(-1,-1);
    FOR(i,0,n){
      FOR(j,i+1,n){
        Line L=getPerpendicularBisector(Segment(p[i],p[j]));
        Polygon tmp=PolygonFolding(p,L);
        pid pii=mp(tmp.size(),getCircumference(tmp));
	      if(comp(ans,pii))ans=pii;
      }
    }
    pd(ans.s);
  }
  return 0;
}