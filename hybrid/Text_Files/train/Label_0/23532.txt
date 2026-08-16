#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<complex>
#include<cassert>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-9)
#define equals(a,b) (fabs((a)-(b)) < EPS)
#define COUNTER_CLOCKWISE 1
#define CLOCKWISE -1 
#define ONLINE_BACK 2
#define ONLINE_FRONT -2
#define ON_SEGMENT 0

using namespace std;

// BEGIN - Library

bool LT(double a,double b) { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return equals(a,b) || a < b; }

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

// ??????????????¢????????????
double toRad(double agl){ return agl*M_PI/180.0; }

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

double getArea(vector<Point>& vec) {
  double sum = 0;
  for(int i=0;i<vec.size();i++)
    sum += cross(vec[i],vec[(i+1)%vec.size()]);
  return fabs(sum)/2.0;
}

  
typedef pair<double,double> dd;
const double DINF = 1e20;

#define pow2(a) ((a)*(a))

dd calc(double x1,double y1,double vx1,double vy1,
        double x2,double y2,double vx2,double vy2,double r){
  double VX = (vx1-vx2), X = (x1-x2), VY = (vy1-vy2), Y = (y1-y2);
  double a = pow2(VX) + pow2(VY), b = 2*(X*VX+Y*VY), c = pow2(X) + pow2(Y) - pow2(r);
  dd ret = dd(DINF,DINF);
  double D = b*b - 4 * a * c;

  if( LT(D,0.0) ) return ret;

  if( equals(a,0.0) ) {
    if( equals(b,0.0) ) return ret;
    if( LT(-c/b,0.0)  ) return ret;
    ret.first = - c / b;
    return ret;
  }

  if( equals(D,0.0) ) D = 0;
  ret.first  = ( -b - sqrt( D ) ) / ( 2 * a );
  ret.second = ( -b + sqrt( D ) ) / ( 2 * a );
  if( !equals(ret.first,ret.second) && ret.first > ret.second ) swap(ret.first,ret.second);
  return ret;
}


const Point ZERO = Point(0,0);
//??????AB??¨?????????cp,??????r????????¨?????±?????¨????????¢???????±???????
inline double calculator_TypeA(Point A,Point B,Point cp,double r){
  A = A - cp, B = B - cp; 
  if( A == ZERO || B == ZERO ) return 0;
  double cross_value = cross(A,B);
  if( equals(cross_value,0.0) ) return 0;
  double sig = LT(cross_value,0.0) ? -1 : 1;
  Segment AB = Segment(A,B);
  double nearest_distance = distanceLP(AB,ZERO);
  double distance_OA = abs(A);
  double distance_OB = abs(B);

  if( LTE(0.0,r-distance_OA) && LTE(0.0,r-distance_OB) && LTE(0.0,r-nearest_distance) ) {
    return sig * fabs( cross_value / 2.0 );
  } else if( LTE(0.0,distance_OA-r) && LTE(0.0,distance_OB-r) && LTE(0.0,nearest_distance-r) ) {
    return sig * ( r * r * (M_PI-getArg(A,ZERO,B)) ) / 2.0;
  } else if( LTE(0.0,distance_OA-r) && LTE(0.0,distance_OB-r) && LT(0.0,r-nearest_distance) ) {

    Point proj_p = projection(AB,ZERO);
    if( onSegment(AB.p1,AB.p2,proj_p) ) {
      Vector e = ( A - B ) / abs( A - B );
      dd tmp = calc(A.x,A.y,e.x,e.y,0,0,0,0,r);
      Point r_p1 = A + e * tmp.first;
      Point r_p2 = A + e * tmp.second; 
      double ret = r * r * (M_PI-getArg(B,ZERO,A)) / 2.0;
      double subtract = r * r * (M_PI-getArg(r_p1,ZERO,r_p2)) / 2.0 - fabs(cross(r_p1,r_p2))/2.0 ;
      return sig * ( ret - subtract );
    } else {
      return sig * ( r * r * (M_PI-getArg(B,ZERO,A)) ) / 2.0; 
    }
  } else {

    if( LT(distance_OB-r,0.0) ) swap(A,B);
    Vector e = ( A - B ) / abs( A - B );
    dd tmp = calc(A.x,A.y,e.x,e.y,0,0,0,0,r);
    Point r_p1 = A + e * tmp.first;
    Point r_p2 = A + e * tmp.second; 
    if( onSegment(A,B,r_p2) ) r_p1 = r_p2;
    double ret = fabs(cross(r_p1,A)) * 0.5;
    ret += r * r * (M_PI-getArg(r_p1,ZERO,B)) * 0.5;
    return sig * ret;
  }
  assert(false);
}

double getCommonAreaPolygonCircle(const Polygon &poly,Point cp,double r){
  double sum = 0;
  rep(i,(int)poly.size()){  
    sum += calculator_TypeA(poly[i],poly[(i+1)%(int)poly.size()],cp,r);
  }
  return fabs(sum);
}

Polygon andrewScan(Polygon s) {
  Polygon u,l;
  if(s.size() < 3)return s;

  sort(s.begin(),s.end());

  u.push_back(s[0]);
  u.push_back(s[1]);
  l.push_back(s[s.size()-1]);
  l.push_back(s[s.size()-2]);

  for(int i=2;i<(int)s.size();i++)
    {
      for(int n=u.size();n >= 2 && ccw(u[n-2],u[n-1],s[i]) != CLOCKWISE; n--)
	u.pop_back();
      u.push_back(s[i]);
    }

  for(int i=s.size()-3; i>=0 ; i--)
    {
      for(int n=l.size(); n >= 2 && ccw(l[n-2],l[n-1],s[i]) != CLOCKWISE; n--)
	l.pop_back();
      l.push_back(s[i]);
    }

  reverse(l.begin(),l.end());

  for(int i = u.size()-2; i >= 1; i--) l.push_back(u[i]);

  return l;
}



Point calc_ps(Polygon poly) {
  poly = andrewScan(poly);
  Point mp = poly[0];
  double rate = 1; // 0.5???????????¨???
  int max_pos;
  double eps = 1e-10; // 1e-20???????????¨???
  while( rate > eps ) {
    rep(_,60){ // 70???????????¨???
      max_pos = 0;
      REP(j,1,(int)poly.size()) {
        double dist1 = abs(mp-poly[max_pos]);
        double dist2 = abs(mp-poly[j]);
	if( LT(dist1,dist2) ) max_pos = j;
      }
      mp.x += ( poly[max_pos].x - mp.x ) * rate;
      mp.y += ( poly[max_pos].y - mp.y ) * rate;
    }
    rate *= 0.5;
  }
  return mp;
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


// END   - Library

int n,r;
Polygon poly;

void compute() {
  double maxi;
  Point mp = calc_ps(poly);
  maxi = getCommonAreaPolygonCircle(poly,mp,r);
  double rate = 1.0;
  double eps = 1e-10;
  while( LT(eps,rate) ) {
    rep(_,70) {
      double max_area = -1; 
      Point np;
      rep(i,n) {
	Point tp = mp;
	tp.x += ( poly[i].x - mp.x ) * rate;
	tp.y += ( poly[i].y - mp.y ) * rate;
	double area = getCommonAreaPolygonCircle(poly,tp,r);
	if( LT(max_area,area) ) {
	  max_area = area;
	  np = tp;
	}
      }
      assert( !equals(max_area,-1) );
      mp = np;
      if( LT(maxi,max_area) ) maxi = max_area;
    }
    rate *= 0.5;
  }
  rep(__,10) {
    Point mp = calc_ps(poly);
    double rate = 1.0;
    double eps = 1e-10;
    while( LT(eps,rate) ) {
      rep(_,70) {
	double max_area = -1; 
	Point np;
	rep(i,n) {
	  Point tp = mp;
	  tp.x += ( poly[i].x - mp.x ) * rate;
	  tp.y += ( poly[i].y - mp.y ) * rate;
	  double area = getCommonAreaPolygonCircle(poly,tp,r);
	  if( LT(max_area,area) ) {
	    max_area = area;
	    np = tp;
	  }
	}
	if( rand() % 50 == 0 ) {
	  int v = rand() % n;
	  np.x = ( poly[v].x - mp.x ) * rate;
	  np.y = ( poly[v].y - mp.y ) * rate;
	  double area = getCommonAreaPolygonCircle(poly,np,r);
	  if( LT(max_area,area) ) {
	    max_area = area;
	  }
	}
	assert( !equals(max_area,-1) );
	mp = np;
	if( LT(maxi,max_area) ) maxi = max_area;
      }
      rate *= 0.5;
    }
  }
  printf("%.10f\n",maxi);
}

int main() {
  srand((unsigned int)time(NULL));
  cin >> n >> r;
  poly.resize(n);
  rep(i,n) cin >> poly[i].x >> poly[i].y;
  //cout << getArea(poly) << endl;
  compute();
  return 0;
}