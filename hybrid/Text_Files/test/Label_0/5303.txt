#include <bits/stdc++.h>
using namespace std;
const long long int MOD = 1e9 + 7;
inline long long int gcd(long long int a, long long int b) {
  return b ? gcd(b, a % b) : a;
}
inline long long int lcm(long long int a, long long int b) {
  return a * b / gcd(a, b);
}
inline long long int add(long long int a, long long int b) {
  return ((a % MOD) + (b % MOD)) % MOD;
}
inline long long int multi(long long int a, long long int b) {
  return ((a % MOD) * (b % MOD)) % MOD;
}
inline long long int sub(long long int a, long long int b) {
  a %= MOD;
  b %= MOD;
  a -= b;
  if (a < 0) a += MOD;
  return a;
}
inline long long int power(long long int a, long long int b) {
  a %= MOD;
  long long int res = 1;
  while (b > 0) {
    if (b & 1) {
      res = multi(res, a);
    }
    a = multi(a, a);
    b >>= 1;
  }
  return res;
}
bool isPrime(long long int x) {
  if (x <= 4 || x % 2 == 0 || x % 3 == 0) {
    return x == 2 || x == 3;
  }
  for (long long int i = 5; i * i <= x; i += 6) {
    if (x % i == 0 || x % (i + 2) == 0) {
      return 0;
    }
  }
  return 1;
}
map<string, long long int> mop;
long long int dist[2005][10];
long long int n, k;
string arr[2005];
vector<vector<long long int>> dp(2005, vector<long long int>(2005, -1));
void call() {
  string brr[10] = {"1110111", "0010010", "1011101", "1011011", "0111010",
                    "1101011", "1101111", "1010010", "1111111", "1111011"};
  for (long long int i = 0; i < 10; i++) {
    mop[brr[i]] = i;
  }
  for (long long int i = 0; i < n; i++) {
    string temp = arr[i];
    for (long long int j = 0; j < 10; j++) {
      string to = brr[j];
      dist[i][j] = 0;
      for (long long int m = 0; m < 7; m++) {
        if (temp[m] == to[m])
          continue;
        else if (temp[m] == '0' && to[m] == '1')
          dist[i][j]++;
        else {
          dist[i][j] = -1;
          break;
        }
      }
    }
  }
}
string ans = "";
bool solve(long long int i, long long int k) {
  if (i == n && k == 0) {
    return true;
  }
  if (i == n || k < 0) return false;
  if (dp[i][k] != -1) return (bool)dp[i][k];
  for (long long int j = 9; j >= 0; j--) {
    if (dist[i][j] == -1) continue;
    if (solve(i + 1, k - dist[i][j])) {
      ans = to_string(j) + ans;
      return dp[i][k] = true;
    }
  }
  return dp[i][k] = false;
}
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> k;
  for (long long int i = 0; i < n; i++) cin >> arr[i];
  call();
  if (solve(0, k)) {
    cout << ans;
  } else
    cout << -1;
}
