#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int i, n, k;
  vector<pair<string, string> > vec;
  cin >> n;
  string a, b;
  for (i = 0; i < n; i++) {
    cin >> a >> b;
    vec.push_back({a, b});
  }
  vector<int> ind;
  for (i = 0; i < n; i++) {
    cin >> k;
    ind.push_back(k - 1);
  }
  string now = min(vec[ind[0]].first, vec[ind[0]].second);
  for (i = 1; i < n; i++) {
    int j = ind[i];
    string s1 = min(vec[j].first, vec[j].second);
    string s2 = max(vec[j].first, vec[j].second);
    if (s1 >= now)
      now = s1;
    else {
      if (s2 >= now)
        now = s2;
      else {
        cout << "NO";
        return 0;
      }
    }
  }
  cout << "YES";
}
