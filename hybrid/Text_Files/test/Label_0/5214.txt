#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  unordered_multiset<int> a, b;
  unordered_multiset<int>::iterator it;
  for (int i = 0, x; i < n; i++) {
    cin >> x;
    a.emplace(x);
    b.emplace(x);
  }
  n--;
  for (int i = 0, x; i < n; i++) {
    cin >> x;
    it = a.find(x);
    a.erase(it);
  }
  cout << *a.begin() << endl;
  it = b.find(*a.begin());
  b.erase(it);
  n--;
  for (int i = 0, x; i < n; i++) {
    cin >> x;
    it = b.find(x);
    b.erase(it);
  }
  cout << *b.begin() << endl;
  return 0;
}
