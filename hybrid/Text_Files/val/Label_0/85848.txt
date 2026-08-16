#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
const long long N = 200005;
const long long inf = 10000000000000000;
bool prime[10000000];
void print(vector<long long> v) {
  long long i;
  for (i = 0; i < v.size(); i++) cout << v[i] << " ";
  cout << "\n";
}
void print(set<long long> s) {
  set<long long>::iterator itr = s.begin();
  for (; itr != s.end(); itr++) {
    cout << (*itr) << " ";
  }
  cout << "\n";
}
vector<long long> read(long long n) {
  long long i;
  vector<long long> arr(n, 0);
  for (i = 0; i < n; i++) cin >> arr[i];
  return arr;
}
vector<long long> read(long long n, long long k) {
  long long i;
  vector<long long> arr(n + k, 0);
  for (i = k; i < n + k; i++) cin >> arr[i];
  return arr;
}
bool isEven(long long n) {
  if (n % 2 == 0) return true;
  return false;
}
bool isOdd(long long n) {
  if (n % 2 == 1) return true;
  return false;
}
void fillPrime() {
  long long i, j;
  long long n = 1000001;
  for (i = 0; i < n; i++) {
    prime[i] = 1;
  }
  prime[0] = 0;
  prime[1] = 0;
  for (i = 2; i * i <= n; i++) {
    if (prime[i]) {
      for (j = i * i; j <= n; j += i) {
        prime[j] = 0;
      }
    }
  }
}
long long gcd(long long a, long long b) {
  if (a < b) swap(a, b);
  if (b == 0) return a;
  return gcd(b, a % b);
}
class Triplet {
 public:
  long long gcd;
  long long x;
  long long y;
};
Triplet extendedEuclidian(long long a, long long b) {
  if (b == 0) {
    Triplet ans;
    ans.gcd = a;
    ans.x = 1;
    ans.y = 0;
    return ans;
  }
  Triplet smallAns = extendedEuclidian(b, a % b);
  Triplet ans;
  ans.gcd = smallAns.gcd;
  ans.x = smallAns.y;
  ans.y = smallAns.x - (a / b) * smallAns.y;
  return ans;
}
long long modInv(long long a, long long m) {
  Triplet ans = extendedEuclidian(a, m);
  return (ans.x % m + m) % m;
}
long long power(long long x, long long n, long long m) {
  if (x == 0) {
    return 0;
  }
  if (n == 0) {
    return 1;
  }
  long long ans;
  if (isEven(n)) {
    long long smallAns = power(x, n / 2, m);
    ans = (smallAns * smallAns) % m;
  } else {
    long long smallAns = power(x, n - 1, m);
    ans = x;
    ans = (ans * smallAns) % m;
  }
  return (ans + m) % m;
}
void multiply(long long M[2][2], long long A[2][2]) {
  long long r00 = A[0][0] * M[0][0] + A[0][1] * M[1][0];
  long long r01 = A[0][0] * M[0][1] + A[0][1] * M[1][1];
  long long r10 = A[1][0] * M[0][0] + A[1][1] * M[1][0];
  long long r11 = A[1][0] * M[1][0] + A[1][1] * M[1][1];
  M[0][0] = r00;
  M[0][1] = r01;
  M[1][0] = r10;
  M[1][1] = r11;
}
void power(long long M[2][2], long long n) {
  if (n == 0 || n == 1) return;
  power(M, n / 2);
  multiply(M, M);
  if (isOdd(n)) {
    long long A[2][2] = {{1, 1}, {1, 0}};
    multiply(M, A);
  }
}
long long fib(long long n) {
  long long M[2][2] = {{1, 1}, {1, 0}};
  if (n == 0) return 0;
  power(M, n - 1);
  return M[0][0];
}
void solve() {
  long long t;
  cin >> (t);
  while (t--) {
    long long i, j, k, n, m, p, q, x, y;
    cin >> n >> k;
    vector<long long> a(n), w(k);
    a = read(n);
    w = read(k);
    sort(a.begin(), a.end(), greater<long long>());
    sort(w.begin(), w.end(), greater<long long>());
    long long ans = 0;
    vector<bool> done(k, 0);
    long long ct = count(w.begin(), w.end(), 1);
    for (i = 0; i < ct; i++) {
      ans += 2 * a[i];
    }
    long long lo = ct, hi = n - 1;
    for (i = 0; i < k; i++) {
      if (w[i] != 1) {
        ans += (a[lo] + a[hi]);
        lo++;
        hi -= w[i] - 1;
      }
    }
    cout << ans << "\n";
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  solve();
  long long i, j, k, n, m, p, q, x, y, a, b;
  return 0;
}
