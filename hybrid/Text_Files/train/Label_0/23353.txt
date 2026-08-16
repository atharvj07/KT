#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  cerr.tie(nullptr);
  int n;
  cin >> n;
  list<int> a;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    a.push_back(x);
  }
  auto it = a.begin();
  while (it != --a.end()) {
    if (*it == *next(it)) {
      a.erase(next(it));
      ++*it;
      if (it != a.begin()) --it;
    } else {
      ++it;
    }
  }
  cout << a.size() << '\n';
  for (int x : a) cout << x << ' ';
  cout << '\n';
}
