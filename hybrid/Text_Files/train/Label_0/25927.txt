#include <bits/stdc++.h>
using namespace std;
pair<int, int> v[100100];
vector<int> good;
vector<int> bad;
int isgood[100100];
int isbad[100100];
vector<pair<int, int> > ponto[100100];
vector<int> t[100100];
int has[1010][100100 / 8];
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    int x, y;
    scanf("%d%d", &x, &y);
    v[i] = pair<int, int>(x, y);
    t[x].push_back(y);
    ponto[x].push_back(pair<int, int>(x, y));
  }
  bool b = (v[0].first == 1);
  for (int i = 0; i < 100100; i++) sort(t[i].begin(), t[i].end());
  sort(v, v + n);
  int cur = 1;
  for (int i = 1; i < n; i++) {
    if (v[i].first == v[i - 1].first) {
      cur++;
      continue;
    }
    if (cur <= 100)
      good.push_back(v[i - 1].first), isgood[v[i - 1].first] = 1;
    else
      bad.push_back(v[i - 1].first), isbad[v[i - 1].first] = 1;
    cur = 1;
  }
  if (cur <= 100)
    good.push_back(v[n - 1].first), isgood[v[n - 1].first] = 1;
  else
    bad.push_back(v[n - 1].first), isbad[v[n - 1].first] = 1;
  long long ans = 0;
  int p = 0;
  while (p < n) {
    ;
    while (p < n && isbad[v[p].first]) p++;
    if (p == n) continue;
    int A = p;
    int B = A;
    while (B < n && v[B].first == v[A].first) B++;
    B--;
    ;
    p = B + 1;
    for (int i = A; i <= B; i++)
      for (int j = i + 1; j <= B; j++) {
        int dx = v[j].second - v[i].second;
        assert(v[i].first == v[j].first);
        if (binary_search(t[v[i].first + dx].begin(), t[v[i].first + dx].end(),
                          v[i].second) &&
            binary_search(t[v[j].first + dx].begin(), t[v[j].first + dx].end(),
                          v[j].second))
          ans++;
        if (v[i].first >= dx)
          if (isbad[v[i].first - dx])
            if (binary_search(t[v[i].first - dx].begin(),
                              t[v[i].first - dx].end(), v[i].second) &&
                binary_search(t[v[j].first - dx].begin(),
                              t[v[j].first - dx].end(), v[j].second))
              ans++;
      }
  }
  int x = 0, y = 0;
  for (vector<int>::iterator it = bad.begin(); it < bad.end(); it++, x++)
    for (vector<pair<int, int> >::iterator it2 = ponto[*it].begin();
         it2 < ponto[*it].end(); it2++)
      has[x][(it2->second) / 8] |= (1 << ((it2->second) % 8));
  x = y = 0;
  for (vector<int>::iterator it = bad.begin(); it < bad.end(); it++, x++)
    for (vector<pair<int, int> >::iterator pt = ponto[*it].begin();
         pt < ponto[*it].end(); pt++) {
      y = x + 1;
      for (vector<int>::iterator it2 = it + 1; it2 < bad.end(); it2++, y++) {
        int X = (*pt).first;
        int Y = (*pt).second;
        int dx = (*it2) - (*it);
        if ((has[x][(Y + dx) / 8] & (1 << ((Y + dx) % 8))) &&
            (has[y][(Y) / 8] & (1 << ((Y) % 8))) &&
            (has[y][(Y + dx) / 8] & (1 << ((Y + dx) % 8))))
          ans++;
      }
    }
  printf("%I64d\n", ans);
}
