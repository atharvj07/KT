#include <bits/stdc++.h>
using namespace std;
unordered_map<int, int> ct;
unsigned long long ansP = 0, ansN = 0;
unsigned long long sum = 0;
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    ansP += (unsigned long long)i * x;
    ansN += ct[x - 1] + sum;
    ansP += ct[x + 1];
    sum += x;
    ct[x]++;
    if (ansP >= ansN) {
      ansP -= ansN;
      ansN = 0;
    } else {
      ansN -= ansP;
      ansP = 0;
    }
  }
  if (ansN > 0) {
    printf("-%llu", ansN);
  } else {
    printf("%llu", ansP);
  }
}
