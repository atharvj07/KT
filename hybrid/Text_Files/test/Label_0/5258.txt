#include <bits/stdc++.h>
using namespace std;
long long MOD = 1e9 + 7;
long long INF = LLONG_MAX / 4;
vector<string> &split(const std::string &s, char delim, vector<string> &e) {
  stringstream ss(s);
  string item;
  while (getline(ss, item, delim)) e.push_back(item);
  return e;
}
long long Pow(long long a, long long b, long long Mo) {
  long long ans = 1;
  for (; b; b >>= 1, a = a * a % Mo)
    if (b & 1) ans = ans * a % Mo;
  return ans;
}
vector<int> Zfunc(string &s) {
  int n = s.length();
  vector<int> z(n, 0);
  for (int i = 1, l = 0, r = 0; i < n; i++) {
    if (i <= r) z[i] = min(z[i - l], r - i + 1);
    while (i + z[i] < n && s[i + z[i]] == s[z[i]]) z[i]++;
    if (r < i + z[i] - 1) l = i, r = i + z[i] - 1;
  }
  return z;
}
long long sgn(long long x) {
  if (x % 2) return -1;
  return 1;
}
long long solve() { return 0; }
int main(int argc, char const *argv[]) {
  std::ios::sync_with_stdio(false);
  cin.tie(0);
  long long n;
  cin >> n;
  std::vector<long long> v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }
  long long mx = 0;
  {
    long long l = 0;
    long long sum = 0;
    long long leftsum = 0;
    long long minleftsum = 0;
    for (int r = 0; r < n - 1; ++r) {
      sum += abs(v[r] - v[r + 1]) * sgn(r);
      mx = max(mx, sum - minleftsum);
      if (l + 2 <= r) {
        long long x = abs(v[l] - v[l + 1]) - abs(v[l + 1] - v[l + 2]);
        leftsum += x;
        l += 2;
      }
      minleftsum = min(minleftsum, leftsum);
    }
  }
  {
    long long l = 1;
    long long sum = 0;
    long long leftsum = 0;
    long long minleftsum = 0;
    for (int r = 1; r < n - 1; ++r) {
      sum += abs(v[r] - v[r + 1]) * sgn(r + 1);
      mx = max(mx, sum - minleftsum);
      if (l + 2 <= r) {
        long long x = abs(v[l] - v[l + 1]) - abs(v[l + 1] - v[l + 2]);
        leftsum += x;
        l += 2;
      }
      minleftsum = min(minleftsum, leftsum);
    }
  }
  cout << mx;
  return 0;
}
