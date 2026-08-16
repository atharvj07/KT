#include<bits/stdc++.h>
 
#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-8)
#define equals(a,b) (fabs((a)-(b))<EPS)
 
using namespace std;
 
class Point{
public:
  double x,y;
 
  Point(double x = 0,double y = 0): x(x),y(y){}
  Point operator + (Point p){return Point(x+p.x,y+p.y);}
  Point operator - (Point p){return Point(x-p.x,y-p.y);}
  Point operator * (double a){return Point(a*x,a*y);}
  Point operator / (double a){return Point(x/a,y/a);}
  bool operator < (const Point& p) const{ return !equals(x,p.x)?x<p.x:(!equals(y,p.y)&&y<p.y); }
  bool operator == (const Point& p)const{ return fabs(x-p.x) < EPS && fabs(y-p.y) < EPS; }
 
};
 
Point rotate(Point a,double rad){ return Point(cos(rad)*a.x - sin(rad)*a.y,sin(rad)*a.x + cos(rad)*a.y); }
 
const double DINF = 1e20;
int n;
Point ps[2][1010],tmp[1010];
 
inline double getDist(Point p){ return sqrt(p.x*p.x+p.y*p.y); }
 
bool comp_arg(const double &a,const double &b) { return !equals(fabs(a),fabs(b)) && fabs(a) < fabs(b); }
 
void compute(){
  Point grv[2] = {Point(),Point()};
  rep(i,2) rep(j,n) grv[i] = grv[i] + ps[i][j];
  rep(i,2) grv[i] = grv[i] / (double)n;
  rep(i,2) rep(j,n) ps[i][j] = ps[i][j] - grv[i];
  sort(ps[0],ps[0]+n);
  sort(ps[1],ps[1]+n);
 
  vector<double> arg_buf;
  rep(i,min(7,n)) rep(j,n) {
    double dist[2] = { getDist(ps[0][i]), getDist(ps[1][j]) };
    if( !equals(dist[0],dist[1]) ) continue;
    arg_buf.push_back( atan2(ps[0][i].y,ps[0][i].x) - atan2(ps[1][j].y,ps[1][j].x) );
  }
 
  sort(arg_buf.begin(),arg_buf.end(),comp_arg);
  arg_buf.erase(unique(arg_buf.begin(),arg_buf.end()),arg_buf.end());
 
  rep(i,(int)arg_buf.size()){
    double arg = arg_buf[i];
    rep(j,n) tmp[j] = rotate(ps[1][j],arg);
    sort(tmp,tmp+n);
    bool failed = false;
    rep(j,n) if( !( tmp[j] == ps[0][j] ) ) { failed = true; break; }
    if( !failed ) { printf("%.10lf\n",fabs(arg)); break; }
  }
 
}
 
int main(){
  while( cin >> n, n ){
    rep(i,2) rep(j,n) cin >> ps[i][j].x >> ps[i][j].y;
    compute();
  }
  return 0;
}