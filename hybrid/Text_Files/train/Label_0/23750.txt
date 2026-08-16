#include <bits/stdc++.h>
using namespace std;
int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
void es(int n, vector<int> &p) {
  vector<bool> pr(n, true);
  for (int i = 2; i < n; i++) {
    if (pr[i]) {
      p.push_back(i);
      for (int j = i; j < n; j += i) {
        pr[j] = false;
      }
    }
  }
}
void add(int n, map<int, int> &m, vector<int> &p) {
  int i = 0;
  while (i < p.size()) {
    if (n == 1) return;
    if (n % p[i] == 0) {
      if (m.count(p[i]) == 0) {
        m[p[i]] = 0;
      }
      m[p[i]]++;
      while (n % p[i] == 0) {
        n /= p[i];
      }
    }
    i++;
  }
  if (m.count(n) == 0) {
    m[n] = 0;
  }
  m[n]++;
}
int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  vector<int> primes;
  es(4000, primes);
  map<int, int> m;
  int usj = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
    usj = gcd(v[i], usj);
  }
  for (int i = 0; i < n; i++) {
    v[i] /= usj;
    add(v[i], m, primes);
  }
  if (m.size() == 0) {
    cout << -1 << endl;
    return 0;
  }
  int max = 0;
  for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it) {
    if (it->second > max) max = it->second;
  }
  cout << n - max << endl;
}
