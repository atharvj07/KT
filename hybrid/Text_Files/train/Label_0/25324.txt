#include <bits/stdc++.h>
using namespace std;
inline long long toint(const std::string &s) {
  std::stringstream ss;
  ss << s;
  long long x;
  ss >> x;
  return x;
}
inline std::string tostring(long long number) {
  std::stringstream ss;
  ss << number;
  return ss.str();
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  long long int t;
  cin >> t;
  for (long long int tt = 0; tt < t; tt++) {
    long long int n, a = 0, r = 0;
    cin >> n;
    while (n > 9) {
      a += n - n % 10;
      r = n / 10 + n % 10;
      n = r;
    }
    cout << a + n << "\n";
  }
  return 0;
}
