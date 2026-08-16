#include <bits/stdc++.h>
using namespace std;
const int MAX = 500500, MOD = 1e9 + 7;
long long Norm(long long x) { return ((x % MOD + MOD) % MOD); }
int n;
long long prefsumx[2 * MAX], prefsumy[2 * MAX];
long long prefpov[2 * MAX];
long long prefob[2 * MAX], prefprav[2 * MAX];
pair<int, int> tocke[2 * MAX];
long long UmToc(int a, int b) {
  return (long long)tocke[a].first * tocke[b].second -
         (long long)tocke[b].first * tocke[a].second;
}
long long Suma(long long polje[2 * MAX], int a, int b) {
  if (a > b) b += n;
  long long ret = polje[b];
  if (a) ret -= polje[a - 1];
  return ret;
}
long long Povrsina(int a, int b) {
  if (a == b || a + 1 == b) return 0;
  return Suma(prefpov, a, b - 1) + UmToc(b, a);
}
void GenPref() {
  for (int i = 0; i < 2 * n; i++) {
    prefpov[i] = UmToc(i, i + 1);
    prefsumx[i] = tocke[i].first;
    prefsumy[i] = tocke[i].second;
    if (i) {
      prefpov[i] += prefpov[i - 1];
      prefsumx[i] += prefsumx[i - 1];
      prefsumy[i] += prefsumy[i - 1];
    }
    prefsumx[i] = Norm(prefsumx[i]);
    prefsumy[i] = Norm(prefsumy[i]);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = n - 1; i >= 0; i--)
    scanf("%d%d", &tocke[i].first, &tocke[i].second);
  for (int i = n; i <= 2 * n; i++) tocke[i] = tocke[i % n];
  GenPref();
  long long summanj = 0;
  for (int i = 0, j = 1; i < n; i++) {
    j = max(j, i + 1);
    for (; Povrsina(i, j) <= Povrsina(j, i); j++)
      ;
    j--;
    if (Povrsina(i, j) == Povrsina(j, i) && i > (j % n)) j--;
    if (j == i + 1) continue;
    int kol = j - (i + 1);
    prefob[i] += kol;
    prefprav[i + 2]--;
    prefprav[j + 1]++;
    summanj = Norm(summanj + Norm(Suma(prefsumx, i + 2, j)) * tocke[i].second -
                   Norm(Suma(prefsumy, i + 2, j)) * tocke[i].first);
  }
  long long tprav = 0, tsum = 0;
  for (int i = 0; i < 2 * n; i++) {
    tprav += prefprav[i];
    tsum += prefob[i] + tprav;
    tsum = Norm(tsum);
    summanj = Norm(summanj + Norm(UmToc(i, i + 1)) * tsum);
  }
  long long rje =
      Norm(Norm((long long)n * (n - 3) / 2) * Norm(Povrsina(0, n - 1)) -
           2 * summanj);
  printf("%lld\n", rje);
  return 0;
}
