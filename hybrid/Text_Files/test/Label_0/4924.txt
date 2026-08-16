#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < (int)(j); ++i)
#define FOR(i, j, k) for(int i = (int)(j); i < (int)(k); ++i)
#define SORT(v) sort((v).begin(), (v).end())
#define REVERSE(v) reverse((v).begin(), (v).end())
typedef complex<double> P;

int check(vector<int> &v, int N, int K){
  int res = 0;
  REP(i, N - K + 1){
    int tmp = v[i];
    FOR(j, 1, K) tmp *= v[i + j];
    res = max(res, tmp);
  }
  return res;
}

int main() {
  int N, K;
  while(cin >>N >>K && N){
    vector<int> v(N);
    REP(i, N) cin >>v[i];
    int bef = check(v, N, K), ans = -1;
    REP(i, N){
      FOR(j, i + 1, N){
        swap(v[i], v[j]);
        int tmp = check(v, N, K);
        if(tmp - bef >= 0) ans = max(ans, tmp - bef);
        swap(v[i], v[j]);
      }
    }
    if(ans == -1) cout <<"NO GAME" <<endl;
    else cout <<ans <<endl;
  }

  return 0;
}