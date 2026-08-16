

#include "bits/stdc++.h"
#include<unordered_map>
#pragma warning(disable:4996)
using namespace std;

double eps = 1e-9;
int main() {
  int A; cin >> A;
  while (A--) {
    int N; cin >> N;
    vector<int>as;
    for (int i = 0; i < N; ++i) {
      int a; cin >> a;
      as.push_back(a);
    }
    sort(as.begin(), as.end());
    int Q; cin >> Q;
    for (int t = 0; t< Q; ++t) {
      int x, v; cin >> x >> v;
      double stoptime = double(v) / as.back();
      if (x + eps < stoptime*v / 2) {
        cout << "crash" << endl;
      }
      else {
        bool dp[201][101];
        memset(dp, false, sizeof(dp));
        dp[2 * x][v] = true;
        for (int i = 2 * x; i >0; --i) {
          for (int j = 1; j <= v; ++j) {
            if (dp[i][j]) {
              for (int k = 0; k < as.size(); ++k) {
                int nextspeed = j - as[k];
                if (nextspeed >= 0) {
                  if (i - j - nextspeed >= 0) {
                    dp[i - j - nextspeed][nextspeed] = true;
                  }
                }
              }
            }
            
          }
        }
        int dis = 9999;
        for (int i = 0; i <= 2 * x; ++i) {
          if (dp[i][0]) {
            dis = min(dis, i);
          }
        }
        if (dis == 9999) {
          cout << "try again" << endl;
        }
        else if (dis > 0) {
          cout << setprecision(3) << fixed << "good ";
          printf("%.3f", double(dis)/2);
          cout << endl;
        } 
        else {
          cout << "perfect" << endl;
        }
      }
    }
    if (A)cout << endl;
  }
  
  return 0;
}