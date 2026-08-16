#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-6)
#define COUNTER_CLOCKWISE 1
#define CLOCKWISE -1 
#define ONLINE_BACK 2
#define ONLINE_FRONT -2
#define ON_SEGMENT 0
#define equals(a,b) (fabs((a)-(b)) < EPS)

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
  bool operator <  (const Segment& s)const { return (p1==s.p1) ? p2 < s.p2 : p1 < s.p1; } 
  bool operator == (const Segment& p)const { return ( p.p1 == p1 && p.p2 == p2 ) || ( p.p1 == p2 && p.p2 == p1 ); }
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

//rad は角度をラジアンで持たせること
Point rotate(Point a,double rad){ return Point(cos(rad)*a.x - sin(rad)*a.y,sin(rad)*a.x + cos(rad)*a.y); }

// 度をラジアンに変換
double toRad(double agl){ return agl*M_PI/180.0; }

// a => prev, b => cur, c=> next
// prev から cur へ行って next へ行く際の角度を求める
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

int V;
Polygon poly;
Point light;

// type 0 => =w=, type 1 => mirror
void inner_add_new_points(Polygon &pol,vector<Point> &vp,int type,Line ref){
  rep(i,V){
    Vector e = ( poly[i] - light ) / abs( poly[i] - light );
    Segment seg = Segment(light,light+e*10000);
    rep(j,V) {
      Segment poly_seg = Segment(pol[j],pol[(j+1)%V]);
      if( equals(cross(seg.p2-seg.p1,poly_seg.p2-poly_seg.p1),0.0) ) continue;
      if( intersectSS(poly_seg,seg) ) {
        if( !type ) vp.push_back(crosspoint(poly_seg,seg));
        else        vp.push_back(reflection(ref,crosspoint(poly_seg,seg)));
      }
    }

    e = ( pol[i] - light ) / abs( pol[i] - light );
    seg = Segment(light,light+e*10000);
    rep(j,V) {
      Segment poly_seg = Segment(pol[j],pol[(j+1)%V]);
      if( equals(cross(seg.p2-seg.p1,poly_seg.p2-poly_seg.p1),0.0) ) continue;
      if( intersectSS(poly_seg,seg) ) {
        if( !type ) vp.push_back(crosspoint(poly_seg,seg));
        else        vp.push_back(reflection(ref,crosspoint(poly_seg,seg)));
      }
    }

  }
}

bool  LT(double a,double b) { return !equals(a,b) && a < b; } 
bool LTE(double a,double b) { return  equals(a,b) || a < b; } 

Point vir;
bool comp_dist(const Point& p1,const Point& p2){ return LT(abs(vir-p1),abs(vir-p2)); }

void add_new_points(Polygon &new_poly){
  vector<Point> vp;

  inner_add_new_points(poly,vp,0,Line());
  rep(i,V){
    Line ref = Line(poly[i],poly[(i+1)%V]);
    Polygon rpoly(V);
    rep(j,V) {
      rpoly[j] = reflection(ref,poly[j]);
      if( equals(rpoly[j].x,0.0) ) rpoly[j].x = 0;
      if( equals(rpoly[j].y,0.0) ) rpoly[j].y = 0;
    }
    inner_add_new_points(rpoly,vp,1,ref);
  }


  /*
  // 直接見える点の列挙
  rep(i,V){
    Vector e = ( poly[i] - light ) / abs( poly[i] - light );
    Segment vline = Segment(light,light+e*10000);
    rep(j,V){
      Segment seg = Segment(poly[j],poly[(j+1)%V]);
      if( equals(cross(vline.p1-vline.p2,seg.p1-seg.p2),0.0) ) continue;
      if( intersectSS(vline,seg) ) {
        if( onSegment(vline.p1,vline.p2,seg.p1) || onSegment(vline.p1,vline.p2,seg.p2) ) continue;
        if( onSegment(seg.p1,seg.p2,vline.p1)   || onSegment(seg.p1,seg.p2,vline.p2)   ) continue;
        vp.push_back(crosspoint(vline,seg));
      }
    }
  }

  // 鏡に反射して見える点の列挙

  rep(i,V){
    Line ref = Line(poly[i],poly[(i+1)%V]);
    Polygon rev_poly;
    rep(j,V) rev_poly.push_back(reflection(ref,poly[j]));    
    

  }
  */


  //------------------------------

  rep(i,(int)vp.size()) {
    if( equals(vp[i].x,0.0) ) vp[i].x = 0;
    if( equals(vp[i].y,0.0) ) vp[i].y = 0;
  }

  vector<Point> tmp;
  rep(i,vp.size()) {
    bool failed = false;
    rep(j,V) if( vp[i] == poly[j] ) { failed = true; break; }
    if( !failed ) tmp.push_back(vp[i]);
  }
  vp = tmp;

  sort(vp.begin(),vp.end());
  vp.erase(unique(vp.begin(),vp.end()),vp.end());

  rep(i,V){
    vector<Point> buf;
    Segment seg = Segment(poly[i],poly[(i+1)%V]);
    rep(j,(int)vp.size()) if( onSegment(seg.p1,seg.p2,vp[j]) ) buf.push_back(vp[j]);
    vir = seg.p1;
    sort(buf.begin(),buf.end(),comp_dist);
    rep(j,(int)buf.size()) new_poly.push_back(buf[j]);
    new_poly.push_back(seg.p2);
  }  

}

void compute_saw(Polygon &npoly,bool *saw){
  
  int nV = npoly.size();  
  // 直接見れる

  rep(i,nV) {
    Point mp = ( npoly[i] + npoly[(i+1)%nV] ) / 2.0;
    Segment vline = Segment(light,mp);
    bool failed = false;
    rep(j,V) {
      Segment seg = Segment(poly[j],poly[(j+1)%V]);
      if( equals(cross(seg.p1-seg.p2,vline.p1-vline.p2),0.0) ) continue;
      if( intersectSS(seg,vline) ) {
        if( onSegment(seg.p1,seg.p2,vline.p1) || onSegment(seg.p1,seg.p2,vline.p2) ) continue;
        if( onSegment(vline.p1,vline.p2,seg.p1) || onSegment(vline.p1,vline.p2,seg.p2) ) continue;
        failed = true;
        break;
      }
    }
    if( failed ) continue;
    saw[i] = true;
  }
  /*
  cout << "direct see" << endl;
  rep(i,nV) if( saw[i] )cout << npoly[i] << "," << npoly[(i+1)%nV]<< endl;
  cout << endl;
  */
  // 鏡一枚で見れる

  // 直接見える鏡だけを列挙
  vector<Line> ref;
  rep(i,nV) {
    Point mp = ( npoly[i] + npoly[(i+1)%nV] ) / 2.0;
    Segment vline = Segment(light,mp);
    bool failed = false;
    rep(j,V) {
      Segment seg = Segment(poly[j],poly[(j+1)%V]);
      if( equals(cross(seg.p1-seg.p2,vline.p1-vline.p2),0.0) ) continue;
      if( intersectSS(seg,vline) ) {
        if( onSegment(seg.p1,seg.p2,vline.p1) || onSegment(seg.p1,seg.p2,vline.p2) ) continue;
        if( onSegment(vline.p1,vline.p2,seg.p1) || onSegment(vline.p1,vline.p2,seg.p2) ) continue;
        failed = true;
        break;
      }
    }
    if( !failed ) ref.push_back(Line(npoly[i],npoly[(i+1)%nV]));
  }
  
  vector<Polygon> ref_polies;
  rep(i,(int)ref.size()){
    Polygon tmp_poly;
    rep(j,(int)poly.size()) tmp_poly.push_back(reflection(ref[i],poly[j]));
    ref_polies.push_back(tmp_poly);
  }
  /*
  rep(i,(int)ref.size()) {
    cout << "ref[" << i << "] = " << ref[i] << endl;
    rep(j,(int)ref_polies[i].size()){
      cout << " " << ref_polies[i][j];
    } cout << endl;
  }
  */

  rep(i,nV) if( !saw[i] ) {
    rep(j,(int)ref.size()){
      Segment rev_edge = Segment(reflection(ref[j],npoly[i]),reflection(ref[j],npoly[(i+1)%nV]));
      Point rev_mp = ( rev_edge.p1 + rev_edge.p2 ) / 2.0;
      Segment rev_vline = Segment(light,rev_mp);
      if( equals(cross(rev_vline.p1-rev_vline.p2,ref[j].p1-ref[j].p2),0.0) ) continue;
      if( !intersectSS(rev_vline,ref[j]) ) continue;

      rev_vline.p1 = crosspoint(rev_vline,ref[j]);
      
      if( inPolygon(ref_polies[j],rev_vline) ) {
        saw[i] = true;
        break;
      }

    }
  }
  
}

void compute(){
  Polygon npoly;
  add_new_points(npoly);
  int nV = npoly.size();
  rep(i,nV) {
    if( equals(npoly[i].x,0.0) ) npoly[i].x = 0;
    if( equals(npoly[i].y,0.0) ) npoly[i].y = 0;
  }
  bool saw[nV];
  rep(i,nV) saw[i] = false;
  compute_saw(npoly,saw);
  rep(i,nV) {
    if( equals(npoly[i].x,0.0) ) npoly[i].x = 0;
    if( equals(npoly[i].y,0.0) ) npoly[i].y = 0;
  }
  /*
  cout << "nV = " << nV << endl;
  rep(i,nV) cout << i << "-th " << npoly[i] << endl;
  cout << endl;

  rep(i,nV) {
    if( !saw[i] ) cout << "cannot see " << npoly[i] << "," << npoly[(i+1)%nV] << " : " << abs(npoly[i]-npoly[(i+1)%nV]) << endl;
  }
  */

  double sum = 0;
  rep(i,nV) if( !saw[i] )sum += abs(npoly[(i+1)%nV]-npoly[i]);
  sum = fabs(sum);
  printf("%.10lf\n",sum);
}

int main(){
  while( cin >> V, V ){
    poly.resize(V);
    rep(i,V) cin >> poly[i].x >> poly[i].y;
    cin >> light.x >> light.y;
    compute();
  }
  return 0;
}