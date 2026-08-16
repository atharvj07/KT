#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  srand(time(NULL));
  ;
  int n, r, q, i, j;
  cin >> q;
  while (q) {
    cin >> n >> r;
    set<int> s;
    int c = 0;
    for (i = 0; i < n; i++) {
      cin >> j;
      s.insert(j);
    }
    vector<int> v;
    for (auto it = s.begin(); it != s.end(); it++) {
      j = *it;
      v.push_back(j);
    }
    n = v.size();
    reverse(v.begin(), v.end());
    for (i = 0; i < n; i++) {
      if ((v[i] - (r * c)) <= 0) {
        break;
      }
      c++;
    }
    cout << i << endl;
    q--;
  }
  return 0;
}
