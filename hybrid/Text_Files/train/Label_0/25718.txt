#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char *argv[]) {
  int x, y;

  while (cin >> x >> y) {
    int tmp;

    if (x < y) {
      tmp = y;
      y = x;
      x = tmp;
    }
    while (x % y != 0) {
      tmp = x % y;
      x = y;
      y = tmp;
    }
    cout << y << endl;
  }
  return 0;
}