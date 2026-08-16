#include <bits/stdc++.h>

using namespace std;

const int SIZE = 210;
const double eps = 1e-10;

typedef complex<double> P;

inline double dot(P a, P b){
  return (a * conj(b)).real();
}

inline double cross(P a, P b){
  return (conj(a) * b).imag();
}

int ccw(P a, P b, P c){
  double res1 = cross(b-a, c-a);
  if(res1 > eps) return 1;
  if(res1 < -eps) return -1;
  if(dot(b-a, c-a) < -eps) return -2;
  if(dot(a-b, c-b) < -eps) return 2;
  return 0;
}

bool iscollinear(P a1, P a2, P b1, P b2){
  return abs(cross(a2-a1, b2-b1)) < eps;
}

int isInterSS(P a1, P a2, P b1, P b2){
  if(iscollinear(a1, a2, b1, b2)) return false;
  
  int a = ccw(b1, b2, a1);
  int b = ccw(b1, b2, a2);
  int c = ccw(a1, a2, b1);
  int d = ccw(a1, a2, b2);

  if(a*b <= 0 && c*d < 0) return 1;
  if(a*b <= 0 && c == 0) return -1;
  if(a*b <= 0 && d == 0) return -2;
  return 0;
}

int isInterLS(P a1, P a2, P b1, P b2){
  if(iscollinear(a1, a2, b1, b2)) return false;

  int c = ccw(a1, a2, b1);
  int d = ccw(a1, a2, b2);
  
  if(c == 0) return -1;
  if(d == 0) return -2;
  if(c*d < 0) return 1;
  return 0;
}

bool iscontainedPP(int n, P *g, P p){
  bool f = false;
  for(int i=0;i<n;i++){
    P a = g[i] -p, b = g[(i+1)%n] - p;
    if(abs(cross(a,b)) < eps && dot(a,b) < eps) return true;
    if(a.imag() > b.imag()) swap(a,b);
    if(a.imag() < eps && eps < b.imag() && cross(a,b) > eps) f = !f;
  }
  return f;
}

P getCrossPoint(P a1, P a2, P b1, P b2){
  P a = a2 - a1;
  P b = b2 - b1;
  return a1 + a * cross(b, b1-a1) / cross(b, a);
}

int T = 0;

bool solve(){
  int n;
  int x[SIZE], y[SIZE];
  P p[SIZE];
  
  if(scanf("%d",&n) == EOF) return false;
  if(n == 0) return false;

  printf("Case %d: ",++T);
  
  for(int i=0;i<n;i++){
    scanf("%d%d",x+i, y+i);
    p[i] = P(x[i], y[i]);
  }

  bool inS[SIZE][SIZE][2][2] = {}; // [a][b][{a:0,b:1}][0:in,1:out}]
  
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      auto dir = (p[j] - p[i]); //i->j
      double e = 1e10;
      if (abs(dir.imag()) > eps) e = min(e, abs(dir.imag()));
      if (abs(dir.real()) > eps) e = min(e, abs(dir.real()));
      dir = dir / e * 1e-7;

      inS[i][j][0][0] = iscontainedPP(n, p, p[i] + dir);
      inS[i][j][0][1] = iscontainedPP(n, p, p[i] - dir);
      inS[i][j][1][0] = iscontainedPP(n, p, p[j] - dir);
      inS[i][j][1][1] = iscontainedPP(n, p, p[j] + dir);
      inS[j][i][0][0] = inS[j][i][1][0];
      inS[j][i][0][1] = inS[j][i][1][1];
      inS[j][i][1][0] = inS[j][i][0][0];
      inS[j][i][1][1] = inS[j][i][0][1];
    }
  }

  double ans = 0;

  for(int i=0;i<n;i++){
    ans = max(ans,abs(p[i] - p[(i+1)%n]));
  }
  
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      bool f = true;

      if (i+1 != j){
        for(int k=0;k<n;k++){
          if(k == i || (k+1)%n == i || k == j || (k+1)%n == j) continue;

          int resISS = isInterSS(p[i], p[j], p[k], p[(k+1)%n]);
          
          if(resISS == 1 ||
             (resISS == -1 && (!inS[i][k][1][1] || !inS[i][k][1][0])) ||
             (resISS == -2 && (!inS[i][(k+1)%n][1][1] || !inS[i][(k+1)%n][1][0]))){
            f = false;
            break;
          }
        }

        if (!f) continue;
      }
      
      P cp1, cp2;
      bool cp1f = false, cp2f = false;
      
      for(int k=0;k<n;k++){
        if(k == i || (k+1)%n == i || k == j || (k+1)%n == j) continue;
        
        int resILS = isInterLS(p[i], p[j], p[k], p[(k+1)%n]);
        P cp = getCrossPoint(p[i], p[j], p[k], p[(k+1)%n]);
        
        if(resILS){
          bool near1 = false;
          bool near2 = false;
          
          if(abs(p[i] - cp) < abs(p[j] - cp)){
            if (!cp1f || abs(p[i] - cp) < abs(p[i] - cp1)){
              if(resILS == 1 ||
                 (resILS == -1 && !inS[i][k][1][1]) ||
                 (resILS == -2 && !inS[i][(k+1)%n][1][1]))
                near1 = true;
            }
          }else{
            if (!cp2f || abs(p[j] - cp) < abs(p[j] - cp2)){
              if(resILS == 1 ||
                 (resILS == -1 && !inS[j][k][1][1]) ||
                 (resILS == -2 && !inS[j][(k+1)%n][1][1]))
                near2 = true;
            }
          }
          
          if(near1){
            cp1 = cp; cp1f = true;
          }
          
          if(near2){
            cp2 = cp; cp2f = true;
          }
        }

        //cerr << i << " " << j << " " << k << " : " << resILS << endl;
      }

      
      if(inS[i][j][0][0]){
        ans = max(ans, abs(p[i] - p[j]));
      } else {
        continue;
      }

      //1
      
      if (cp1f && inS[i][j][0][1]){
        ans = max(ans, abs(p[j] - cp1));
      }
      
      //2
      if (cp2f && inS[i][j][1][1]) {
        ans = max(ans, abs(cp2 - p[i]));
        if(cp1f && inS[i][j][0][1])
          ans = max(ans, abs(cp1-cp2));
      }

      //cerr << i << " " << j << " : " << ans << endl;
    }
  }

  printf("%.10lf\n",ans);
  
  return true;
}
  

int main(){
  //while(solve());

  for(int i=0;;i++){
    if(!solve()) break;
  }
  return 0;
}

