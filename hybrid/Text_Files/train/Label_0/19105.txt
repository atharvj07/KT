#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 2e5 + 4;
int main() {
  vector<pair<long long, char> > ans;
  long long n, st[MAX_N],
      pr[MAX_N] = {
          0,
      };
  long long sum = 0;
  scanf("%lld", &n);
  for (int i = 0; i < n; i++) {
    scanf("%lld", &st[i]);
    pr[i] = st[i];
    sum += (1ll * st[i]);
  }
  long long k, last[MAX_N];
  scanf("%lld", &k);
  for (int i = 0; i < k; i++) {
    scanf("%lld", &last[i]);
    sum = sum - last[i];
  }
  if (sum != 0) {
    cout << "NO";
    return 0;
  }
  int left = n - 1, left_last = k - 1, prev;
  while (left >= 0 && left_last >= 0) {
    if (st[left] != last[left_last]) {
      if (last[left_last] < st[left]) {
        cout << "NO";
        return 0;
      }
      prev = left;
      while (left >= 0 && st[left] < last[left_last]) {
        left--;
        st[left] = st[left] + st[left + 1];
      }
      if (left < 0 || st[left] != last[left_last]) {
        cout << "NO";
        return 0;
      }
      long long max_ = pr[left], find_ = left;
      for (int i = left + 1; i < prev; i++)
        if (max_ < pr[i]) {
          max_ = pr[i];
          find_ = i;
        } else if (max_ == pr[i]) {
          if (i < prev)
            if (pr[i] > pr[i + 1]) {
              max_ = pr[i];
              find_ = i;
            }
        }
      if (max_ < pr[prev]) {
        find_ = prev;
        max_ = pr[prev];
      }
      if (find_ == prev)
        ;
      else if (find_ == left && pr[find_ + 1] == pr[find_]) {
        cout << "NO";
        return 0;
      }
      if (find_ != left && max_ == pr[find_ - 1]) {
        if (find_ < prev && pr[find_] > pr[find_ + 1])
          ;
        else {
          cout << "NO";
          return 0;
        }
      }
      int kol1 = prev - find_;
      int kol2 = find_ - left;
      if (find_ != left && pr[find_ - 1] < pr[find_]) {
        ans.push_back(make_pair(find_ + 1, 'L'));
        kol2--;
        find_--;
      }
      while (kol1 > 0) {
        ans.push_back(make_pair(find_ + 1, 'R'));
        kol1--;
      }
      while (kol2 > 0) {
        ans.push_back(make_pair(find_ + 1, 'L'));
        find_--;
        kol2--;
      }
    }
    left--;
    left_last--;
  }
  cout << "YES" << endl;
  for (auto it : ans) {
    printf("%lld %c\n", it.first, it.second);
  }
  return 0;
}
