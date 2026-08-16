/*
  テ」ツ?ャテ」ツ?」テ」ツ?ステ」ツ??
 */
#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-4)
#define equals(a,b) (fabs((a)-(b))<EPS)
#define COUNTER_CLOCKWISE 1
#define CLOCKWISE -1
#define ONLINE_BACK 2
#define ONLINE_FRONT -2
#define ON_SEGMENT 0

using namespace std;

bool LT(double a,double b) { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return equals(a,b) || a < b; }

class Point {
public:
  double x,y;

  Point(double x=0,double y=0):x(x),y(y){}

  Point operator + (const Point& p) { return Point(x+p.x,y+p.y); }
  Point operator - (const Point& p) { return Point(x-p.x,y-p.y); }
  Point operator * (const double& p) { return Point(x*p,y*p); }
  Point operator / (const double& p) { return Point(x/p,y/p); }
  
  bool operator < ( const Point & p ) const { return !equals(x,p.x)?x<p.x:(!equals(y,p.y)&&y<p.y);}
  bool operator == ( const Point & p ) const { return equals(x,p.x) && equals(y,p.y); }
  
};

struct Segment {
  Point p1,p2;
  Segment(Point p1=Point(),Point p2=Point()) : p1(p1), p2(p2) {}
};

typedef Point Vector;
typedef Segment Line;
typedef vector<Point> Polygon;


ostream& operator << (ostream& os,const Point&a ) { os << "(" << a.x << "," << a.y << ")"; }
ostream& operator << (ostream& os,const Segment& a) { os << "(" << a.p1 << "," << a.p2 << ")"; }

double dot(Point a,Point b) { return a.x*b.x + a.y*b.y; }
double cross(Point a,Point b) { return a.x*b.y-a.y*b.x; }
double norm(Point a) { return a.x*a.x + a.y*a.y; }
double abs(Point a) { return sqrt(norm(a)); }
double toRad(double a){ return a * M_PI / 180.0; }
Point rotate(Point a,double rad) { return Point(cos(rad)*a.x-sin(rad)*a.y,sin(rad)*a.x+cos(rad)*a.y); }

int ccw(Point p0,Point p1,Point p2){
  Point a = p1-p0;
  Point b = p2-p0;
  if( cross(a,b) > EPS ) return COUNTER_CLOCKWISE;
  if( cross(a,b) <-EPS ) return CLOCKWISE;
  if( dot(a,b) < -EPS ) return ONLINE_BACK;
  if( norm(a) < norm(b) ) return ONLINE_FRONT;
  return ON_SEGMENT;
}

bool intersectLP(Line l,Point p){
  return abs(cross(l.p2-p,l.p1-p)) < EPS;
}

Point projection(Line l,Point p) {
  double  t = dot(p-l.p1,l.p1-l.p2) / norm(l.p1-l.p2);
  return l.p1 + ( l.p1 - l.p2 ) * t;
}

Point reflection(Line l,Point p){
  return p + (projection(l,p)-p) * 2;
}

double cross3p(Point p,Point q,Point r) { return (r.x-q.x) * (p.y-q.y) - (r.y-q.y) * (p.x-q.x); }
bool collinear(Point p,Point q,Point r) { return fabs(cross3p(p,q,r)) < EPS; }
bool onSegment(Point p,Point q,Point r) {
  return collinear(p,q,r) && equals(sqrt(pow(p.x-r.x,2)+pow(p.y-r.y,2))+sqrt(pow(r.x-q.x,2)+pow(r.y-q.y,2)),sqrt(pow(p.x-q.x,2)+pow(p.y-q.y,2)));
}

const string YES = "Yes";
const string NO  = "No";
int n;

Polygon answerScan(Polygon s){
  Polygon u,l;
  if( s.size() < 3 ) return s;
  sort(s.begin(),s.end());
  u.push_back(s[0]);
  u.push_back(s[1]);
  l.push_back(s[s.size()-1]);
  l.push_back(s[s.size()-2]);
  REP(i,2,s.size()){
    for(int n=u.size();n>=2&&ccw(u[n-2],u[n-1],s[i])!=CLOCKWISE;n--)
      u.pop_back();
    u.push_back(s[i]);
  }
  for(int i=s.size()-3;i>=0;i--){
    for(int n=l.size();n>=2&&ccw(l[n-2],l[n-1],s[i])!=CLOCKWISE;n--)
      l.pop_back();
    l.push_back(s[i]);
  }
  reverse(l.begin(),l.end());
  for(int i=u.size()-2;i>=1;i--) l.push_back(u[i]);
  return l;

}

//// --additional

double getArea(vector<Point>& vec) {
  double sum = 0;
  for(int i=0;i<vec.size();i++)
    sum += cross(vec[i],vec[(i+1)%vec.size()]);
  return fabs(sum)/2.0;
}

Point getCentroidOfConvex(Polygon& poly){
  double area = getArea(poly);
  int V = poly.size();
  assert( !equals(area,0.0) );
  double x = 0, y = 0;
  rep(i,(int)poly.size()) {
    x += ( poly[i].x + poly[(i+1)%V].x ) * ( poly[i].x*poly[(i+1)%V].y - poly[(i+1)%V].x*poly[i].y );
    y += ( poly[i].y + poly[(i+1)%V].y ) * ( poly[i].x*poly[(i+1)%V].y - poly[(i+1)%V].x*poly[i].y );
  }
  return Point(x/(6.0*area),y/(6.0*area));
}


//// --additional

bool isValid(vector<Point> &vec) {
  Line line = Line(vec[0],vec[1]);
  bool ok = false;
  rep(i,vec.size()) {
    if( !intersectLP(line,vec[i]) ) { ok = true; break; }
  }
  if( !ok ) return false;
  return true;
}

bool isAnswer(Line line,vector<Point> &vec){
  vector<Point> vec_CW,vec_CCW;
  int on_line = 0;
  rep(j,n){
    if( intersectLP(line,vec[j]) ) { ++on_line; continue; }
    int res = ccw(line.p1,line.p2,vec[j]);
    assert( res == COUNTER_CLOCKWISE || res == CLOCKWISE );
    if( res == CLOCKWISE ) vec_CW.push_back(vec[j]);
    else                   vec_CCW.push_back(vec[j]);
  }
  if( vec_CW.size() != vec_CCW.size() ) return false;
  if( !( on_line <= 2 ) ) return false;

  map<Point,bool> mp;
  rep(j,vec_CCW.size()) mp[vec_CCW[j]] = true;
  bool success = true;
  rep(j,vec_CW.size()){
    Point rp = reflection(line,vec_CW[j]);
    if( !mp.count(rp) ) { success = false; break; }
  }
  return success;
}

void compute(vector<Point> &vec){
  if( !isValid(vec) ) {
    cout << NO << endl;
    return;
  }

  Polygon poly = answerScan(vec);
  //rep(i,poly.size()) cout << poly[i] << endl;
  Point centroid = getCentroidOfConvex(poly);

  rep(i,poly.size()){
    Vector v = poly[(i+1)%poly.size()] - poly[i];
    v = rotate(v,toRad(90));
    Vector e = v / abs(v);
    Point mid_p = (poly[i]+poly[(i+1)%poly.size()])/2;
    Line line = Line(mid_p,mid_p+e*100);
    if( isAnswer(line,vec) ) {
      cout << YES << endl;
      return;
    }

    // --additional
    line = Line(centroid,poly[i]);
    if( isAnswer(line,vec) ) {
      cout << YES << endl;
      return;
    }
  }
  /*
  rep(i,n) REP(j,i+1,n) {
    Line line = Line(vec[i],vec[j]);
    if( isAnswer(line,vec) ) {
      cout << YES << endl;
      return;
    }
  }
  */

  cout << NO << endl;
}

int main(){
  cin >> n;
  vector<Point> vec(n);
  rep(i,n) cin >> vec[i].x >> vec[i].y;
  compute(vec);
  return 0;
}