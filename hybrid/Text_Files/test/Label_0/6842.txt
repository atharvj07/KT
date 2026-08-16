#include <bits/stdc++.h>
using namespace std;
int Matrix_Num = 2;
long long pp;
struct Tmatrix {
  long long num[3][3], n;
  Tmatrix() {
    memset(num, 0, sizeof(num));
    n = Matrix_Num;
  }
  void unit() {
    memset(num, 0, sizeof(num));
    for (int i = 1; i <= n; i++) num[i][i] = 1;
  }
  Tmatrix operator*(const Tmatrix &a) {
    Tmatrix c;
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= n; j++) {
        long long tmp = 0;
        for (int k = 1; k <= n; k++) {
          long long t = (long double)num[i][k] * a.num[k][j] / pp;
          tmp += num[i][k] * a.num[k][j] - t * pp;
          if (tmp >= pp) tmp -= pp;
          if (tmp < 0) tmp += pp;
        }
        c.num[i][j] = tmp;
      }
    return c;
  }
} Matrix;
Tmatrix power(Tmatrix &x, long long n) {
  Tmatrix tmp = x, ans;
  ans.unit();
  while (n) {
    if (n & 1) ans = ans * tmp;
    tmp = tmp * tmp;
    n >>= 1;
  }
  return ans;
}
int f[5008];
vector<long long> q, q1;
long long X;
struct Tprogram {
  void open() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
  }
  void close() {
    fclose(stdin);
    fclose(stdout);
  }
  void init() {
    scanf("%I64d", &X);
    Matrix_Num = 2;
  }
  void work() {
    for (int i = 0; i <= 1505; i++) {
      if (i == 0)
        f[i] = 0;
      else if (i == 1)
        f[i] = 1;
      else
        f[i] = f[i - 1] + f[i - 2];
      if (f[i] >= 1000) f[i] -= 1000;
    }
    for (int i = 0; i <= 1499; i++)
      if (f[i] == X % 1000) q.push_back(i);
    Tmatrix tmp;
    tmp.num[1][1] = 0;
    tmp.num[1][2] = tmp.num[2][1] = tmp.num[2][2] = 1;
    for (long long t = 1e4; t <= 1e13; t *= 10) {
      long long T = t / 100 * 15;
      pp = t;
      Tmatrix gg = power(tmp, T);
      q1.clear();
      for (int i = 0; i <= (int)q.size() - 1; i++) {
        Tmatrix g = power(tmp, q[i]);
        if (g.num[2][1] == X % t) q1.push_back(q[i]);
        for (int j = 1; j <= 9; j++) {
          g = g * gg;
          q[i] += T;
          if (g.num[2][1] == X % t) q1.push_back(q[i]);
        }
      }
      q = q1;
    }
    sort(q.begin(), q.end());
    if (q.empty())
      printf("-1\n");
    else
      printf("%I64d\n", q[0]);
  }
} Program;
int main() {
  Program.init();
  Program.work();
  return 0;
}
