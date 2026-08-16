#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100100;
int n;
pair<pair<int, int>, bool> ar[2 * MAXN];
int main() {
  ios ::sync_with_stdio(0);
  if (fopen("input.txt", "r")) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  }
  cin >> n;
  for (int i = 0; i < n; i++) {
    int h, l, r;
    cin >> h >> l >> r;
    ar[2 * i] = pair<pair<int, int>, bool>(pair<int, int>(l, h), 0);
    ar[2 * i + 1] = pair<pair<int, int>, bool>(pair<int, int>(r, h), 1);
  }
  sort(ar, ar + 2 * n);
  multiset<int> st;
  vector<pair<int, int> > ans, ans2;
  st.insert(0);
  ans2.push_back(pair<int, int>(ar[0].first.first, 0));
  for (int i = 0; i < 2 * n; i++) {
    if (ar[i].second)
      st.erase(st.find(ar[i].first.second));
    else
      st.insert(ar[i].first.second);
    int h = *st.rbegin();
    ans2.push_back(pair<int, int>(ar[i].first.first, ans2.back().second));
    ans2.push_back(pair<int, int>(ar[i].first.first, h));
  }
  for (int i = 0, j; i < ans2.size(); i = max(i + 1, j - 1)) {
    for (j = i; j < ans2.size() && ans2[j].second == ans2[i].second; j++)
      ;
    ans.push_back(ans2[i]);
  }
  ans2 = ans;
  ans.clear();
  for (int i = 0, j; i < ans2.size(); i = max(i + 1, j - 1)) {
    for (j = i; j < ans2.size() && ans2[j].first == ans2[i].first; j++)
      ;
    ans.push_back(ans2[i]);
  }
  cout << ans.size() << '\n';
  for (int i = 0; i < ans.size(); i++)
    cout << ans[i].first << ' ' << ans[i].second << '\n';
  return 0;
}
