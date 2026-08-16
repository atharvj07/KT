#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-6)
#define equals(a,b) (fabs((a)-(b)) < EPS)
#define COUNTER_CLOCKWISE 1
#define CLOCKWISE -1 
#define ONLINE_BACK 2
#define ONLINE_FRONT -2
#define ON_SEGMENT 0

using namespace std;

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

ostream& operator << (ostream& os,const Point& a){ os << "(" << a.x << "," << a.y << ")"; }

ostream& operator << (ostream& os,const Segment& a){ os << "( " << a.p1 << " , " << a.p2 << " )"; }

double dot(Point a,Point b){ return a.x*b.x + a.y*b.y; }

double cross(Point a,Point b){ return a.x*b.y - a.y*b.x; }

double norm(Point a){ return a.x*a.x+a.y*a.y; }

double abs(Point a){ return sqrt(norm(a)); }

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
    assert(vec[1] == vec[2]); //同じセグメントかもよ
    return vec[1];
    //return m.p1;
  }
  if(abs(A) < EPS)assert(false);
  return m.p1 + (m.p2-m.p1)*(B/A);
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
  
//多角形poly内（線分上も含む）に点pが存在するかどうは判定する  
bool inPolygon(Polygon poly,Point p){
  if((int)poly.size() == 0)return false;
  rep(i,poly.size()) if(onSegment(poly[i],poly[(i+1)%poly.size()],p))return true;
  double sum = 0;
  for(int i=0; i < (int)poly.size() ;i++) {
    if( equals(cross(poly[i]-p,poly[(i+1)%poly.size()]-p),0.0) ) continue; // ３点が平行だとangleがnanを返しsumがnanになり死ぬ
    if( cross3p(p,poly[i],poly[(i+1)%poly.size()]) < 0 ) sum -= angle(p,poly[i],poly[(i+1)%poly.size()]);
    else                                                 sum += angle(p,poly[i],poly[(i+1)%poly.size()]);
  }
  // あまり誤差を厳しくしすぎると良くないので以下のほうが良い 
  const double eps = 1e-5;
  return (fabs(sum - 2*M_PI) < eps || fabs(sum + 2*M_PI) < eps);
}  

struct Edge {
  int from,to,rev;
  double cost;
  Edge(int from=0,int to=0,int rev=-1,double cost=0):from(from),to(to),rev(rev),cost(cost){}
  bool operator < (const Edge& a)const { return !equals(cost,a.cost) && cost < a.cost; }
};

vector<vector<Edge> > segmentArrangement(vector<Segment> vs,vector<Point> &ps) {

  rep(i,vs.size())
    REP(j,i+1,vs.size())
    if(intersectSS(vs[i],vs[j]))
      ps.push_back(Point(crosspoint(vs[i],vs[j])));

  sort(ps.begin(),ps.end());  
  ps.erase(unique(ps.begin(),ps.end()),ps.end());

  vector<vector<Edge> > ret(ps.size());

  for(int i=0;i<vs.size();i++){
    vector<pair<double,int> > list;
    rep(j,ps.size()) if(intersectSP(vs[i],ps[j]))list.push_back(pair<double,int>(norm(vs[i].p1-ps[j]),j));
    sort(list.begin(),list.end());
    for(int j=0;j+1<list.size();++j) {
      int from = list[j].second, to = list[j+1].second;
      double cost = abs(ps[from]-ps[to]);
      ret[from].push_back(Edge(from,to,-1,cost));
      ret[to].push_back(Edge(to,from,-1,cost));
    }
  }  

  vector<Point> tmp;
  rep(i,ps.size()) if( ret[i].size() >= 2 ) tmp.push_back(ps[i]);
  ps = tmp;
  ret.clear();
  ret.resize(ps.size());
  for(int i=0;i<vs.size();i++){
    vector<pair<double,int> > list;
    rep(j,ps.size()) if(intersectSP(vs[i],ps[j]))list.push_back(pair<double,int>(norm(vs[i].p1-ps[j]),j));
    sort(list.begin(),list.end());
    for(int j=0;j+1<list.size();++j) {
      int from = list[j].second, to = list[j+1].second;
      double cost = abs(ps[from]-ps[to]);
      ret[from].push_back(Edge(from,to,-1,cost));
      ret[to].push_back(Edge(to,from,-1,cost));
    }
  }    

  return ret;
}

////////////////// にゃんこまっしぐら ///////////////////////////////
const int MAX_V = 5000;
bool visited[MAX_V][MAX_V];
vector<vector<Edge> > G;
vector<Point> vp;

bool getPath(int start_node,int node,int edge,vector<Point> &buf,set<Point> &used){
  if( visited[node][edge] ){
    if( !buf.empty() && node == start_node ) return true;
    return false;
  }
  visited[node][edge] = true;
  if( used.count(vp[node]) ) return visited[node][edge] = false;
  used.insert(vp[node]);
  int next_node = G[node][edge].to;
  int next_edge = (G[node][edge].rev+1)%((int)G[next_node].size());
  buf.push_back(vp[G[node][edge].from]);
  if(getPath(start_node,next_node,next_edge,buf,used)) return true;
  else return visited[node][edge] = false;
}
///////////////// みゃおみゃお //////////////////////////////////////

int uf[MAX_V];
void init(int _size=MAX_V) { rep(i,_size) uf[i] = i; }
int find(int x) {
  if( x == uf[x] ) return x;
  return uf[x] = find(uf[x]);
}
void unit(int x,int y){
  x = find(x), y = find(y);
  if( x != y ) uf[x] = y;
}

bool  LT(double a,double b) { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return  equals(a,b) || a < b; }

// true -> CCW, false -> CW
bool rotationCheck(vector<Point>& vec){
  double sum = 0;
  for(int i=0;i<vec.size();i++) sum += cross(vec[i],vec[(i+1)%vec.size()]);
  return ( !equals(sum,0.0) && sum > 0 ); 
}


Point vir;
bool comp_angle(const Edge &a, const Edge &b){
  Vector va = vir - vp[a.to];
  Vector vb = vir - vp[b.to];
  return LT(atan2(va.y,va.x),atan2(vb.y,vb.x));
}


bool inPolygon(Polygon a,Polygon b) {
  rep(i,(int)a.size()) {
    Point mp = ( a[i] + a[(i+1)%(int)a.size()] ) / 2.0;
    if( !inPolygon(b,mp) ) return false;
  }
  return true;
}

bool canUnit(Polygon a,Polygon b){
  if( inPolygon(a,b) || inPolygon(b,a) ) return true;
  rep(i,(int)a.size()) rep(j,(int)b.size()) {
    Segment seg_a = Segment(a[i],a[(i+1)%(int)a.size()]);
    Segment seg_b = Segment(b[j],b[(j+1)%(int)b.size()]);
    if( equals(cross(seg_a.p1-seg_a.p2,seg_b.p1-seg_b.p2),0.0) ) {
      if( onSegment(seg_a.p1,seg_a.p2,seg_b.p1) || onSegment(seg_a.p1,seg_a.p2,seg_b.p2) ||
          onSegment(seg_b.p1,seg_b.p2,seg_a.p1) || onSegment(seg_b.p1,seg_b.p2,seg_a.p2) ) {
        vector<Point> tmp;
        tmp.push_back(seg_a.p1), tmp.push_back(seg_a.p2);
        tmp.push_back(seg_b.p1), tmp.push_back(seg_b.p2);
        sort(tmp.begin(),tmp.end());
        if( tmp[1] == tmp[2] ) continue;
        return true;
      }
    }
  }
  rep(i,(int)a.size()) {
    Point mp = ( a[i] + a[(i+1)%(int)a.size()] ) / 2.0;
      if( inPolygon(b,mp) ) return true;
  }
  rep(i,(int)b.size()) {
    Point mp = ( b[i] + b[(i+1)%(int)b.size()] ) / 2.0;
      if( inPolygon(a,mp) ) return true;
  }
  return false;
}

int N;

void compute(vector<Segment> &segs){
  G = segmentArrangement(segs,vp);
  int V = G.size();
  /*
  cout << V << endl;
  rep(i,V) cout << vp[i] << endl;
  */
  assert( V < MAX_V );



  rep(i,V) { vir = vp[i]; sort(G[i].begin(),G[i].end(),comp_angle); }

  rep(i,V) rep(j,(int)G[i].size()) if( G[i][j].rev == -1 ) {
    int to = G[i][j].to;
    rep(k,(int)G[to].size()) if( G[to][k].to == i ) {
      G[i][j].rev  = k;
      G[to][k].rev = j;
      break;
    }
  }

  vector<Polygon> polies;
  rep(i,V) rep(j,(int)G[i].size()) if( !visited[i][j] ) {
    vector<Point> buf;
    set<Point> used;
    if( getPath(i,i,j,buf,used) ) if( (int)buf.size() >= 3 ) {
        polies.push_back(buf);
      }
  }
  V = polies.size();
  /*
  cout << V << endl;
  rep(i,V){
    cout << i << "-th:" << endl;
    rep(j,polies[i].size()) cout << polies[i][j] << " "; cout << endl;
  }

  cout << endl;
  cout << endl;
  rep(i,V){
    rep(j,polies[i].size()){
      cout << polies[i][j].x << " " << polies[i][j].y << " " << polies[i][(j+1)%polies[i].size()].x << " " << polies[i][(j+1)%polies[i].size()].y << endl;
    }
  }
  cout << endl;
  cout << endl;
  */
  init(V);
  set<int> S;
  rep(i,V) rep(j,V) if( i != j ) {
    if( canUnit(polies[i],polies[j]) ) unit(i,j);
  }
  rep(i,V) S.insert(find(i));
  cout << (int)S.size() << endl;
}

int main(){
  cin >> N;
  vector<Segment> segs(N);
  rep(i,N)  cin >> segs[i].p1.x >> segs[i].p1.y >> segs[i].p2.x >> segs[i].p2.y;
  compute(segs);
  return 0;
}