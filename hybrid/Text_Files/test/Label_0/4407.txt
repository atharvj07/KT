#include <bits/stdc++.h>
#pragma GCC optimize "trapv"
using namespace std;
const long long int mod = 1000000007;
const long long int MAX = 100005;
long long int fact(long long int);
long long int lcm(long long int, long long int);
long long int gcd(long long int, long long int);
bool prime[MAX + 1];
vector<long long int> pr;
long long int fact(long long int n) {
  if (n == 0) return 1;
  return n * fact(n - 1);
}
long long int gcd(long long int a, long long int b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
long long int lcm(long long int a, long long int b) {
  return (a * b) / gcd(a, b);
}
long long int modPower(long long int a, long long int b) {
  long long int res = 1;
  while (b) {
    if (b & 1) res = (res % mod * a % mod) % mod;
    b >>= 1;
    a = (a % mod * a % mod) % mod;
  }
  return res;
}
long long int sigma(long long int x) { return (x * (x + 1)) / 2; }
string decimalToBinary(long long int n) {
  string s = bitset<64>(n).to_string();
  const auto loc1 = s.find('1');
  if (loc1 != string::npos) return s.substr(loc1);
  return "0";
}
long long int modFact(long long int n) {
  if (n >= mod) return 0;
  long long int result = 1;
  for (long long int i = 1; i <= n; i++) result = (result * i) % mod;
  return result;
}
void SieveOfEratosthenes() {
  memset(prime, true, sizeof(prime));
  for (long long int p = 2; p * p <= MAX; p++) {
    if (prime[p] == true) {
      for (long long int i = p * p; i <= MAX; i += p) prime[i] = false;
    }
  }
  for (long long int p = 2; p <= MAX; p++)
    if (prime[p]) pr.push_back(p);
}
void solve() {
  long long int n;
  cin >> n;
  string s1, s2;
  cin >> s1 >> s2;
  long long int c = 0;
  for (long long int i = 0; i < n; i++) {
    if (s1[i] != s2[i] && i + 1 < n && s1[i + 1] != s2[i + 1] &&
        ((s1[i] == '1' && s1[i + 1] == '0') ||
         (s1[i] == '0' && s1[i + 1] == '1'))) {
      c++;
      i++;
    } else if (s1[i] != s2[i])
      c++;
  }
  cout << c;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long int T = 1;
  for (long long int i = 1; i <= T; i++) {
    solve();
    cout << "\n";
  }
  return 0;
}
