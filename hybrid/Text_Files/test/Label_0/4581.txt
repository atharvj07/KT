#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, s = 0;
  scanf("%d", &n);
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    s ^= a[i];
  }
  for(int i = 0; i < n; i++) { printf("%d ", s ^ a[i]); }
}