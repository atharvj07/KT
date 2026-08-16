#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:60777216")
using namespace std;
int n, m;
int a[222222];
int k[222222];
int pos[222222];
int w[222222];
vector<int> z[222222];
int s[1 << 20];
void addOne(int pos) {
  pos += (1 << 19);
  while (pos) {
    s[pos]++;
    pos >>= 1;
  }
}
int solve(int pos) {
  int start = 1;
  while (start < (1 << 19)) {
    if (s[start * 2] >= pos)
      start *= 2;
    else {
      pos -= s[start * 2];
      start = start * 2 + 1;
    }
  }
  return start - (1 << 19);
}
int main() {
  cin >> n;
  for (int i = (0); i < (n); i++) scanf("%d", a + i);
  cin >> m;
  for (int i = (0); i < (m); i++)
    scanf("%d %d", k + i, pos + i), z[k[i]].push_back(i);
  vector<pair<int, int> > v;
  for (int i = (0); i < (n); i++) v.push_back(pair<int, int>(a[i], -i));
  sort((v).begin(), (v).end());
  reverse(v.begin(), v.end());
  for (int i = (0); i < (v.size()); i++) {
    int p = -v[i].second;
    addOne(p);
    for (int j = (0); j < (z[i + 1].size()); j++) {
      int id = z[i + 1][j];
      int pp = pos[id];
      w[id] = a[solve(pp)];
    }
  }
  for (int i = (0); i < (m); i++) printf("%d\n", w[i]);
  return 0;
}
