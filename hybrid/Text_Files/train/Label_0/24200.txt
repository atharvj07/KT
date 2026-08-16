#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<pair<int, int> > T;
  std::ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, s;
  cin >> n >> s;
  for (int i = 0; i < n; i++) {
    int x, x1;
    cin >> x >> x1;
    T.push_back(make_pair(x, x1));
  }
  if ((T[0].first * 60 + T[0].second) > s) {
    cout << "0 0";
    return 0;
  }
  for (int i = 0; i < n - 1; i++) {
    if (((T[i + 1].first * 60 + T[i + 1].second) -
         (T[i].first * 60 + 1 + T[i].second)) > s * 2) {
      ;
      cout << (T[i].first * 60 + 1 + T[i].second + s) / 60 << " "
           << (T[i].first * 60 + 1 + T[i].second + s) % 60;
      return 0;
    }
  }
  cout << (T[n - 1].first * 60 + T[n - 1].second + 1 + s) / 60 << " "
       << (T[n - 1].first * 60 + T[n - 1].second + 1 + s) % 60;
  return 0;
}
