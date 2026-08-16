#include <algorithm>
#include <complex>
#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;
#define X real()
#define Y imag()
#define EPS (1e-10)
typedef complex<double> P;
typedef pair<P, P> L;

namespace std{
  bool operator<(const P& a, const P& b){
    return a.X != b.X ? a.X < b.X : a.Y < b.Y;
  }
}

double dot(P a, P b){
  return a.X*b.X + a.Y*b.Y;
}

double cross(P a, P b){
  return a.X*b.Y - a.Y*b.X;
}

P projection(P a, P b){
  return dot(a, b)/abs(b)/abs(b)*b;
}

int ccw(P a, P b, P c){
  if(cross(b-a,c-a) > EPS) return 1;
  if(cross(b-a,c-a) < -EPS) return -1;
  if(dot(b-a,c-a) < -EPS) return 2;
  if(abs(b-a) < abs(c-a) - EPS) return -2;
  return 0;
}

bool is_cross(L a, L b){
  if(ccw(a.first,a.second,b.first)*ccw(a.first,a.second,b.second) <= 0 &&
     ccw(b.first,b.second,a.first)*ccw(b.first,b.second,a.second) <= 0) return true;
  return false;
}

P intersection(L a, L b){
  //テ、ツコツ、テァツつケ
  return a.first + abs(cross(b.second-b.first,a.first-b.first)/(abs(cross(b.second-b.first,a.second-b.first))+abs(cross(b.second-b.first,a.first-b.first))))*(a.second-a.first);;
}

int main(){
  int n;
  while(cin >> n, n){
    vector<L> s;
    double x1, y1, x2, y2;
    for(int i = 0; i < n; ++i){
      cin >> x1 >> y1 >> x2 >> y2;
      s.push_back(L(P(x1,y1), P(x2,y2)));
    }
    int ans = 1;
    for(int i = 0; i < n; ++i){
      L si = s[i];
      vector<P> cp;
      cp.push_back(si.first);
      cp.push_back(si.second);
      for(int j = 0; j < i; ++j){
	if(is_cross(si,s[j]))
	  cp.push_back(intersection(si,s[j]));
      }
      sort(cp.begin(), cp.end());
      for(int j = 1; j < cp.size(); ++j)
	if(abs(cp[j-1]-cp[j]) > EPS) ++ans;
    }
    cout << ans << endl;
  }
  return 0;
}