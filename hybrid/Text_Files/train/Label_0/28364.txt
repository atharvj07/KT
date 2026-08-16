#include <bits/stdc++.h>
using namespace std;
const int N = 1000010;
const long long MOD = 1e9 + 7;
void solve() {
  int a, x, y;
  cin >> a >> x >> y;
  int k = a / 2;
  if (x == k && y == k) {
    cout << "NO"
         << "\n";
    return;
  }
  if (x == k + 1 && y == k) {
    cout << "NO"
         << "\n";
    return;
  }
  if (x == k && y == k + 1) {
    cout << "NO"
         << "\n";
    return;
  }
  if (x == k + 1 && y == k + 1) {
    cout << "NO"
         << "\n";
    return;
  }
  cout << "YES"
       << "\n";
}
int main() { solve(); }
