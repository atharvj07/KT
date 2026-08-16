#include <bits/stdc++.h>
using namespace std;
long long sieve[100000];
vector<long long> primes;
void eratosthenis(long long n) {
  for (long long x = 2; x <= n; x++) {
    if (sieve[x]) continue;
    for (long long u = 2 * x; u <= n; u += x) {
      sieve[u] = x;
    }
    primes.push_back(x);
  }
}
vector<long long> V;
vector<pair<long long, long long> > ans;
void mull(long long p, long long n) {
  vector<long long> mul;
  for (long long i = p; i <= n; i += p) {
    if (V[i] == 0) mul.push_back(i);
  }
  reverse(mul.begin(), mul.end());
  if (mul.size() % 2 && mul.size() > 1) {
    long long temp = mul.back();
    mul.pop_back();
    mul.pop_back();
    mul.push_back(temp);
  }
  for (long long i = 0; i < mul.size(); i += 2) {
    ans.push_back({mul[i], mul[i + 1]});
    V[mul[i]] = V[mul[i + 1]] = 1;
  }
  return;
}
int main() {
  long long n;
  cin >> n;
  eratosthenis(n / 2);
  V.assign(n + 2, 0);
  reverse(primes.begin(), primes.end());
  for (auto x : primes) {
    if (x != 2) mull(x, n);
  }
  vector<long long> artion;
  for (long long i = 2; i <= n; i += 2) {
    if (V[i] == 0) {
      artion.push_back(i);
    }
  }
  cout << ans.size() + artion.size() / 2 << endl;
  for (auto x : ans) {
    cout << x.first << ' ' << x.second << endl;
  }
  long long k = 1;
  if (artion.size() % 2 == 1) artion.pop_back();
  for (auto x : artion) {
    cout << x;
    if (k)
      cout << ' ';
    else
      cout << '\n';
    V[x] = 1;
    k ^= 1;
  }
  cout << endl;
  return 0;
}
