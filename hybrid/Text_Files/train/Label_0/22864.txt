#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	for(int t = 0; t < n; t++) {
		int s;
		cin >> s;
		cout << "Case " << t + 1 << ":" << endl;
		for(int i = 0; i < 10; i++) {
			s = s * s;
			s = (s / 100) % 10000;
			cout << s << endl;
		}
	}
}