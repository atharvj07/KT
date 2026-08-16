#include <bits/stdc++.h>
using namespace std;
const int N = 100000;
struct num {
  vector<long long> z;
  num() { z = vector<long long>(5); }
  num operator+(const num &b) const {
    num c;
    for (int i = 0; i < 5; ++i) {
      c.z[i] = z[i] + b.z[i];
    }
    return c;
  }
  num operator-(const num &b) const {
    num c;
    for (int i = 0; i < 5; ++i) {
      c.z[i] = z[i] - b.z[i];
    }
    return c;
  }
  num operator*(const num &b) const {
    num c;
    for (int i = 0; i < 5; ++i) {
      for (int j = 0; j < 5; ++j) {
        int t = i + j;
        if (t >= 5) t -= 5;
        c.z[t] += z[i] * b.z[j];
      }
    }
    return c;
  }
  num shift(int w) {
    num res;
    for (int i = 0; i < 5; ++i) {
      int t = i + w;
      if (t >= 5) t -= 5;
      res.z[t] = z[i];
    }
    return res;
  }
};
long long power(long long x, long long y) {
  long long res = 1;
  for (; y; y >>= 1, x *= x) {
    if (y & 1) {
      res *= x;
    }
  }
  return res;
}
num power(num x, int y) {
  num res;
  res.z[0] = 1;
  for (; y; y >>= 1, x = x * x) {
    if (y & 1) {
      res = res * x;
    }
  }
  return res;
}
vector<num> a(N);
vector<num> temp(10);
int base[5];
vector<vector<int>> digit(N);
vector<vector<int>> mod(10, vector<int>(10));
vector<vector<int>> dex(10, vector<int>(5));
void dft(bool idft) {
  for (int i = 0; i < 5; i++) {
    for (int k = 0; k < N; k++) {
      if (digit[k][i] == 0) {
        fill(temp.begin(), temp.end(), num());
        for (int u = 0; u < 10; u++) {
          for (int v = 0; v < 10; v++) {
            int w = mod[u][v];
            if (idft) w = 10 - w;
            for (int ii = 0; ii < 5; ii++) {
              if (w & 1)
                temp[u].z[ii] = temp[u].z[ii] -
                                a[k + dex[v][i]].z[(ii + ((w + 5) >> 1)) % 5];
              else
                temp[u].z[ii] =
                    temp[u].z[ii] + a[k + dex[v][i]].z[(ii + (w >> 1)) % 5];
            }
          }
        }
        for (int u = 0; u < 10; u++) a[k + dex[u][i]] = temp[u];
      }
    }
  }
};
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    ++a[x].z[0];
  }
  base[0] = 1;
  for (int i = 1; i < 5; i++) base[i] = 10 * base[i - 1];
  for (int i = 0; i < N; i++) {
    int ta = i;
    for (int j = 0; j < 5; j++) {
      digit[i].push_back(ta % 10);
      ta /= 10;
    }
  }
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      mod[i][j] = i * j % 10;
    }
  }
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 5; j++) {
      dex[i][j] = i * base[j];
    }
  }
  dft(false);
  for (int i = 0; i < N; ++i) {
    a[i] = power(a[i], n);
  }
  dft(true);
  long long inv = power(3125, LLONG_MAX);
  for (int i = 0; i < n; ++i) {
    printf("%lld\n", ((a[i].z[0] - a[i].z[1] >> 5) * inv & (1ll << 58) - 1));
  }
  return 0;
}
