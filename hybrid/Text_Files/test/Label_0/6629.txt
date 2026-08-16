#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-8;
const double INF = 1e+8;

struct P3{
  double x, y, z;
  P3(double x=0, double y=0, double z=0):x(x),y(y),z(z){}
  P3 operator + (const P3 &a) const{ return P3(x+a.x, y+a.y, z+a.z); }
  P3 operator - (const P3 &a) const{ return P3(x-a.x, y-a.y, z-a.z); }
  P3 operator * (const double &c) const{ return P3(x*c, y*c, z*c); }
  P3 operator / (const double &c) const{ return P3(x/c, y/c, z/c); }
};

struct L3{
  P3 a,b;
  L3(P3 a=P3(), P3 b=P3()):a(a),b(b){}
};


double abs(P3 a){ return sqrt(a.x*a.x + a.y*a.y + a.z*a.z); }
double dot(P3 a, P3 b){ return a.x*b.x + a.y*b.y + a.z*b.z; }
P3 cross(P3 a, P3 b){
  return P3(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x);
}
P3 normalize(P3 a){
  double len = abs(a);
  return P3(a.x/len, a.y/len, a.z/len);
}

struct Plane{
  double a,b,c,d;

  Plane(P3 p1=P3(), P3 p2=P3(), P3 p3=P3()){
    P3 normal = normalize(cross(p2 - p1, p3 - p2));
    a = normal.x;
    b = normal.y;
    c = normal.z;
    d = dot(p1, normal);
  }

  P3 pl_n(){ return P3(a, b, c); }
};

struct data{
  P3 c, v[2];
};

bool equal(double a, double b){ return fabs(a-b) < EPS;}

bool isParallel(Plane a, Plane b){
  P3 e = cross(a.pl_n(), b.pl_n());
  return equal(e.x, 0.0) && equal(e.y, 0.0) && equal(e.z, 0.0);
}

double distSP(L3 S, P3 p){
  double a = dot(S.b - S.a, S.b - S.a);
  double b = dot(S.b - S.a, S.a - p);
  double c = dot(S.a - p, S.a - p);
  double t = -b / a;
  if(t < -EPS) return abs(S.a - p);
  if(t > 1 + EPS) return abs(S.b - p);
  return a * t * t + 2 * b * t + c;
}

L3 getIntersectLine(Plane a, Plane b){
  P3 e = cross(a.pl_n(), b.pl_n());
  P3 p;

  assert(!isParallel(a, b));
  if(!equal(e.z, 0.0)) {
    p = P3((a.d * b.b - b.d * a.b) / e.z,
           (a.d * b.a - b.d * a.a) / -e.z,
           0.0);
  }
  else if(!equal(e.y, 0.0)){
    p = P3((a.d * b.c - b.d * a.c) / -e.y,
           0.0,
           (a.d * b.a - b.d * a.a) / e.y);
  }
  else {
    p = P3(0.0,
           (a.d * b.c - b.d * a.c) / e.x,
           (a.d * b.b - b.d * a.b) / -e.x);
  }
  return L3(p, p+e);
}



data v[2];

vector<P3> getNearests(L3 line){
  vector<P3> res;

  for(int i=0;i<2;i++){
    P3 le = line.a, p1, p2, ri = line.b;
    double d0, d1, d2;
    while(abs(ri - line.a) - abs(le - line.a) > EPS){
      p1 = (le * 2.0 + ri) / 3.0;
      p2 = (le + ri * 2.0) / 3.0;
      d0 = abs(le - v[i].c);
      d1 = abs(p1 - v[i].c);
      d2 = abs(p2 - v[i].c);
      if(d0 > d1 && d1 > d2) le = p1;
      else ri = p2;
    }
    if(abs((le + ri) / 2.0 - v[i].c) < 1.0 + EPS){
      res.push_back((le + ri) / 2.0);
    }
  }

  return res;
}

vector<P3> getP(L3 line, P3 nearest, int pos){
  vector<P3> res;
  P3 le = line.a, ri = nearest, mid;

  while(abs(ri - line.a) - abs(le - line.a) > EPS){
    mid = (le + ri) / 2.0;
    if(abs(mid - v[pos].c) >= 1.0) le = mid;
    else ri = mid;
  }
  res.push_back((le + ri) / 2.0);

  le = nearest, ri = line.b;
  while(abs(ri - line.a) - abs(le - line.a) > EPS){
    mid = (le + ri) / 2.0;
    if(abs(mid - v[pos].c) >= 1.0) ri = mid;
    else le = mid;
  }
  res.push_back((le + ri) / 2.0);

  if(abs(res[0] - line.a) > abs(res[1] - line.a)) {
    swap(res[0], res[1]);
  }

  return res;
}

bool solve(){
  vector<P3> nearests, p[2];
  L3 line;
  Plane pl[2];

  for(int i=0;i<2;i++){
    pl[i] = Plane(v[i].c, v[i].c + v[i].v[0], v[i].c + v[i].v[1]);
  }

  if(isParallel(pl[0], pl[1])) return false;

  line = getIntersectLine(pl[0], pl[1]);
  line = L3(line.a - (line.b-line.a) * INF, line.a + (line.b-line.a) * INF);

  nearests = getNearests(line);
  if(nearests.size() != 2) return false;

  for(int i=0;i<2;i++){
    p[i] = getP(line, nearests[i], i);
  }

  for(int i=0;i<2;i++){
    int j = 1 - i;
    double d1 = abs(p[i][0] - line.a);
    double d2 = abs(p[j][0] - line.a);
    double d3 = abs(p[i][1] - line.a);
    double d4 = abs(p[j][1] - line.a);
    if(d1 + EPS < d2 && d2 + EPS < d3 && d3 + EPS < d4){
      return true;
    }
  }
  return false;
}

int main(){
  while(cin >> v[0].c.x >> v[0].c.y >> v[0].c.z){
    for(int i=0;i<2;i++){
      if(i > 0) cin >> v[i].c.x >> v[i].c.y >> v[i].c.z;
      for(int j=0;j<2;j++) cin >> v[i].v[j].x >> v[i].v[j].y >> v[i].v[j].z;
    }
    cout << (solve() ? "YES" : "NO") << endl;
  }
}