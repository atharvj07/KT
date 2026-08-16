#include <algorithm>
#include <iostream>
#include <ostream>

void print_array(const int a[], int n) {
  for (int i = 0; i < n; ++i) {
    if (i > 0)
      std::cout << " ";
    std::cout << a[i];
  }
  std::cout << std::endl;
}

int main(int argc, char *argv[]) {
  int n;
  std::cin >> n;
  int a[10];
  for (int i = 0; i < n; ++i)
    std::cin >> a[i];

  if (std::prev_permutation(a, a + n))
    print_array(a, n);
  std::next_permutation(a, a + n);
  print_array(a, n);
  if (std::next_permutation(a, a + n))
    print_array(a, n);
}

