#include <bits/stdc++.h>
using namespace std;
int judge(int n) {
  int flag = 0;
  for (int i = 2; i <= n / 2; i++) {
    if (n % i == 0) {
      flag = 1;
      break;
    }
  }
  if (flag)
    return 0;
  else
    return 1;
}
int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= 1000; i++) {
    int sum = i * n + 1;
    if (judge(sum) == 0) {
      printf("%d\n", i);
      return 0;
    }
  }
  return 0;
}
