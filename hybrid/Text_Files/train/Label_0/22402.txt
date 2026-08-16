#include <iostream>
#include <complex>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;
typedef complex<double> P;
typedef pair<P,P> L;
typedef pair<P,double> C;
typedef vector<P> Poly;
#define X real()
#define Y imag()
const double EPS = (1e-10);
const double INF = (1e15);

//2D version
namespace std{
  bool operator < (const P& a, const P& b){
    return a.X != b.X ? a.X < b.X : a.Y < b.Y;
  }
  bool cmp_y(const P &a, const P &b){
    return a.Y != b.Y ? a.Y < b.Y : a.X < b.X;
  }
  bool operator == (const P& a, const P& b){
    return abs(a-b) < EPS;
  }
}
double dot(P a, P b){
  return a.X * b.X + a.Y * b.Y;
}
double cross(P a, P b){
  return a.X * b.Y - a.Y * b.X;
}
P intersection(L a, L b){
  //直線aと直線bの交点
  P af = a.first, as = a.second, bf = b.first, bs = b.second;
  return af + cross(bs-bf,af-bf)/(-cross(bs-bf,as-bf)+cross(bs-bf,af-bf))*(as-af);
}

int ccw(P a, P b, P c) {
  b -= a; c -= a;
  if(cross(b,c) > EPS) return +1;
  if(cross(b,c) < -EPS) return -1;
  if(dot(b,c) < 0) return +2;
  if(abs(b) + EPS < abs(c)) return -2;
  return 0;
}

Poly convex_cut(Poly p, L l){
  Poly ret;
  int n = p.size();
  for(int i = 0; i < n; ++i){
    if(ccw(l.first, l.second, p[i]) != -1)
      ret.push_back(p[i]);
    if(ccw(l.first, l.second, p[i]) != -1 ^
       ccw(l.first, l.second, p[(i+1)%n]) != -1)
      ret.push_back(intersection(L(p[i], p[(i+1)%n]), l));
  }
  return ret;
}

int main(){
  int N;
  cin >> N;
  Poly Po;
  for(int i = 0; i < N; ++i){
    double x,y;
    cin >> x >> y;
    Po.emplace_back(x,y);
  }
  int M;
  cin >> M;
  Poly C;
  for(int i = 0; i < M; ++i){
    double x,y;
    cin >> x >> y;
    C.emplace_back(x,y);
  }
  double ans = 0;
  for(int i = 0; i < M; ++i){
    Poly Q = Po;
    for(int j = 0; j < M; ++j){
      if(j == i) continue;
      P m = (C[i]+C[j])/2.0;
      Q = convex_cut(Q,L(m,m+(C[j]-C[i])*P(0,1)));
    }
    for(size_t j = 0; j < Q.size(); ++j){
      ans = max(ans, abs(Q[j]-C[i]));
    }
  }
  printf("%.12f\n",ans);
  return 0;
}

