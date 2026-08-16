#include <iostream>
#include <vector>
#include <set>
#define loop(i, a, n) for (int i = (a); i < (n); i++)
#define rep(i, n) loop(i, 0, n)
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  for (int &x : a) cin >> x;
  for (int &x : b) cin >> x;
  set<int> s(b.begin(), b.end());
  if (s.size() == n) {
    cout << "Yes" << endl;
    return 0;
  }
  cout << "No" << endl;
  rep(i, n) cout << a[0] << " \n"[i == n - 1];
  rep(i, n) cout << (s.count(a[i]) ? a[0] : a[1]) << " \n"[i == n - 1];
}
