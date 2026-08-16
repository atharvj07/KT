#include <bits/stdc++.h>
using namespace std;
int n, c[200], v[200], ans = 123456;
bool visc[200], visv[200];
char setc[] = {'R', 'G', 'B', 'Y', 'W'};
map<char, int> mp;
set<pair<int, int> > ss;
int main() {
  scanf("%d", &n);
  for (int i = 0; i < 5; i++) mp[setc[i]] = i;
  for (int i = 0; i < n; i++) {
    char a, b;
    scanf(" %c %c", &a, &b);
    int aa = mp[a];
    int ab = b - '0' - 1;
    ss.insert(make_pair(aa, ab));
  }
  n = 0;
  for (set<pair<int, int> >::iterator it = ss.begin(); it != ss.end(); it++) {
    pair<int, int> pa = *it;
    c[n] = pa.first;
    v[n] = pa.second;
    ++n;
  }
  for (int mc = 0; mc < (1 << 5); mc++) {
    for (int mv = 0; mv < (1 << 5); mv++) {
      memset(visc, false, sizeof visc);
      memset(visv, false, sizeof visv);
      for (int i = 0; i < 5; i++) {
        if ((mc & (1 << i)) == 0) continue;
        for (int j = 0; j < n; j++)
          if (c[j] == i) visc[j] |= true;
      }
      for (int i = 0; i < 5; i++) {
        if ((mv & (1 << i)) == 0) continue;
        for (int j = 0; j < n; j++)
          if (v[j] == i) visv[j] |= true;
      }
      while (true) {
        bool go = false;
        set<int> cc;
        set<int> cv;
        for (int i = 0; i < n; i++) {
          if (!visc[i]) cc.insert(c[i]);
          if (!visv[i]) cv.insert(v[i]);
        }
        if ((int)cc.size() == 1) {
          for (int i = 0; i < n; i++)
            if (!visc[i]) visc[i] |= true;
          go = true;
        }
        if ((int)cv.size() == 1) {
          for (int i = 0; i < n; i++)
            if (!visv[i]) visv[i] |= true;
          go = true;
        }
        for (int ic = 0; ic < 5; ic++) {
          set<int> vv;
          for (int i = 0; i < n; i++)
            if (c[i] == ic && !visv[i]) vv.insert(v[i]);
          if ((int)vv.size() != 1) continue;
          int val = *vv.begin();
          for (int i = 0; i < n; i++) {
            if (c[i] == ic && visc[i] && !visv[i]) {
              visv[i] = go = true;
            }
          }
        }
        for (int iv = 0; iv < 5; iv++) {
          set<int> vv;
          for (int i = 0; i < n; i++)
            if (v[i] == iv && !visc[i]) vv.insert(c[i]);
          if ((int)vv.size() != 1) continue;
          int val = *vv.begin();
          for (int i = 0; i < n; i++) {
            if (v[i] == iv && visv[i] && !visc[i]) {
              visc[i] = go = true;
            }
          }
        }
        if (!go) break;
      }
      bool ok = true;
      for (int i = 0; i < n; i++) {
        ok &= visc[i];
        ok &= visv[i];
      }
      int b = __builtin_popcount(mc) + __builtin_popcount(mv);
      if (ok) ans = min(ans, b);
    }
  }
  printf("%d\n", ans);
  return 0;
}
