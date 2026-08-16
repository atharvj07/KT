#include <bits/stdc++.h>
using namespace std;
const int maxn = 100005;
long long cntodd[2], cnteven[2];
char buf[maxn];
int main() {
  scanf("%s", buf + 1);
  int len = strlen(buf + 1);
  long long sumodd = 0, sumeven = 0;
  for (int i = 1; i <= len; i++) {
    int now = buf[i] - 'a';
    if (i & 1)
      cntodd[now]++;
    else
      cnteven[now]++;
    if (i & 1) {
      sumodd += cntodd[now];
      sumeven += cnteven[now];
    } else {
      sumodd += cnteven[now];
      sumeven += cntodd[now];
    }
  }
  cout << sumeven << " " << sumodd << endl;
  return 0;
}
