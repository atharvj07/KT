#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long LINF = 0x3f3f3f3f3f3f3f3fll;
const double Pi = acos(-1.0);
char s[100100];
long long aimpar[100100], apar[100100], bimpar[100100], bpar[100100];
int main() {
  scanf(" %s", s);
  long long imp = 0, par = 0, n = strlen(s);
  aimpar[0] = bimpar[0] = 0;
  for (int i = 1; i < n; i++) {
    aimpar[i] = aimpar[i - 1];
    bimpar[i] = bimpar[i - 1];
    if (i % 2 == 0) continue;
    if (s[i] == 'a') aimpar[i]++;
    if (s[i] == 'b') bimpar[i]++;
  }
  apar[0] = (int)(s[0] == 'a');
  bpar[0] = (int)(s[0] == 'b');
  for (int i = 1; i < n; i++) {
    apar[i] = apar[i - 1];
    bpar[i] = bpar[i - 1];
    if (i % 2 == 1) continue;
    if (s[i] == 'a') apar[i]++;
    if (s[i] == 'b') bpar[i]++;
  }
  for (int i = 0; i < n; i++) {
    if (s[i] == 'a') {
      if (i % 2 == 0) {
        par += aimpar[i];
        imp += apar[i];
      } else {
        par += apar[i];
        imp += aimpar[i];
      }
    } else {
      if (i % 2 == 0) {
        par += bimpar[i];
        imp += bpar[i];
      } else {
        par += bpar[i];
        imp += bimpar[i];
      }
    }
  }
  cout << par << ' ' << imp << endl;
  return 0;
}
