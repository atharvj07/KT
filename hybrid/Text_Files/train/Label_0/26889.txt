#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-8)
#define equals(a,b) (fabs((a)-(b))<EPS)

using namespace std;

static const int COUNTER_CLOCKWISE = 1;
static const int CLOCKWISE = -1;
static const int ONLINE_BACK = 2;
static const int ONLINE_FRONT = -2;
static const int ON_SEGMENT = 0;

class Point{
public:
  double x,y;
  Point(double x = 0,double y = 0): x(x),y(y){}
  Point operator + (Point p){return Point(x+p.x,y+p.y);}
  Point operator - (Point p){return Point(x-p.x,y-p.y);}
  bool operator < (const Point& p) const{ return !equals(x,p.x)?x<p.x:y<p.y; }
};

typedef Point Vector;
typedef vector<Point> Polygon;

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

Polygon andrewScan(Polygon s){
  Polygon u,l;
  if(s.size() < 3)return s;
  sort(s.begin(),s.end());
  u.push_back(s[0]);
  u.push_back(s[1]);
  l.push_back(s[s.size()-1]);
  l.push_back(s[s.size()-2]);

  for(int i=2;i<s.size();i++){
    for(int n=u.size();n >= 2 && ccw(u[n-2],u[n-1],s[i]) != CLOCKWISE; n--) u.pop_back();
    u.push_back(s[i]);
  }
  for(int i=s.size()-3; i>=0 ; i--){
    for(int n=l.size(); n >= 2 && ccw(l[n-2],l[n-1],s[i]) != CLOCKWISE; n--) l.pop_back();
    l.push_back(s[i]);
  }
  reverse(l.begin(),l.end());
  for(int i = u.size()-2; i >= 1; i--) l.push_back(u[i]);
  return l;
}

vector<int> G[310];
int match[310];
bool used[310];
int V;
void add_edge(int u,int v){
  G[u].push_back(v);
  G[v].push_back(u);
}

bool dfs(int v){
  used[v] = true;
  for(int i=0;i<G[v].size();i++){
    int u = G[v][i], w = match[u];
    if( w < 0 || !used[w] && dfs(w) ) {
      match[v] = u;
      match[u] = v;
      return true;
    }
  }
  return false;
}

int bipartite_matching(){
  int res = 0;
  memset(match,-1,sizeof(match));
  rep(v,V){
    if( match[v] < 0 ) {
      memset(used,0,sizeof(used));
      if( dfs(v) ) res++;
    }
  }
  return res;
}


int n,m;
double r[110],poly_r[110];
Polygon vec[110];
Point ps[110];
vector<int> cand[110];

inline double dist(Point a) { return sqrt(a.x*a.x+a.y*a.y); }
bool LT(double a,double b)  { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return  equals(a,b) || a < b; }

Point calc_ps(Polygon poly) {
  poly = andrewScan(poly);
  Point mp = poly[0];
  double rate = 1;
  int max_pos;
  double eps = 1e-10;
  while( rate > eps ) {
    rep(_,60){
      max_pos = 0;
      REP(j,1,poly.size()) {
        double dist1 = dist(mp-poly[max_pos]);
        double dist2 = dist(mp-poly[j]);
        if( !fabs(dist1-dist2) < eps && dist1 < dist2 ) max_pos = j;
      }
      mp.x += ( poly[max_pos].x - mp.x ) * rate;
      mp.y += ( poly[max_pos].y - mp.y ) * rate;
    }
    rate *= 0.5;
  }
  return mp;
}

int main(){
  cin >> n >> m;
  V = n + m;
  rep(i,n) cin >> r[i];
  rep(i,m) {
    int p;
    cin >> p;
    vec[i].resize(p);
    rep(j,p) cin >> vec[i][j].x >> vec[i][j].y;
  }

  rep(i,m) ps[i] = calc_ps(vec[i]);

  rep(i,m) {
    double maxi = dist(ps[i]-vec[i][0]);
    REP(j,1,vec[i].size()) maxi = max(maxi,dist(ps[i]-vec[i][j]));
    poly_r[i] = maxi;
  }

  set<int> S[n];
  rep(i,n) {
    rep(j,m){
      if( LTE(poly_r[j],r[i]) ) { cand[i].push_back(j); S[i].insert(j); }
    }
  }
  int ans[m];
  bool completed[n];
  rep(i,m) ans[i] = -1;
  rep(i,n) completed[i] = false;
  rep(i,m) {
    rep(j,n) if( !completed[j] && !cand[j].empty() ){
      if( !S[j].count(i) ) continue;
      rep(k,V) G[k].clear();
      rep(k,n) if( k != j && !completed[k] )rep(l,cand[k].size()) {
        if( cand[k][l] == i || ans[cand[k][l]] != -1 ) continue;
        add_edge(cand[k][l],k+m);
      }
      int res = bipartite_matching();
      if( res == m - i - 1 ) {
        ans[i] = j + 1;
        completed[j] = true;
        goto Skip;
      }
    }
  Skip:;
    if( ans[i] == -1 ) { puts("NG"); return 0; }
  }

  rep(i,m) cout << ans[i] << endl;
  return 0;
}