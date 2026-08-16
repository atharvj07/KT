#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline T gcd(T a, T b) {
  return b ? gcd(b, a % b) : a;
}
int n;
string s;
void basic() {
  cin >> n >> s;
  int i = 0, k = 1;
  while (i != n) {
    cout << s[i];
    i += k;
    k++;
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  basic();
  getchar();
  getchar();
  return 0;
}
