#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string rebus;
  getline(cin, rebus);
  int n = 0, num_plus = 1, num_minus = 0;
  for (char c : rebus) {
    if (c == '+')
      ++num_plus;
    else if (c == '-')
      ++num_minus;
    else if (c >= '0' && c <= '9')
      n = 10 * n + c - '0';
  }
  if (n > n * num_plus - num_minus || n < num_plus - n * num_minus) {
    cout << "Impossible\n";
    return 0;
  }
  int res = num_plus - n * num_minus;
  vector<int> plus(num_plus, 1), minus(num_minus, n);
  for (int i = 0; i < num_plus; ++i) {
    if (res < 1) {
      plus[i] += n - 1;
      res += n - 1;
    } else {
      plus[i] += n - res;
      res += n - res;
    }
  }
  for (int i = 0; i < num_minus; ++i) {
    if (res < 1) {
      minus[i] -= n - 1;
      res += n - 1;
    } else {
      minus[i] -= n - res;
      res += n - res;
    }
  }
  cout << "Possible\n";
  char op = '+';
  int i = 0, j = 0;
  for (char c : rebus) {
    if (c == '+' || c == '-') op = c;
    if (c == '?') {
      if (op == '+')
        cout << plus[i++];
      else
        cout << minus[j++];
    } else {
      cout << c;
    }
  }
  cout << '\n';
  return 0;
}
