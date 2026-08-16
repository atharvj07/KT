#include <bits/stdc++.h>
using namespace std;
const inline int __GET_INT() {
  int ret;
  scanf("%d", &ret);
  return ret;
}
vector<int> a;
vector<bool> isKnown;
const int inf = 2 * 1000000000;
int toInt(string str) {
  int ret = 0;
  stringstream is(str);
  is >> ret;
  return ret;
}
long long getSum(long long cnt, long long val) {
  if (val < 0) {
    val = labs(val);
    if (cnt <= (val + 1)) {
      return val * cnt - ((cnt * (cnt - 1)) / 2);
    }
    return val * val - ((val * (val - 1)) / 2) + getSum(cnt - val, 0);
  }
  return val * cnt + ((cnt * (cnt - 1)) / 2);
}
void update(int st, int nd, int k) {
  long long cnt = (nd - st) / k + 1;
  if (isKnown[st]) --cnt;
  if (st != nd && isKnown[nd]) --cnt;
  long long low = -inf, high = inf, mid1, mid2;
  if (isKnown[st]) low = a[st] + 1;
  if (isKnown[nd]) high = a[nd] - cnt;
  long long best = (1LL << 60), bestVal = -inf;
  while (low <= high) {
    long long dif = (high - low);
    dif /= 3;
    mid1 = low + dif;
    mid2 = high - dif;
    long long leftSum = getSum(cnt, mid1);
    long long rightSum = getSum(cnt, mid2);
    if (leftSum > rightSum) {
      low = mid1 + 1;
      if (rightSum < best) {
        best = rightSum;
        bestVal = mid2;
      }
    } else {
      high = mid2 - 1;
      if (leftSum < best) {
        best = leftSum;
        bestVal = mid1;
      }
    }
  }
  while (st <= nd) {
    if (!isKnown[st]) {
      a[st] = bestVal++;
    }
    st += k;
  }
}
int main() {
  int n = __GET_INT(), k = __GET_INT();
  char token[20];
  for (int i = 0; i < n; ++i) {
    scanf("%s", token);
    if (token[0] != '?') {
      a.push_back(toInt(token));
      isKnown.push_back(true);
    } else {
      a.push_back(-1);
      isKnown.push_back(false);
    }
  }
  for (int i = 0; i < k; ++i) {
    int j = i, last = i;
    while (j < n) {
      if (isKnown[j]) {
        update(last, j, k);
        last = j;
      }
      j += k;
    }
    update(last, j - k, k);
  }
  bool correct = true;
  for (int i = 0; correct && (i < k); ++i) {
    int j = i + k;
    while (j < n) {
      if (a[j] <= a[j - k]) {
        correct = false;
        break;
      }
      j += k;
    }
  }
  if (correct) {
    for (int i = 0; i < n; ++i) {
      if (i) printf(" ");
      printf("%d", a[i]);
    }
    puts("");
  } else
    puts("Incorrect sequence");
  return 0;
}
