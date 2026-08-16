#include <bits/stdc++.h>
using namespace std;
vector<long long> a;
long long k, p;
long long getNext(long long curr) {
  if (curr > 0)
    return -(curr / k);
  else {
    if (curr % k == 0)
      return -(curr / k);
    else
      return -(curr / k) + 1;
  }
}
int main() {
  scanf("%lld %lld", &p, &k);
  a.reserve(100);
  a.push_back(getNext(p));
  if (a.back() >= k) {
    printf("-1\n");
    return 0;
  }
  if (p < k) {
    printf("1\n%lld\n", p);
    return 0;
  }
  for (int i = 0;; i++) {
    a.push_back(getNext(a[i]));
    if (0 < a[i + 1] && a[i + 1] < k) {
      break;
    }
    if (a[i + 1] == 0) {
      printf("-1\n");
      return 0;
    }
  }
  printf("%d\n", a.size() + 1);
  printf("%lld ", k * a[0] + p);
  for (int i = 0; i + 1 < a.size(); i++) {
    printf("%lld ", k * a[i + 1] + a[i]);
  }
  printf("%lld\n", a.back());
}
