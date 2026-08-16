#include <bits/stdc++.h>
template <typename T>
void swap(T &l, T &r) {
  T tmp = l;
  l = r;
  r = tmp;
}
template <typename T>
void bubble_sort(std::vector<T> &vct) {
  for (int i = 0; i != vct.size(); ++i) {
    for (int j = 0; j != vct.size() - 1; ++j) {
      if (vct[j] > vct[j + 1]) {
        swap(vct[j], vct[j + 1]);
      }
    }
  }
}
int main() {
  std::size_t amount;
  std::cin >> amount;
  std::vector<int> vct;
  for (std::size_t i = 0; i != amount; ++i) {
    int tmp;
    std::cin >> tmp;
    vct.push_back(tmp);
  }
  bubble_sort(vct);
  int n{};
  for (std::size_t i = 0; i != vct.size(); i += 2) {
    n += vct[i + 1] - vct[i];
  }
  std::cout << n;
  return 0;
}
