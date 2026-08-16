#include <bits/stdc++.h>
using namespace std;
const int MAX = 200009;
int n, k;
int x, y;
int tree[4 * MAX], lazy[4 * MAX];
vector<pair<pair<int, int>, int> > v;
vector<int> ans;
void update(int low, int high, int pos) {
  if (lazy[pos] != 0) {
    tree[pos] += lazy[pos];
    if (low != high) {
      lazy[2 * pos] += lazy[pos];
      lazy[2 * pos + 1] += lazy[pos];
    }
    lazy[pos] = 0;
  }
  if (x > high || y < low) {
    return;
  }
  if (x <= low && y >= high) {
    tree[pos]++;
    if (low != high) {
      lazy[2 * pos]++;
      lazy[2 * pos + 1]++;
    }
    return;
  }
  int mid = (low + high) >> 1;
  update(low, mid, 2 * pos);
  update(mid + 1, high, 2 * pos + 1);
  tree[pos] = max(tree[2 * pos], tree[2 * pos + 1]);
}
int qwr(int low, int high, int pos) {
  if (lazy[pos] != 0) {
    tree[pos] += lazy[pos];
    if (low != high) {
      lazy[2 * pos] += lazy[pos];
      lazy[2 * pos + 1] += lazy[pos];
    }
    lazy[pos] = 0;
  }
  if (x > high || y < low) {
    return 0;
  }
  if (x <= low && y >= high) {
    return tree[pos];
  }
  int mid = (low + high) >> 1;
  int x = qwr(low, mid, 2 * pos);
  int y = qwr(mid + 1, high, 2 * pos + 1);
  tree[pos] = max(tree[2 * pos], tree[2 * pos + 1]);
  return max(x, y);
}
bool cmp(const pair<pair<int, int>, int>& p1,
         const pair<pair<int, int>, int>& p2) {
  if (p1.first.second != p2.first.second) {
    return p1.first.second < p2.first.second;
  }
  return p1.first.first < p2.first.first;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    int l, r;
    cin >> l >> r;
    v.push_back({{l, r}, i});
  }
  sort(v.begin(), v.end(), cmp);
  for (int i = 0; i < v.size(); i++) {
    x = v[i].first.first;
    y = v[i].first.second;
    int mx = qwr(1, 200000, 1);
    if (mx == k) {
      ans.push_back(v[i].second);
    } else {
      update(1, 200000, 1);
    }
  }
  cout << (int)ans.size() << "\n";
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i] << " ";
  }
  return 0;
}
