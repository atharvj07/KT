#include <bits/stdc++.h>
int N, alf[26];
long long ans;
std::string s;
std::map<int, int> m[27];
int main() {
  std::cin >> N;
  for (int i = 0; i < N; ++i) {
    std::cin >> s;
    for (int j = 0; j < 26; ++j) alf[j] = 0;
    for (int j = 0; j < s.size(); ++j) {
      ++alf[s[j] - 'a'];
    }
    int odd = 0, flag = 0;
    for (int j = 0; j < 26; ++j)
      if (alf[j] % 2) {
        ++odd;
        flag += 1 << j;
      }
    m[odd][flag]++;
  }
  if (m[0].size()) ans = 1LL * (m[0][0] - 1) * m[0][0] / 2LL;
  for (int odd = 1; odd < 26; ++odd) {
    for (auto el : m[odd]) {
      int flag = el.first;
      int cnt = el.second;
      ans += 1LL * (cnt - 1) * cnt / 2LL;
      for (int i = 0; i < 26; ++i) {
        if (flag & (1 << i)) {
          if (m[odd - 1].count(flag - (1 << i))) {
            ans += 1LL * cnt * m[odd - 1][flag - (1 << i)];
          }
        }
      }
    }
  }
  std::cout << ans;
  return 0;
}
