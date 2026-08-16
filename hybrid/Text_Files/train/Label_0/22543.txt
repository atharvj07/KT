#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-7)
#define equals(a,b) (fabs((a)-(b))<EPS)
#define COUNTER_CLOCKWISE 1
#define CLOCKWISE -1 
#define ONLINE_BACK 2
#define ONLINE_FRONT -2
#define ON_SEGMENT 0


using namespace std;

const bool debug = false; // DEBUG - DEBUG - DEBUG - DEBUG - DEBUG - DEBUG - DEBUG - DEBUG - DEBUG
 
inline double toRad(double theta){
  return theta * M_PI / 180.0;
}

// x >= y
bool GTE(double x, double y){ return equals(x,y) || x > y; }
 
// x > y
bool GT(double x, double y){ return !equals(x,y) && x > y; }
 
// x < y
bool LT(double x, double y){ return !equals(x,y) && x < y; }
 
// x <= y
bool LTE(double x, double y){ return equals(x,y) || x < y; }

// -- Library 2d -- BEGIN ----------------------------------------
class Point{
public:
  double x,y;
 
  Point(double x = 0,double y = 0): x(x),y(y){}
 
  Point operator + (Point p){return Point(x+p.x,y+p.y);}
  Point operator - (Point p){return Point(x-p.x,y-p.y);}
  Point operator * (double a){return Point(a*x,a*y);}
  Point operator / (double a){return Point(x/a,y/a);}
  Point operator * (Point a){ return Point(x * a.x - y * a.y, x * a.y + y * a.x); }
 
  bool operator < (const Point& p) const{ return !equals(x,p.x)?x<p.x:(!equals(y,p.y)&&y<p.y); }
 
  bool operator == (const Point& p)const{ return fabs(x-p.x) < EPS && fabs(y-p.y) < EPS; }
 
};
 
struct Segment{
  Point p1,p2;
  Segment(Point p1 = Point(),Point p2 = Point()):p1(p1),p2(p2){}
  bool operator <  (const Segment& s) const { return ( p2 == s.p2 ) ? p1 < s.p1 : p2 < s.p2; }
  bool operator == (const Segment& s) const { return ( s.p1 == p1 && s.p2 == p2 ) || ( s.p1 == p2 && s.p2 == p1 ); }
 
};
 
typedef Point Vector;
typedef Segment Line;
typedef vector<Point> Polygon;
 
ostream& operator << (ostream& os,const Point& a){ return os << "(" << a.x << "," << a.y << ")"; }
 
ostream& operator << (ostream& os,const Segment& a){ return os << "( " << a.p1 << " , " << a.p2 << " )"; }
 
double dot(Point a,Point b){ return a.x*b.x + a.y*b.y; }
 
double cross(Point a,Point b){ return a.x*b.y - a.y*b.x; }
 
double norm(Point a){ return a.x*a.x+a.y*a.y; }
 
double abs(Point a){ return sqrt(norm(a)); }
 
//rad ????§???????????????¢?????§?????????????????¨
Point rotate(Point a,double rad){ return Point(cos(rad)*a.x - sin(rad)*a.y,sin(rad)*a.x + cos(rad)*a.y); }
 
// a => prev, b => cur, c=> next
// prev ?????? cur ????????£??? next ????????????????§????????±???????
double getArg(Point a,Point b,Point c){
  double arg1 = atan2(b.y-a.y,b.x-a.x);
  double arg2 = atan2(c.y-b.y,c.x-b.x);
  double arg = fabs( arg1 - arg2 );
  while( arg > M_PI ) arg -= 2.0 * M_PI;
  return fabs(arg);
}

int ccw(Point p0,Point p1,Point p2){
  Point a = p1-p0;
  Point b = p2-p0;
  if(cross(a,b) > EPS)return COUNTER_CLOCKWISE;
  if(cross(a,b) < -EPS)return CLOCKWISE;
  if(dot(a,b) < -EPS)return ONLINE_BACK;
  if(norm(a) < norm(b))return ONLINE_FRONT;
  return ON_SEGMENT;
}

bool intersectLL(Line l, Line m) {
  return abs(cross(l.p2-l.p1, m.p2-m.p1)) > EPS || // non-parallel
         abs(cross(l.p2-l.p1, m.p1-l.p1)) < EPS;   // same line
}
bool intersectLS(Line l, Line s) {
  return cross(l.p2-l.p1, s.p1-l.p1)*       // s[0] is left of l
         cross(l.p2-l.p1, s.p2-l.p1) < EPS; // s[1] is right of l
}
bool intersectLP(Line l,Point p) {
  return abs(cross(l.p2-p, l.p1-p)) < EPS;
}
bool intersectSS(Line s, Line t) {
  return ccw(s.p1,s.p2,t.p1)*ccw(s.p1,s.p2,t.p2) <= 0 &&
         ccw(t.p1,t.p2,s.p1)*ccw(t.p1,t.p2,s.p2) <= 0;
}
bool intersectSP(Line s, Point p) {
  return abs(s.p1-p)+abs(s.p2-p)-abs(s.p2-s.p1) < EPS; // triangle inequality
}
 
Point projection(Line l,Point p) {
  double t = dot(p-l.p1, l.p1-l.p2) / norm(l.p1-l.p2);
  return l.p1 + (l.p1-l.p2)*t;
}
Point reflection(Line l,Point p) {
  return p + (projection(l, p) - p) * 2;
}
double distanceLP(Line l, Point p) {
  return abs(p - projection(l, p));
}
double distanceLL(Line l, Line m) {
  return intersectLL(l, m) ? 0 : distanceLP(l, m.p1);
}
 
double distanceLS(Line l, Line s) {
  if (intersectLS(l, s)) return 0;
  return min(distanceLP(l, s.p1), distanceLP(l, s.p2));
}
double distanceSP(Line s, Point p) {
  Point r = projection(s, p);
  if (intersectSP(s, r)) return abs(r - p);
  return min(abs(s.p1 - p), abs(s.p2 - p));
}
 
double distanceSS(Line s, Line t) {
  if (intersectSS(s, t)) return 0;
  return min(min(distanceSP(s, t.p1), distanceSP(s, t.p2)),
             min(distanceSP(t, s.p1), distanceSP(t, s.p2)));
}
 
Point crosspoint(Line l,Line m){
  double A = cross(l.p2-l.p1,m.p2-m.p1);
  double B = cross(l.p2-l.p1,l.p2-m.p1);
  if(abs(A) < EPS && abs(B) < EPS){
    vector<Point> vec;
    vec.push_back(l.p1),vec.push_back(l.p2),vec.push_back(m.p1),vec.push_back(m.p2);
    sort(vec.begin(),vec.end());
    assert(vec[1] == vec[2]); //???????????°??????????????????
    return vec[1];
    //return m.p1;
  }
  if(abs(A) < EPS)assert(false);
  return m.p1 + (m.p2-m.p1)*(B/A);
}

struct Edge {
  int from,to;
  double cost;
  Edge(int from=0,int to=0,double cost=0):from(from),to(to),cost(cost){}
  bool operator < (const Edge& a)const { return !equals(cost,a.cost) && cost < a.cost; }
};
 
vector<vector<Edge> > segmentArrangement(vector<Segment> vs,vector<Point> &ps) {
/*
???????????????????????????
????????§???????????????????????????ps????????????
*/
  rep(i,(int)vs.size())
    REP(j,i+1,(int)vs.size())
    if(intersectSS(vs[i],vs[j]))
      ps.push_back(Point(crosspoint(vs[i],vs[j])));
 
  sort(ps.begin(),ps.end());  
  ps.erase(unique(ps.begin(),ps.end()),ps.end());
 
  vector<vector<Edge> > ret(ps.size());
 
  for(int i=0;i<(int)vs.size();i++){
    vector<pair<double,int> > list;
    rep(j,(int)ps.size()) if(intersectSP(vs[i],ps[j]))list.push_back(pair<double,int>(norm(vs[i].p1-ps[j]),j));
    sort(list.begin(),list.end());
    for(int j=0;j+1<(int)list.size();++j) {
      int from = list[j].second, to = list[j+1].second;
      double cost = abs(ps[from]-ps[to]);
      ret[from].push_back(Edge(from,to,cost));
      ret[to].push_back(Edge(to,from,cost));
    }
  }  
  return ret;
}
 
//cross product of pq and pr
double cross3p(Point p,Point q,Point r) { return (r.x-q.x) * (p.y -q.y) - (r.y - q.y) * (p.x - q.x); }
  
//returns true if point r is on the same line as the line pq
bool collinear(Point p,Point q,Point r) { return fabs(cross3p(p,q,r)) < EPS; }
  
//returns true if point t is on the left side of line pq
bool ccwtest(Point p,Point q,Point r){
  return cross3p(p,q,r) > 0; //can be modified to accept collinear points
}
 
bool onSegment(Point p,Point q,Point r){
  return collinear(p,q,r) && equals(sqrt(pow(p.x-r.x,2)+pow(p.y-r.y,2)) + sqrt(pow(r.x-q.x,2) + pow(r.y-q.y,2) ),sqrt(pow(p.x-q.x,2)+pow(p.y-q.y,2)) ) ;
}
  
 
bool isConvex(vector<Point> p) {
  int sz = (int)p.size();
  if(sz < 3)return false;//boundary case, we treat a point or a line as not convex
  bool isLeft = ccwtest(p[0],p[1],p[2]);
  for(int i=1; i<(int)p.size();i++)
    if(ccwtest(p[i],p[(i+1)%sz],p[(i+2)%sz]) != isLeft) return false;
  return true;
}
 
 
double angle(Point a,Point b,Point c) {
  double ux = b.x - a.x, uy = b.y - a.y;
  double vx = c.x - a.x, vy = c.y - a.y;
  return acos((ux*vx + uy*vy)/sqrt((ux*ux + uy*uy) * (vx*vx + vy*vy)));
}  
  
//????§???¢poly?????????????????????????????????p????????¨??????????????????????????????  
bool inPolygon(Polygon poly,Point p){
  if((int)poly.size() == 0)return false;
  rep(i,(int)poly.size()) if(onSegment(poly[i],poly[(i+1)%poly.size()],p))return true;
  double sum = 0;
  for(int i=0; i < (int)poly.size() ;i++) {
    if( equals(cross(poly[i]-p,poly[(i+1)%poly.size()]-p),0.0) ) continue; // ????????????????????¨angle???nan?????????sum???nan??????????????¬
    if( cross3p(p,poly[i],poly[(i+1)%poly.size()]) < 0 ) sum -= angle(p,poly[i],poly[(i+1)%poly.size()]);
    else                                                 sum += angle(p,poly[i],poly[(i+1)%poly.size()]);
  }
  // ?????????????????????????????????????????¨?????????????????§??\????????????????????? 
  const double eps = 1e-5;
  return (fabs(sum - 2*M_PI) < eps || fabs(sum + 2*M_PI) < eps);
}  


bool inPolygon(const Polygon &poly,Segment seg){
  vector<Point> vp;
  vp.push_back(seg.p1);
  vp.push_back(seg.p2);
  rep(i,(int)poly.size()) {
    Segment edge = Segment(poly[i],poly[(i+1)%(int)poly.size()]);
    if( equals(cross(seg.p1-seg.p2,edge.p1-edge.p2),0.0) ) {
      if( onSegment(seg.p1,seg.p2,edge.p1) ) vp.push_back(edge.p1);
      if( onSegment(seg.p1,seg.p2,edge.p2) ) vp.push_back(edge.p2);
    } else {
      if( intersectSS(seg,edge) ) vp.push_back(crosspoint(seg,edge));
    }
  }
  sort(vp.begin(),vp.end());
  vp.erase(unique(vp.begin(),vp.end()),vp.end());
  rep(i,(int)vp.size()-1) {
    Point middle_point = ( vp[i] + vp[i+1] ) / 2.0;
    if( !inPolygon(poly,middle_point) ) return false;
  }
  return true;  
}
 
Polygon andrewScan(Polygon s)
{
  Polygon u,l;
  if((int)s.size() < 3)return s;
 
  sort(s.begin(),s.end());
 
  u.push_back(s[0]);
  u.push_back(s[1]);
  l.push_back(s[s.size()-1]);
  l.push_back(s[s.size()-2]);
 
  for(int i=2;i<(int)s.size();i++)
    {
      for(int n=(int)u.size();n >= 2 && ccw(u[n-2],u[n-1],s[i]) != CLOCKWISE; n--)
	u.pop_back();
      u.push_back(s[i]);
    }
 
  for(int i=(int)s.size()-3; i>=0 ; i--)
    {
      for(int n=(int)l.size(); n >= 2 && ccw(l[n-2],l[n-1],s[i]) != CLOCKWISE; n--)
	l.pop_back();
      l.push_back(s[i]);
    }
 
  reverse(l.begin(),l.end());
 
  for(int i = (int)u.size()-2; i >= 1; i--) l.push_back(u[i]);
 
  return l;
}


// -- Library 2d -- END   ----------------------------------------

struct Data {
  int cur;
  double v;
  bool operator < (const Data &data) const {
    //return v > data.v;
    return LT(data.v,v); // data.v < v
  }
};

double dijkstra(vector<vector<Edge>> &G,int s,int t) {

  int V = G.size();
  vector<double> mini(V,1e8);

  priority_queue<Data> Q;
  Q.push((Data){s,0});
  mini[s] = 0;

  while( !Q.empty() ) {
    Data data = Q.top(); Q.pop();
    rep(i,(int)G[data.cur].size()) {
      Edge &e = G[data.cur][i];
      if( LT(data.v+e.cost,mini[e.to]) ) {
	mini[e.to] = data.v + e.cost;
	Q.push((Data){e.to,mini[e.to]});
      }
    }
  }
  assert( !equals(mini[t],1e8) );
  return mini[t];
}

inline bool is_parallel(Segment s,Segment t) { return equals(cross(s.p1-s.p2,t.p1-t.p2),0.0); }

const double rho = 1e5;
Polygon calc_shadow(Polygon &poly,double H,double theta,double phi) {
  assert( poly.size() >= 3 );
  assert( !( is_parallel(Segment(poly[0],poly[1]),Segment(poly[1],poly[2])) ) );
  
  theta = toRad(theta);
  phi   = toRad(phi);
  if( debug ) {
    cout << "theta = " << theta << " and phi = " << phi << endl;
  }
  Polygon shadow_poly;
  rep(i,(int)poly.size()) {
    double r = H / tan(phi);
    Vector v = Vector(r*cos(theta),r*sin(theta));
    shadow_poly.push_back(poly[i]-v);
  }
  rep(i,(int)poly.size()) shadow_poly.push_back(poly[i]);
  return andrewScan(shadow_poly);
}

void compute(vector<double> &H,vector<Polygon> &polies,vector<Segment> &segs,double theta,double phi,Point &s,Point &t) {  
  // ??±?????°??????????§????
  vector<Polygon> shadow_polies;
  rep(i,(int)polies.size()) {
    shadow_polies.push_back(calc_shadow(polies[i],H[i],theta,phi));
    if( debug ) {
      puts("");
      cout << i << "-th polygon (MINE)" << endl;
      rep(j,(int)shadow_polies[i].size()) {
	cout << shadow_polies[i][j] << endl;
      }
      puts("");
    }
  }
  
  if( debug ) {
    puts("");
    cout << "--- graph construction was finished! ---" << endl;
    puts("");
  }

  // ????????????
  vector<Point> ps;
  rep(i,(int)segs.size()) {
    ps.push_back(segs[i].p1);
    ps.push_back(segs[i].p2);
  }
  ps.push_back(s);
  ps.push_back(t);
  rep(i,(int)shadow_polies.size()) {
    int V = shadow_polies[i].size();
    rep(j,V) {
      Segment seg = Segment(shadow_polies[i][j],shadow_polies[i][(j+1)%V]);
      rep(k,(int)segs.size()) {
	if( intersectSS(seg,segs[k]) ) {
	  ps.push_back(crosspoint(seg,segs[k]));
	}
      }
    }
  }

  if( debug ) {
    puts("");
    cout << "--- enumeration was finished! ---" << endl;
    puts("");
  }

  // ??°???????§????
  vector<vector<Edge>> G = segmentArrangement(segs,ps);
  assert( G.size() == ps.size() );

  if( debug ) {
    puts("");
    cout << "--- arrangement was finished! ---" << endl;
    puts("");
  }

  // ???????????? (????????°????????±???????????????????????????0)
  rep(i,(int)G.size()) {
    rep(j,(int)G[i].size()) {
      Edge &e = G[i][j];
      Point mp = (ps[e.from]+ps[e.to])/2.0;
      bool in_shadow = false;
      rep(k,(int)shadow_polies.size()) {
	if( inPolygon(shadow_polies[k],mp) ) {
	  in_shadow = true;
	  break;
	}
      }
      if( in_shadow ) {
	e.cost = 0;
      }
    }
  }

  if( debug ) {
    puts("");
    cout << "--- weighting was finished! ---" << endl;
    puts("");
  }
  
  // dijkstra
  int sp=-1,ep=-1;
  rep(i,(int)ps.size()) {
    if( ps[i] == s ) sp = i;
    if( ps[i] == t ) ep = i;
  }
  assert( sp != -1 );
  assert( ep != -1 );
  printf("%.10f\n",dijkstra(G,sp,ep));
}


int main() {
  int N,M;
  while( cin >> N >> M, N|M ) {
    vector<double> H(N);
    vector<Polygon> polies(N);
    rep(i,N) {
      int V;
      cin >> V >> H[i];
      polies[i].resize(V);
      rep(j,V) cin >> polies[i][j].x >> polies[i][j].y;
    }
    vector<Segment> segs(M);
    rep(i,M) cin >> segs[i].p1.x >> segs[i].p1.y >> segs[i].p2.x >> segs[i].p2.y;
    double theta,phi;
    cin >> theta >> phi;
    Point s,t;
    cin >> s.x >> s.y;
    cin >> t.x >> t.y;

    rep(i,N) {
      int V = polies[i].size();
      rep(j,V) {
	Segment seg = Segment(polies[i][j],polies[i][(j+1)%V]);
	rep(k,M) {
	  assert( !intersectSS(seg,segs[k]) );
	}
      }
    }

    compute(H,polies,segs,theta,phi,s,t);
  }
  return 0;
}