#include <bits/stdc++.h>
using namespace std;
void RD(int &x) { scanf("%d", &x); }
void RD(long long &x) { scanf("%I64d", &x); }
void RD(unsigned long long &x) { scanf("%I64u", &x); }
void RD(unsigned int &x) { scanf("%u", &x); }
void RD(double &x) { scanf("%lf", &x); }
void RD(int &x, int &y) { scanf("%d%d", &x, &y); }
void RD(unsigned int &x, unsigned int &y) { scanf("%u%u", &x, &y); }
void RD(double &x, double &y) { scanf("%lf%lf", &x, &y); }
void RD(double &x, double &y, double &z) { scanf("%lf%lf%lf", &x, &y, &z); }
void RD(int &x, int &y, int &z) { scanf("%d%d%d", &x, &y, &z); }
void RD(unsigned int &x, unsigned int &y, unsigned int &z) {
  scanf("%u%u%u", &x, &y, &z);
}
void RD(char &x) { x = getchar(); }
void RD(char *s) { scanf("%s", s); }
void RD(string &s) { cin >> s; }
void PR(int x) { printf("%d\n", x); }
void PR(int x, int y) { printf("%d %d\n", x, y); }
void PR(long long x) { printf("%I64d\n", x); }
void PR(unsigned int x) { printf("%u\n", x); }
void PR(double x) { printf("%.10lf\n", x); }
void PR(double x, double y) { printf("%.5lf %.5lf\n", x, y); }
void PR(char x) { printf("%c\n", x); }
void PR(char *x) { printf("%s\n", x); }
void PR(string x) { cout << x << endl; }
void upMin(int &x, int y) {
  if (x > y) x = y;
}
void upMin(long long &x, long long y) {
  if (x > y) x = y;
}
void upMin(double &x, double y) {
  if (x > y) x = y;
}
void upMax(int &x, int y) {
  if (x < y) x = y;
}
void upMax(long long &x, long long y) {
  if (x < y) x = y;
}
void upMax(double &x, double y) {
  if (x < y) x = y;
}
const long long inf = ((long long)1) << 60;
const double dinf = 1e10;
const int INF = 100000000;
const int N = 5005;
int n, m, K, s, a[N][N];
set<int> S[10][4];
int b[100005], c[10][10];
int main() {
  while (scanf("%d", &n) != -1) {
    RD(m, K, s);
    int i, j, k;
    for (i = 0; i < 10; i++)
      for (j = 0; j < 4; j++) S[i][j].clear();
    for (i = 1; i <= n; i++)
      for (j = 1; j <= m; j++) {
        int x;
        RD(x);
        S[x][0].insert(-i - j);
        S[x][1].insert(-i + j);
        S[x][2].insert(i - j);
        S[x][3].insert(i + j);
      }
    memset(c, 0, sizeof(c));
    for (i = 1; i <= s; i++) {
      RD(b[i]);
      if (i > 1) c[b[i]][b[i - 1]] = c[b[i - 1]][b[i]] = 1;
    }
    int ans = 0;
    set<int>::iterator it;
    for (i = 1; i <= 9; i++)
      for (j = 1; j <= 9; j++)
        if (c[i][j]) {
          for (k = 0; k < 4; k++)
            for (it = S[i][k].begin(); it != S[i][k].end(); it++) {
              upMax(ans, ((*it - *S[j][k].rbegin()) >= 0
                              ? (*it - *S[j][k].rbegin())
                              : -(*it - *S[j][k].rbegin())));
              upMax(ans, ((*it - *S[j][k].begin()) >= 0
                              ? (*it - *S[j][k].begin())
                              : -(*it - *S[j][k].begin())));
            }
        }
    PR(ans);
  }
}
