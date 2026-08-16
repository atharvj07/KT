#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<functional>
 
using namespace std;

/* constant */

const int MAX_N = 100;

const int INF = 1 << 29;

/* typedef */

typedef pair<int,int> pii;
typedef vector<pii> vpii;

typedef double vec[MAX_N];
typedef vec mat[MAX_N];

/* global variables */

int n, st, gl;
bool qs[MAX_N];
int as[MAX_N][MAX_N], bs[MAX_N][MAX_N], idx[MAX_N];
vpii nbrs[MAX_N];

mat mm;
vec vv;

/* subroutines */

void print_matvec(int n, mat& m, vec& v) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) printf(" %9.6lf", m[i][j]);
    printf(" : %9.6lf\n", v[i]);
  }
  putchar('\n');
}

// gauss-jordan
bool solve(int n, mat& m, vec& v) {
  //print_matvec(n, m, v);
  for (int i = 0; i < n; i++) {
    if (m[i][i] == 0.0) {
      for (int i0 = i + 1; i0 < n; i0++)
        if (m[i0][i] != 0.0) {
	  for (int j = i; j < n; j++) swap(m[i][j], m[i0][j]);
	  swap(v[i], v[i0]);
          break;
	}
    }

    double mii = m[i][i];
    if (mii != 0.0) {
      m[i][i] = 1.0;
      for (int j = i + 1; j < n; j++) m[i][j] /= mii;
      v[i] /= mii;
      //printf("mii=%lf, v[%d]=%lf\n", mii, i, v[i]);
      
      for (int i0 = i + 1; i0 < n; i0++) {
	double mii0 = m[i0][i];
        if (mii0 != 0.0) {
          m[i0][i] = 0.0;
	  for (int j = i + 1; j < n; j++)
            m[i0][j] -= mii0 * m[i][j];
          v[i0] -= mii0 * v[i];
	}
      }
    }
  }
  //print_matvec(n, m, v);
  
  for (int i = n - 1; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) v[i] -= m[i][j] * v[j];
    //if (m[i][i] == 0.0 && v[i] != 0.0) return false;
  }
  
  return true;
}

/* main */

int main() {
  for (;;) {
    cin >> n >> st >> gl;
    if (n == 0) break;
    st--, gl--;

    for (int i = 0; i < n; i++) cin >> qs[i];

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) {
	int d;
	cin >> d;
	as[i][j] = (d == 0 && i != j) ? INF : d;
	bs[i][j] = d;
      }

    for (int k = 0; k < n; k++)
      for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++) {
	  int d = as[i][k] + as[k][j];
	  if (as[i][j] > d) as[i][j] = d;
	}

    if (as[st][gl] >= INF) {
      cout << "imposslible" << endl;
      continue;
    }

    int n0 = 0;
    for (int i = 0; i < n; i++)
      idx[i] = (as[st][i] >= INF || as[i][gl] >= INF) ? -1 : n0++;

    for (int i = 0; i < n; i++) {
      int i0 = idx[i];
      if (i0 < 0) continue;

      nbrs[i0].clear();
      for (int j = 0; j < n; j++) {
	int j0 = idx[j];
	if (j0 < 0) continue;

	as[i0][j0] = as[i][j];
	if (bs[i0][j0] > 0) nbrs[i0].push_back(pii(j0, bs[i0][j0]));
      }
    }

    st = idx[st];
    gl = idx[gl];
    n = n0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) mm[i][j] = 0.0;
      mm[i][i] = 1.0;
      vv[i] = 0.0;
      if (i == gl) continue;

      vpii& nbri = nbrs[i];
      
      if (qs[i]) {
	int nn = 0;
	for (vpii::iterator vit = nbri.begin(); vit != nbri.end(); vit++) {
	  int j = vit->first;
	  int d = vit->second;
	  if (as[i][gl] == d + as[j][gl]) {
	    vv[i] += d;
	    mm[i][j] = -1.0;
	    nn++;
	  }
	}
	if (nn > 0) {
	  for (int j = 0; j < n; j++)
	    if (i != j) mm[i][j] /= nn;
	  vv[i] /= nn;
	}
      }
      else {
	int nn = nbri.size();
	if (nn > 0) {
	  for (vpii::iterator vit = nbri.begin(); vit != nbri.end(); vit++) {
	    int j = vit->first;
	    int d = vit->second;
	    vv[i] += d;
	    mm[i][j] = (double)-1.0 / nn;
	  }
	  vv[i] /= nn;
	}
      }
    }

    solve(n, mm, vv);

    printf("%.9lf\n", vv[st]);
  }

  return 0;
}