#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int MAX_R = 128;
const int MAX_C = 16+1;
const int BIT = 1<<MAX_C;

int r, c;
string s[MAX_R];
int dp[2][BIT];

int main() {
  while(1) {
    if(cin >> r >> c) ; else break;
    for(int i = 0; i < r; ++i) cin >> s[i];

    int p = 0;

    fill(dp[0], dp[2], -1);
    for(int k = 0; k < (1<<c); ++k) {
      if(__builtin_popcount(k) != s[0].size()) continue;
      string tmp = "";
      for(int i = 0, a = 0; i < c; ++i) {
        if(k&(1<<i)) tmp += s[0][a++];
        else tmp += '.';
      }
      dp[p][k] = 0;
      for(int i = 1; i < tmp.size(); ++i) {
        if(tmp[i] != '.' && tmp[i-1] == tmp[i]) {
          dp[p][k] += 2;
        }
      }
    }

    for(int i = 1; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
        int q = 1-p;
        for(int k = 0; k < (1<<c); ++k) dp[q][k] = -1;
        for(int k = 0; k < (1<<c); ++k) {
          if(dp[p][k] == -1) continue;
          int Lu = c - j;
          char u, l;
          int use;
          u = l = '.';
          for(int t = Lu-1, a = (int)s[i-1].size()-1; t >= 0; --t) {
            if(k&(1<<t)) u = s[i-1][a--];
            else u = '.';
          }
          use = 0;
          for(int t = Lu; t < c; ++t) {
            if(k&(1<<t)) l = s[i][use++];
            else l = '.';
          }

          if(use + (c-j) < s[i].size()) continue;

          // space
          {
            int nk = k/2;
            if(j+1 == c && __builtin_popcount(nk) != s[i].size()); else {
              dp[q][nk] = max(dp[q][nk], dp[p][k]);
            }
          }

          // char
          if(use < s[i].size()) {
            int nk = k/2 + (1<<(c-1));
            int add = 0;
            add += (s[i][use] == u) * 2;
            add += (s[i][use] == l) * 2;
            if(j+1 == c && __builtin_popcount(nk) != s[i].size()); else {
              dp[q][nk] = max(dp[q][nk], dp[p][k] + add);
            }
          }
        }
        p = q;
      }
    }

    int res = 0;
    for(int k = 0; k < (1<<c); ++k) {
      res = max(res, dp[p][k]);
    }
    cout << res << endl;
  }
  return 0;
}