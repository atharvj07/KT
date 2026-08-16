#include <bits/stdc++.h>
long long z = 1000000007;
using namespace std;
vector<bool> vec(1000003, 1);
bool sortinrev(const pair<int, int> &a, const pair<int, int> &b) {
  return (a.first > b.first);
}
bool sortbysecdesc(const pair<int, int> &a, const pair<int, int> &b) {
  return a.second > b.second;
}
long long egcd(long long a, long long b) {
  if (b == 0)
    return a;
  else
    return egcd(b, a % b);
}
double logn(double a, double base) { return log2(a) / log2(base); }
bool isprime(long long n) {
  if (n == 1) return false;
  bool b = true;
  for (long long i = 2; i * i <= n; i++) {
    if (n % i == 0) {
      b = false;
      break;
    }
  }
  return b;
}
void sieve(vector<long long> &res, long long n) {
  for (long long i = 2; (i * i) <= n; i++) {
    if (vec[i]) {
      res.push_back(i);
      for (long long j = i * i; (j <= n && j <= 1000000); j += i)
        vec[j] = false;
    }
  }
}
struct node {
  int p, cf, cb;
  node *next;
};
bool compare(double a, double b) {
  double eps = 0.000001;
  return fabs(a - b) <= eps;
}
long long count_Divisors(long long n) {
  long long cnt = 0, ans = 1;
  if (n == 1) {
    return 1;
  }
  for (long long i = 2; (i * i * i) <= n; i++) {
    if (n % i == 0) {
      int cnt = 1;
      while (n > 1 && n % i == 0) {
        n /= i;
        cnt++;
      }
      ans *= cnt;
    }
  }
  if (isprime(n))
    ans *= 2;
  else if ((floor(sqrt(n)) == ceil(sqrt(n))) && isprime((int)sqrt(n)))
    ans *= 3;
  else if (n != 1)
    ans *= 4;
  return ans;
}
void solve() {
  bool b = false;
  long long n, k;
  long long ans = (long long)1e12 + 1;
  pair<long long, long long> p;
  cin >> n;
  if (n == 1) {
    cout << "1 1";
    return;
  }
  for (long long i = 1; i * i <= n; i++) {
    if (n % i == 0 && (n / i != i)) {
      if ((egcd(i, n / i) == 1) && (max(i, n / i) < ans)) {
        ans = max(i, n / i);
        p.first = i;
        p.second = n / i;
      }
    }
  }
  cout << p.first << ' ' << p.second << '\n';
  return;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int T = 1;
  while (T--) {
    solve();
  }
  return 0;
}
