#include<iostream>
using namespace std;
int main() {
	int l;
	while (cin >> l&&l != 0) {
		int m = 0, n = 0, g=10000;
		bool h = false;
		for (int i = 0; i < 12; i++) {
			int a, b;
			cin >> a >> b;
			a -= b;
			m++;
			n += a;
			if (n >= l&&h == false) {
				g = m;h = true;
			}
		}
		if (g == 10000)
			cout << "NA" << endl;
		else {
			cout << g << endl;
		}
	}
}