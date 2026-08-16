#include <bits/stdc++.h>
using namespace std;
const int maxn = 5001;
long long x11[10];
long long y11[10];
long long x22[10];
long long y22[10];
long long deltax[10];
long long deltay[10];
int main() {
  bool flag1 = 0;
  bool flag2 = 0;
  bool flag3 = 0;
  for (int i = 0; i < 4; i++) {
    scanf("%lld %lld %lld %lld", &x11[i], &y11[i], &x22[i], &y22[i]);
    if (x11[i] == x22[i] && y11[i] == y22[i]) flag3 = 1;
    deltax[i] = x11[i] - x22[i];
    deltay[i] = y11[i] - y22[i];
    if (deltax[i] == 0) flag1 = 1;
    if (deltay[i] == 0) flag2 = 1;
  }
  if (!flag1 || !flag2 || flag3) {
    printf("NO\n");
    return 0;
  }
  for (int i = 0; i < 4; i++) {
    if (deltax[i] != 0 && deltay[i] != 0) {
      printf("NO\n");
      return 0;
    }
  }
  vector<long long> vx;
  vector<long long> vy;
  map<long long, int> mp1;
  map<long long, int> mp2;
  for (int i = 0; i < 4; i++) {
    vx.push_back(x11[i]);
    vx.push_back(x22[i]);
    vy.push_back(y11[i]);
    vy.push_back(y22[i]);
    mp1[x11[i]]++;
    mp1[x22[i]]++;
    mp2[y11[i]]++;
    mp2[y22[i]]++;
  }
  if (mp1.size() != 2 || mp2.size() != 2) {
    printf("NO\n");
  } else {
    bool tempflag = 0;
    for (auto it : mp1) {
      if (it.second != 4) tempflag = 1;
    }
    for (auto it : mp2) {
      if (it.second != 4) tempflag = 1;
    }
    if (!tempflag)
      printf("YES\n");
    else
      printf("NO\n");
  }
  return 0;
}
