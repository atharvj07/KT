#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
struct unit {
  int c, s;
  unit() {}
  unit(int c, int s) : c(c), s(s) {}
};
int n, cnt = 1, to, len, ind[N];
map<int, int> u;
unit a[N];
vector<pair<long long, int> > t[N], tmp[N], b[N];
vector<int> res;
bool cmp_costs(pair<long long, int> a, pair<long long, int> b) {
  return a.first > b.first;
}
bool cmp_sizes(int x, int y) { return t[x].size() > t[y].size(); }
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &a[i].c, &a[i].s);
    if (!u[a[i].c])
      to = u[a[i].c] = cnt++;
    else
      to = u[a[i].c];
    t[to].push_back(make_pair(a[i].s, i));
  }
  cnt--;
  for (int i = 1; i <= cnt; i++) sort(t[i].begin(), t[i].end(), cmp_costs);
  for (int i = 1; i <= cnt; i++) {
    len = max(len, (int)t[i].size());
    for (int j = 0; j < (int)t[i].size(); j++) {
      t[i][j].first += (j > 0 ? t[i][j - 1].first : 0);
      b[j].push_back(make_pair(t[i][j].first, i));
    }
  }
  for (int i = 0; i < len; i++) sort(b[i].begin(), b[i].end(), cmp_costs);
  long long ans = 0;
  int pos1, pos2, h1, h2;
  for (int i = 0; i < len; i++) {
    if (b[i].size() < 2) break;
    if (ans < b[i][0].first + b[i][1].first) {
      ans = b[i][0].first + b[i][1].first;
      pos1 = pos2 = i;
      h1 = b[i][0].second;
      h2 = b[i][1].second;
    }
    if (i + 1 < len && b[i + 1].size() > 0) {
      if (b[i][0].second != b[i + 1][0].second) {
        if (ans < b[i][0].first + b[i + 1][0].first) {
          ans = b[i][0].first + b[i + 1][0].first;
          pos1 = i;
          pos2 = i + 1;
          h1 = b[i][0].second;
          h2 = b[i + 1][0].second;
        }
      }
      if (b[i][1].second != b[i + 1][0].second) {
        if (ans < b[i][1].first + b[i + 1][0].first) {
          ans = b[i][1].first + b[i + 1][0].first;
          pos1 = i;
          pos2 = i + 1;
          h1 = b[i][1].second;
          h2 = b[i + 1][0].second;
        }
      }
      if (b[i + 1].size() > 1) {
        if (b[i][0].second != b[i + 1][1].second) {
          if (ans < b[i][0].first + b[i + 1][1].first) {
            ans = b[i][0].first + b[i + 1][1].first;
            pos1 = i;
            pos2 = i + 1;
            h1 = b[i][0].second;
            h2 = b[i + 1][1].second;
          }
        }
        if (b[i][1].second != b[i + 1][1].second) {
          if (ans < b[i][1].first + b[i + 1][1].first) {
            ans = b[i][1].first + b[i + 1][1].first;
            pos1 = i;
            pos2 = i + 1;
            h1 = b[i][1].second;
            h2 = b[i + 1][1].second;
          }
        }
      }
    }
  }
  if (pos1 >= pos2) {
    for (int i = 0; i <= pos2; i++) {
      res.push_back(t[h1][i].second);
      res.push_back(t[h2][i].second);
    }
    if (pos1 > pos2) res.push_back(t[h1][pos1].second);
  } else {
    for (int i = 0; i <= pos1; i++) {
      res.push_back(t[h2][i].second);
      res.push_back(t[h1][i].second);
    }
    res.push_back(t[h2][pos2].second);
  }
  cout << ans << endl << res.size() << endl;
  for (int i = 0; i < (int)res.size(); i++) cout << res[i] + 1 << " ";
  return 0;
}
