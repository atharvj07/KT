#include<iostream>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<cmath>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)
#define REP(i,b,n) for(int i=b;i<n;i++)

typedef long double D;
typedef pair<D, D> P;

#define sq(x) ((x) * (x))
typedef vector<D> Vector;
typedef vector<Vector> Matrix;
 
const D EPS = 1e-8;

Vector gauss_jordan(const Matrix &A, const Vector &b){
  int n = A.size();
  Matrix B(n, Vector(n+1));
  rep(i, n){
    rep(j, n){
      B[i][j] = A[i][j];
    }
  }
 
  rep(i, n){
    B[i][n] = b[i];
  }
 
  rep(i, n){
    int pivot = i;
    REP(j, i, n){
      if(abs(B[j][i]) > abs(B[pivot][i])){
	pivot = j;
      }
    }
 
    swap(B[i], B[pivot]);
 
    if(abs(B[i][i]) < EPS)return Vector();
 
    REP(j, i+1, n+1)B[i][j] /= B[i][i];
    rep(j, n){
      if(i != j){
	REP(k, i+1, n+1){
	  B[j][k] -= B[j][i] * B[i][k];
	}
      }
    }
  }
 
  Vector x(n);
  rep(i, n)x[i] = B[i][n];
  return x;
}

int main() {
  int n;
  cin >> n;
  vector<P> vp(n);
  rep (i, n) cin >> vp[i].first >> vp[i].second;
  Matrix M;
  rep (i, 3) {
    Vector V(3);
    M.push_back(V);
  }
  Vector V(3);
  rep (i, n) {
    M[0][0] += 2 * vp[i].first * vp[i].first;
    M[0][1] += 2 * vp[i].first * vp[i].second;
    M[0][2] += 2 * vp[i].first;
    V[0] -= 2 * vp[i].first * (sq(vp[i].first) + sq(vp[i].second));
    M[1][0] += 2 * vp[i].second * vp[i].first;
    M[1][1] += 2 * vp[i].second * vp[i].second;
    M[1][2] += 2 * vp[i].second;
    V[1] -= 2 * vp[i].second * (sq(vp[i].first) + sq(vp[i].second));
    M[2][0] += 2 * vp[i].first;
    M[2][1] += 2 * vp[i].second;
    M[2][2] += 2;
    V[2] -= 2 * (sq(vp[i].first) + sq(vp[i].second));
  }
  V = gauss_jordan(M, V);
  printf("%.12Lf %.12Lf %.12Lf\n", V[0], V[1], V[2]);
  return 0;
}