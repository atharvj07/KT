#include <bits/stdc++.h>
using namespace std;
int a[6];
int main() {
  for (int i = 0; i < 6; i++) scanf("%d", &a[i]);
  int sum = 0;
  for (int i = 1; i <= (int)(((a[1]) <= (a[5])) ? (a[1]) : (a[5])); i++) {
    sum += a[0];
    a[0]++;
    sum += a[0];
  }
  for (int i = 1; i <= (int)(((a[1]) >= (a[5])) ? (a[1]) : (a[5])) -
                           (int)(((a[1]) <= (a[5])) ? (a[1]) : (a[5]));
       i++) {
    sum += a[0];
    sum += a[0];
  }
  for (int i = 1; i <= (int)(((a[2]) <= (a[4])) ? (a[2]) : (a[4])); i++) {
    sum += a[3];
    a[3]++;
    sum += a[3];
  }
  cout << sum;
  return 0;
}
