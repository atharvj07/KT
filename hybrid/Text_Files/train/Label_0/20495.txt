#include <bits/stdc++.h>
const double PI = 3.141592653589793238460;
using namespace std;
long long pows(long long a, long long n, long long m) {
  long long res = 1;
  while (n) {
    if (n % 2 != 0) {
      res = (res * a) % m;
      n--;
    } else {
      a = (a * a) % m;
      n = n / 2;
    }
  }
  return res % m;
}
long long gcd(long long a, long long b) {
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}
void shift(vector<int> &p) {
  int temp = p[0];
  for (int i = 1; i < p.size(); i++) {
    p[i - 1] = p[i];
  }
  p[p.size() - 1] = temp;
}
bool isprime(int n) {
  if (n == 1) {
    return false;
  }
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}
bool istrue(string s) {
  int i = 0;
  int j = s.size() - 1;
  while (i < j) {
    if (s[i] == s[j]) {
      i++;
      j--;
    } else {
      return false;
    }
  }
  return true;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n, m;
  cin >> n >> m;
  vector<string> vi;
  string s;
  for (int i = 0; i < n; i++) {
    cin >> s;
    vi.push_back(s);
  }
  vector<string> vii;
  long long sum = 0;
  for (int i = 0; i < n; i++) {
    string p = vi[i];
    for (int j = i + 1; j < n; j++) {
      int flag = 1;
      string d = vi[j];
      for (int k = 0; k < m; k++) {
        if (p[k] != d[m - k - 1]) {
          flag = 0;
        }
      }
      if (flag == 1) {
        vii.push_back(p);
        sum = sum + (2 * p.size());
      }
    }
  }
  string g;
  for (int i = 0; i < n; i++) {
    if (istrue(vi[i]) == true) {
      g = vi[i];
      break;
    }
  }
  sum = sum + g.size();
  cout << sum << endl;
  for (int i = 0; i < vii.size(); i++) {
    cout << vii[i];
  }
  cout << g;
  for (int i = vii.size() - 1; i >= 0; i--) {
    string f = vii[i];
    for (int j = m - 1; j >= 0; j--) {
      cout << f[j];
    }
  }
}
