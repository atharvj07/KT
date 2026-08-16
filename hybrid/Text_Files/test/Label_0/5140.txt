#include <bits/stdc++.h>
using namespace std;
const int MX = 25;
int ans[1 << 20];
int main(int argc, char *argv[]) {
  int n;
  cin >> n;
  int val;
  int last[20];
  for (int i = (0), _b = (20); i < (_b); ++i) last[i] = -1;
  for (int i = (0), _b = (n); i < (_b); ++i) {
    cin >> val;
    if (!val) {
      ans[0] = 1;
      continue;
    }
    for (int j = (0), _b = (20); j < (_b); ++j)
      if ((1 << j) & val) last[j] = i;
    vector<pair<int, int> > v;
    for (int j = (0), _b = (20); j < (_b); ++j)
      if (last[j] != -1) v.push_back(make_pair(last[j], j));
    sort((v).begin(), (v).end());
    int x = 0;
    for (int j = v.size() - 1; j >= 0;) {
      int k = j;
      while (k >= 0 && v[k].first == v[j].first) x |= 1 << v[k--].second;
      ans[x] = 1;
      j = k;
    }
  }
  int cnt = 0;
  for (int i = (0), _b = (1 << 20); i < (_b); ++i) cnt += ans[i];
  cout << cnt << endl;
  return 0;
}
