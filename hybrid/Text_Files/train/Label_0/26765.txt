#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

int main() {
	int x, h;
	while (cin >> x >> h) {
		if (x == 0 && h == 0) break;
		printf("%.6lf\n", x * x + hypot(x / 2.0, h) * x * 2.0);
	}
}