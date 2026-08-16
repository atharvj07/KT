#include <bits/stdc++.h>
using namespace std;
void RD(int &x) { scanf("%d", &x); }
void RD(long long &x) { scanf("%I64d", &x); }
void RD(double &x) { scanf("%lf", &x); }
void RD(int &x, int &y) { scanf("%d%d", &x, &y); }
void RD(long long &x, long long &y) { scanf("%I64d%I64d", &x, &y); }
void RD(double &x, double &y) { scanf("%lf%lf", &x, &y); }
void RD(char *s) { scanf("%s", s); }
void RD(char &s) { scanf(" %c", &s); }
void RD(string &s) { cin >> s; }
void PR(int x) { printf("%d\n", x); }
void PR(int x, int y) { printf("%d %d\n", x, y); }
void PR(long long x) { printf("%I64d\n", x); }
void PR(char x) { printf("%c\n", x); }
void PR(char *x) { printf("%s\n", x); }
void PR(string x) { cout << x << endl; }
const long long inf = 1;
const long long mod = 1LL;
int num[100010], entry[100010], mark[100010];
char logg[100010];
int main() {
  int i, j, k, n, m, pre, cnt;
  char ch;
  while (scanf("%d %d", &n, &m) == 2) {
    memset(entry, 0, sizeof(entry));
    for ((i) = 1; (i) <= (int)(n); (i)++) mark[i] = 1;
    cnt = pre = 0;
    for ((i) = 1; (i) <= (int)(m); (i)++) {
      RD(logg[i]);
      RD(num[i]);
    }
    for ((i) = 1; (i) <= (int)(m); (i)++) {
      if (logg[i] == '+') {
        cnt++;
        entry[num[i]] = 1;
        if (i != 1 && num[i] != num[i - 1])
          mark[num[i]] = 0;
        else
          pre = num[i];
      } else {
        if (!entry[num[i]])
          mark[pre] = 0;
        else
          cnt--;
        if (cnt > 0) mark[num[i]] = 0;
        entry[num[i]] = 0;
        if (num[i + 1] != num[i] && i != m) mark[num[i]] = 0;
      }
    }
    PR(k = count(mark + 1, mark + n + 1, 1));
    if (k) {
      for ((i) = 1; (i) <= (int)(n); (i)++)
        if (mark[i] == 1) printf("%d ", i);
      puts("");
    }
  }
  return 0;
}
