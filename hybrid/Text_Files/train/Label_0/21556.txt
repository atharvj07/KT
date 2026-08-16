#include <bits/stdc++.h>
using namespace std;
const int N = 1000001;
long long highp2(long long n) { return (n & (~(n - 1))); }
bool isPrime(long long n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (long long i = 5; i * i <= n; i = i + 6)
    if (n % i == 0 || n % (i + 2) == 0) return false;
  return true;
}
long long binarysearchlf(long long l, long long h, vector<long long> &a,
                         long long k) {
  while (l < h) {
    long long mid = l + ((h - l + 1) / 2);
    if (a[mid] < k)
      l = mid;
    else
      h = mid - 1;
  }
  return l;
}
long long binarysearchft(long long l, long long h, vector<long long> &a,
                         long long k) {
  while (l < h) {
    long long mid = l + ((h - l) / 2);
    if (a[mid] < k)
      l = mid + 1;
    else
      h = mid;
  }
  return l;
}
long long gcd(long long a, long long b) {
  if (a < b) swap(a, b);
  if (b == 0) return a;
  return (b, a % b);
}
string getstring(long long k, char x) {
  string s(k, x);
  return s;
}
bool sort1(const pair<long long, long long> &a,
           const pair<long long, long long> &b) {
  return a.second < b.second;
}
bool sort2(const vector<int> &v1, const vector<int> &v2) {
  if (v1[1] > v2[1])
    return true;
  else if (v1[1] < v2[1])
    return false;
  else {
    return v1[2] > v2[2];
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  string s;
  cin >> s;
  int i1, i2;
  int flag1 = 0, flag2 = 0;
  int n = s.length();
  for (long long i = 0; i < n - 1; i++) {
    if (s[i] == 'A' && s[i + 1] == 'B') {
      i1 = i;
      flag1 = 1;
      break;
    }
  }
  for (long long i = 0; i < n - 1; i++) {
    if (s[i] == 'B' && s[i + 1] == 'A') {
      i2 = i;
      flag2 = 1;
      break;
    }
  }
  if (flag1 == 0 || flag2 == 0) {
    cout << "NO" << endl;
    return 0;
  }
  if (abs(i1 - i2) > 1)
    cout << "YES" << endl;
  else {
    int flag = 0;
    for (int i = i2 + 2; i < n - 1; i++) {
      if (s[i] == 'A' && s[i + 1] == 'B') flag = 1;
    }
    for (int i = i1 + 2; i < n - 1; i++) {
      if (s[i] == 'B' && s[i + 1] == 'A') flag = 1;
    }
    if (flag)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
