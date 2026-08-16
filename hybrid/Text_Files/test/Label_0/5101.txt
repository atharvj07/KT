#include <bits/stdc++.h>
long long a[1000006], b[1000006], ans, count1, count2, lc, count3, count4,
    count;
long long lcm(long long a, long long b) {
  if (a > b) {
    if (a % b == 0) return b;
    return lcm(b, a % b);
  } else {
    if (b % a == 0) return a;
    return lcm(a, b % a);
  }
}
int main() {
  long long m, h1, h2, x1, x2, y1, y2, a1, a2, p, i, n;
  scanf("%lld", &m);
  scanf("%lld%lld", &h1, &a1);
  scanf("%lld%lld", &x1, &y1);
  scanf("%lld%lld", &h2, &a2);
  scanf("%lld%lld", &x2, &y2);
  p = 1;
  for (i = 0; i < m + 2; i++) a[i] = b[i] = 0;
  count1 = count2 = 0;
  for (i = 0; i < m + 2; i++) {
    if (h1 == a1) {
      p = 0;
      break;
    }
    if (!a[h1])
      a[h1] = 1;
    else {
      break;
    }
    count1++;
    h1 = (h1 * x1 + y1) % m;
  }
  if (p) {
    printf("-1");
    return 0;
  }
  p = 1;
  for (i = 0; i < m + 2; i++) {
    if (h2 == a2) {
      p = 0;
      break;
    }
    if (!b[h2])
      b[h2] = 1;
    else {
      break;
    }
    count2++;
    h2 = (h2 * x2 + y2) % m;
  }
  if (p) {
    printf("-1");
    return 0;
  }
  if (count1 == count2) {
    printf("%lld", count1);
    return 0;
  }
  for (i = 0; i < m + 2; i++) a[i] = b[i] = 0;
  h2 = (h2 * x2 + y2) % m;
  h1 = (h1 * x1 + y1) % m;
  count3 = count4 = 1;
  for (i = 0; i < m + 2; i++) {
    if (h1 == a1) {
      break;
    }
    if (!a[h1])
      a[h1] = 1;
    else {
      count3 = -1;
      break;
    }
    count3++;
    h1 = (h1 * x1 + y1) % m;
  }
  for (i = 0; i < m + 2; i++) {
    if (h2 == a2) {
      break;
    }
    if (!b[h2])
      b[h2] = 1;
    else {
      count4 = -1;
      break;
    }
    count4++;
    h2 = (h2 * x2 + y2) % m;
  }
  count = (count1 > count2) ? count1 : count2;
  if (count3 == -1 && count4 == -1) {
    printf("-1");
    return 0;
  } else if (count3 == -1) {
    if (count1 < count2) {
      printf("-1");
      return 0;
    }
    if ((count1 - count2) % count4 == 0) {
      printf("%lld", count1);
      return 0;
    } else {
      printf("-1");
      return 0;
    }
  } else if (count4 == -1) {
    if (count2 < count1) {
      printf("-1");
      return 0;
    }
    if ((count2 - count1) % count3 == 0) {
      printf("%lld", count2);
      return 0;
    } else {
      printf("-1");
      return 0;
    }
  }
  i = 0;
  while (1) {
    if (i > 10000000) {
      printf("-1");
      return 0;
    }
    i++;
    if (((count - count1) % count3 == 0) && ((count - count2) % count4 == 0))
      break;
    count = count3 * i + count1;
  }
  printf("%lld", count);
  return 0;
}
