#include <bits/stdc++.h>
using namespace std;
vector<char> v;
int maxn = 200;
int main() {
  int u[maxn];
  string c = "?";
  int x = 0, y = 1, n = 0, sum;
  v.push_back('+');
  while (c == "?" || c == "+" || c == "-" || c == "=") {
    cin >> c;
    if (c == "-") {
      x++;
      v.push_back('-');
    }
    if (c == "+") {
      y++;
      v.push_back('+');
    }
  }
  for (int i = 0; i < c.size(); i++) {
    n *= 10;
    n += c[i] - '0';
  }
  if (n < y - (x * n) || n > y * n - x) {
    cout << "Impossible";
    return 0;
  } else
    cout << "Possible\n";
  for (int i = 0; i <= 200; i++) u[i] = 1;
  sum = y - x;
  for (int i = 0; i < x + y && sum != n; i++) {
    if (sum > n) {
      while (v[i] != '-') i++;
      u[i] += min(sum - n, n - 1);
      sum -= min(sum - n, n - 1);
    }
    if (sum < n) {
      while (v[i] != '+') i++;
      u[i] += min(n - sum, n - 1);
      sum += min(n - sum, n - 1);
    }
  }
  for (int i = 0; i < x + y; i++) {
    if (i + 1 != x + y)
      cout << u[i] << " " << (char)v[i + 1] << " ";
    else
      cout << u[i] << " ";
  }
  printf("= %d", n);
}
