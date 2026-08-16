#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T MIN_3(T a, T b, T c) {
  return min(min(a, b), c);
}
template <class T>
inline T MAX_3(T a, T b, T c) {
  return max(max(a, b), c);
}
template <class T>
inline T BIGMOD(T n, T m, T mod) {
  long long int ans = 1;
  long long int k = n;
  while (m) {
    if (m & 1) {
      ans *= k;
      if (ans > mod) ans %= mod;
    }
    k *= k;
    if (k > mod) k %= mod;
    m >>= 1;
  }
  return ans;
}
inline int DBLCMP(double a, double b) {
  if (fabs(a - b) <= 1e-11) return 0;
  if (a < b) return -1;
  return 1;
}
template <class T>
inline T sqr(T x) {
  return x * x;
}
template <class T>
inline int countbit(T n) {
  return (n == 0) ? 0 : (1 + countbit(n & (n - 1)));
}
template <class T>
inline T euclide(T a, T b, T &x, T &y) {
  if (a < 0) {
    T d = euclide(-a, b, x, y);
    x = -x;
    return d;
  }
  if (b < 0) {
    T d = euclide(a, -b, x, y);
    y = -y;
    return d;
  }
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  } else {
    T d = euclide(b, a % b, x, y);
    T t = x;
    x = y;
    y = t - (a / b) * y;
    return d;
  }
}
template <class T>
string toString(T n) {
  ostringstream ost;
  ost << n;
  ost.flush();
  return ost.str();
}
template <class T>
string toBinary(T n) {
  string ret = "";
  while (n) {
    if (n % 2 == 1)
      ret += '1';
    else
      ret += '0';
    n >>= 1;
  }
  reverse(ret.begin(), ret.end());
  return ret;
}
void combination(int n, vector<vector<int> > &ret) {
  ret.resize(n + 1, vector<int>(n + 1, 0));
  for (int i = 1; i <= n; i++) {
    ret[i][0] = ret[i][i] = 1;
    for (int j = 1; j < i; j++) {
      ret[i][j] = ret[i - 1][j] + ret[i - 1][j - 1];
    }
  }
}
int toInt(string s) {
  int r = 0;
  istringstream sin(s);
  sin >> r;
  return r;
}
long long int toLInt(string s) {
  long long int r = 0;
  istringstream sin(s);
  sin >> r;
  return r;
}
double toDouble(string s) {
  double r = 0;
  istringstream sin(s);
  sin >> r;
  return r;
}
vector<string> parse(string temp) {
  vector<string> ans;
  ans.clear();
  string s;
  istringstream iss(temp);
  while (iss >> s) ans.push_back(s);
  return ans;
}
template <class T>
inline T gcd(T a, T b) {
  if (a < 0) return gcd(-a, b);
  if (b < 0) return gcd(a, -b);
  return (b == 0) ? a : gcd(b, a % b);
}
template <class T>
inline T lcm(T a, T b) {
  if (a < 0) return lcm(-a, b);
  if (b < 0) return lcm(a, -b);
  return a * (b / gcd(a, b));
}
template <class T>
inline T power(T b, T p) {
  if (p < 0) return -1;
  if (b <= 0) return -2;
  if (!p) return 1;
  return b * power(b, p - 1);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string s;
  int w, b;
  bool f = true;
  for (int i = 0; i < 8; i++) {
    cin >> s;
    w = b = 0;
    for (int j = 0; j < 8; j++) {
      if (s[j] == 'W')
        w++;
      else
        b++;
      if (j < 7 && s[j] == s[j + 1]) f = false;
    }
    if (w != 4 || b != 4) {
      f = false;
    }
  }
  if (f)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
