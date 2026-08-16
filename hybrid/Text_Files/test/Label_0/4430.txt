#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-5)
#define equals(a,b) (fabs((a)-(b))<EPS)

using namespace std;

static const int COUNTER_CLOCKWISE = 1;
static const int CLOCKWISE = -1;
static const int ONLINE_BACK = 2;
static const int ONLINE_FRONT = -2;
static const int ON_SEGMENT = 0;

bool  LT(double a,double b) { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return  equals(a,b) || a < b; }

class Point{
public:
  double x,y;

  Point(double x = 0,double y = 0): x(x),y(y){}

  Point operator + (const Point &p){return Point(x+p.x,y+p.y);}
  Point operator - (const Point &p){return Point(x-p.x,y-p.y);}
  Point operator * (double a){return Point(a*x,a*y);}
  Point operator / (double a){return Point(x/a,y/a);}
  Point operator * (const Point &a){ return Point(x * a.x - y * a.y, x * a.y + y * a.x); }

  bool operator < (const Point& p) const{ return !equals(x,p.x)?x<p.x:(!equals(y,p.y)&&y<p.y); }

  bool operator == (const Point& p)const{ return fabs(x-p.x) < EPS && fabs(y-p.y) < EPS; }

};

struct Segment{
  Point p1,p2;
  Segment(Point p1 = Point(),Point p2 = Point()):p1(p1),p2(p2){}
  bool operator <  (const Segment& s) const { return ( p1 == s.p1 ) ? p2 < s.p2 : p1 < s.p1; }
  bool operator == (const Segment& p) const { return ( p.p1 == p1 && p.p2 == p2 ) || ( p.p1 == p2 && p.p2 == p1 ); }
};

typedef Point Vector;
typedef Segment Line;
typedef vector<Point> Polygon;

ostream& operator << (ostream& os,const Point& a){ os << "(" << a.x << "," << a.y << ")"; }

ostream& operator << (ostream& os,const Segment& a){ os << "( " << a.p1 << " , " << a.p2 << " )"; }

double dot(const Point &a,const Point &b){ return a.x*b.x + a.y*b.y; }

double cross(const Point &a,const Point &b){ return a.x*b.y - a.y*b.x; }

double norm(const Point &a){ return a.x*a.x+a.y*a.y; }

double abs(const Point &a){ return sqrt(norm(a)); }

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

Point nearest_point(Segment seg,Point p){
  Point r = projection(seg,p);
  if( intersectSP(seg,r) ) return r;
  if( LT(abs(seg.p1-p),abs(seg.p2-p)) ) return seg.p1;
  return seg.p2;
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
  }
  if(abs(A) < EPS)assert(false);
  return m.p1 + (m.p2-m.p1)*(B/A);
}

double cross3p(Point p,Point q,Point r){ return (r.x-q.x) * (p.y -q.y) - (r.y - q.y) * (p.x - q.x); }
  
bool collinear(Point p,Point q,Point r){ return fabs(cross3p(p,q,r)) < EPS; }
  
bool ccwtest(Point p,Point q,Point r) { return cross3p(p,q,r) > 0; }
 
bool onSegment(Point p,Point q,Point r){
  return collinear(p,q,r) && equals(sqrt(pow(p.x-r.x,2)+pow(p.y-r.y,2)) + sqrt(pow(r.x-q.x,2) + pow(r.y-q.y,2) ),sqrt(pow(p.x-q.x,2)+pow(p.y-q.y,2)) ) ;
}


double angle(Point a,Point b,Point c){
  double ux = b.x - a.x, uy = b.y - a.y;
  double vx = c.x - a.x, vy = c.y - a.y;
  return acos((ux*vx + uy*vy)/sqrt((ux*ux + uy*uy) * (vx*vx + vy*vy)));
}  
  
//多角形poly内（線分上も含む）に点pが存在するかどうは判定する  
inline bool inPolygon(Polygon poly,Point p,int on) {
  if( LT(poly[0].x,p.x) && LT(p.x,poly[3].x) && LT(poly[0].y,p.y) && LT(p.y,poly[1].y) ) return true;
  return false;
  /*
  if((int)poly.size() == 0)return false;
  if( on ) rep(i,poly.size()) if(onSegment(poly[i],poly[(i+1)%poly.size()],p))return true;
  double sum = 0;
  for(int i=0; i < (int)poly.size() ;i++) {
    if( equals(cross(poly[i]-p,poly[(i+1)%poly.size()]-p),0.0) ) continue;
    if(cross3p(p,poly[i],poly[(i+1)%poly.size()]) < 0)
      sum -= angle(p,poly[i],poly[(i+1)%poly.size()]);
    else
      sum += angle(p,poly[i],poly[(i+1)%poly.size()]);
  }
  const double eps = 1e-5;
  return (fabs(sum - 2*M_PI) < eps || fabs(sum + 2*M_PI) < eps);
  */
}  


//----------------------------------

const double DINF = 1e20;
const int MAX_N = 40;
int N;
Point ps[40][2];
Point A,B;

Point vir;
bool comp_dist(const Point &p1,const Point &p2){
  return LT(abs(vir-p1),abs(vir-p2));
}

// target_segがtriesのいづれかと交差しているか? true -> 交差してる false -> してない
bool intersect_checker(const vector<Polygon>& tries,Segment target_seg){
  rep(i,tries.size()){
    vector<Point> vp;
    vp.push_back(target_seg.p1);
    vp.push_back(target_seg.p2);
    rep(j,tries[i].size()){
      Segment seg = Segment(tries[i][j],tries[i][(j+1)%tries[i].size()]);
      if( equals(cross(target_seg.p1-target_seg.p2,seg.p1-seg.p2),0.0) ) {
        if( onSegment(target_seg.p1,target_seg.p2,seg.p1) ) vp.push_back(seg.p1);
        if( onSegment(target_seg.p1,target_seg.p2,seg.p2) ) vp.push_back(seg.p2);
      } else {
        if( intersectSS(target_seg,seg) ) vp.push_back(crosspoint(target_seg,seg));
      }
    }
    sort(vp.begin(),vp.end());
    vp.erase(unique(vp.begin(),vp.end()),vp.end());
    vir = target_seg.p1;
    sort(vp.begin(),vp.end(),comp_dist);
    rep(k,(int)vp.size()-1) {
      Point mp = ( vp[k] + vp[k+1] ) / 2.0;
      if( inPolygon(tries[i],mp,0) ) return true;
    }
  }
  return false;
  /*
  rep(i,tries.size()){
    rep(j,tries[i].size()){
      Segment seg = Segment(tries[i][j],tries[i][(j+1)%tries[i].size()]);
      if( equals(cross(target_seg.p1-target_seg.p2,seg.p1-seg.p2),0.0) ) continue;
      if( intersectSS(target_seg,seg) ) {
        if( onSegment(target_seg.p1,target_seg.p2,seg.p1) || onSegment(target_seg.p1,target_seg.p2,seg.p2) ) continue;
        if( onSegment(seg.p1,seg.p2,target_seg.p1) || onSegment(seg.p1,seg.p2,target_seg.p2) ) continue;
        return true;
      }
    }
  }
  return false;
  */


}

inline bool containAnyPolygon(vector<Polygon> &polies,Point p){
  rep(i,polies.size()) {
    //if( inPolygon(polies[i],p,0) ) return true;
    if( LT(polies[i][0].x,p.x) && LT(p.x,polies[i][3].x) && LT(polies[i][0].y,p.y) && LT(p.y,polies[i][1].y) ) return true;
  }
  return false;
}

vector<Segment> createBombLine(vector<Polygon> &tries,Point sp){
  Polygon surround(4);
  surround[0] = Point(-20000,-20000); surround[1] = Point(-20000,20000);
  surround[2] = Point(20000,20000);   surround[3] = Point(20000,-20000);
  vector<Segment> ret;
  rep(i,tries.size()) rep(j,tries[i].size()){
    if( sp == tries[i][j] ) continue;
    Vector e = ( tries[i][j] - sp ) / abs( tries[i][j] - sp );
    Segment line = Segment(sp,sp+e*100000);
    vector<Point> vp;
    vp.push_back(sp);
    vp.push_back(tries[i][j]);
    rep(k,4) {
      if( equals(cross(surround[k]-surround[(k+1)%4],line.p1-line.p2),0.0) ) continue;
      Segment seg = Segment(surround[k],surround[(k+1)%4]);
      if( intersectSS(line,seg) ) vp.push_back(crosspoint(line,seg));
    }

    rep(k,tries.size()) rep(l,tries[k].size()) {
      Segment seg = Segment(tries[k][l],tries[k][(l+1)%tries[k].size()]);
      if( equals(cross(seg.p1-seg.p2,line.p1-line.p2),0.0) ) continue;
      if( intersectSS(seg,line) ) vp.push_back(crosspoint(seg,line));
    }

    sort(vp.begin(),vp.end());
    vp.erase(unique(vp.begin(),vp.end()),vp.end());
    vir = sp;
    sort(vp.begin(),vp.end(),comp_dist);
    rep(k,(int)vp.size()-1){
      Segment seg = Segment(vp[k],vp[k+1]);
      Point mp = ( seg.p1 + seg.p2 ) / 2.0;
      if( containAnyPolygon(tries,mp) ) break;
      ret.push_back(seg);
    }

  }
  sort(ret.begin(),ret.end());
  ret.erase(unique(ret.begin(),ret.end()),ret.end());
  return ret;
}

void makeGraph(const vector<Point> &vp,vector<vector<int> > &G,vector<Polygon> &tries){
  int V = vp.size();
  rep(i,V){
    REP(j,i+1,V){
      if( intersect_checker(tries,Segment(vp[i],vp[j])) ) continue;
      G[i].push_back(j);
      G[j].push_back(i);
    }
  }
}

//Aliceから各点への最短距離を求める
struct Data {  
  int cur;
  double weight;
  bool operator < ( const Data& data ) const { return !equals(weight,data.weight) && weight > data.weight; }
};

void dijkstra(const vector<vector<int> > &G,vector<Point> &vp,vector<double> &mindist){
  int V = vp.size();
  int sp = -1;
  rep(i,V) if( vp[i] == A ) { sp = i; break; }
  assert( sp != -1 );
  mindist[sp] = 0;
  priority_queue<Data> Q;
  Q.push((Data){sp,0});
  while( !Q.empty() ){
    Data data = Q.top(); Q.pop();

    if( LT(mindist[data.cur],data.weight) ) continue;
    
    rep(i,G[data.cur].size()){
      int to = G[data.cur][i];
      if( LT(data.weight+abs(vp[data.cur]-vp[to]),mindist[to]) ) {
        mindist[to] = data.weight+abs(vp[data.cur]-vp[to]);
        Q.push((Data){to,mindist[to]});
      }
    }
  }
}

void compute(){
  vector<Polygon> tries;
  rep(i,N) {
    Polygon poly;
    poly.push_back(ps[i][0]);
    poly.push_back(Point(ps[i][0].x,ps[i][1].y));
    poly.push_back(ps[i][1]);
    poly.push_back(Point(ps[i][1].x,ps[i][0].y));
    tries.push_back(poly);
  }

  //Bomb can find Alice already
  if( !intersect_checker(tries,Segment(A,B)) ) { puts("0.000"); return; } 

  vector<Segment> segs = createBombLine(tries,B);

  //rep(i,(int)segs.size()) cout << segs[i] << endl;

  vector<Point> vp;
  vp.push_back(A);
  rep(i,tries.size()) rep(j,tries[i].size()) vp.push_back(tries[i][j]);
  rep(i,segs.size()) rep(j,tries.size()) rep(k,tries[j].size()) {
    if( equals(cross(segs[i].p1-segs[i].p2,tries[j][k]-tries[j][(k+1)%tries[j].size()]),0.0) ) continue;
    Segment seg = Segment(tries[j][k],tries[j][(k+1)%tries[j].size()]);
    if( intersectSS(segs[i],seg) ) vp.push_back(crosspoint(segs[i],seg));
  }
  
  sort(vp.begin(),vp.end());
  vp.erase(unique(vp.begin(),vp.end()),vp.end());
  
  int V = vp.size();
  vector<vector<int> > G(V,vector<int>());
  makeGraph(vp,G,tries);

  vector<double> mindist(V,DINF);
  dijkstra(G,vp,mindist);

  //rep(i,V) cout << vp[i] << " " << mindist[i] << endl;

  double answer = DINF;
  rep(i,vp.size()) {
    if( LTE(answer,mindist[i]) ) continue;
    rep(j,segs.size()){
      double dist = mindist[i] + distanceSP(segs[j],vp[i]);
      if( LTE(answer,dist) ) continue;
      Point np = nearest_point(segs[j],vp[i]);
      Segment seg = Segment(vp[i],np);
      if( intersect_checker(tries,seg) ) continue;
      answer = dist;
    }
  }
  assert( !equals(answer,DINF) ); 
  printf("%.6lf\n",answer);
}

int main(){
  while( cin >> N, N ){
    rep(i,N) rep(j,2) cin >> ps[i][j].x >> ps[i][j].y;
    cin >> A.x >> A.y >> B.x >> B.y;
    rep(i,N) rep(j,2) {
      assert( -10000 <= ps[i][j].x && ps[i][j].x <= 10000 );
      assert( -10000 <= ps[i][j].y && ps[i][j].y <= 10000 );
    }

    assert( -10000 <= A.x && A.x <= 10000 );
    assert( -10000 <= A.y && A.y <= 10000 );

    assert( -10000 <= B.x && B.x <= 10000 );
    assert( -10000 <= B.y && B.y <= 10000 );

    compute();
  }
  return 0;
}