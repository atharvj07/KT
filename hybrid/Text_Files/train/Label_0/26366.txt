#include<iostream>
#define m 52000
using namespace std;

bool ba[m+1] = { true };
int cp(int x) {
	int co = 0;
	for (int i = 0; i < m+1; i++) {
		ba[i] = { true };
	}
	for (int i = 2; i*i <= 52000; i++) {
		if (ba[i]) {
			for (int j = i*i; j <= 52000; j += i) {
				ba[j] = { false };
			}
		}
	}
	for (int i = 2; i <x; i++) {
		if (ba[i]) {
			co = i;
		}
	}
	return co;
}

int main() {
	int n;
	while (cin >> n) {
		int a = cp(n);
		while (ba[n + 1] == false) {
			n++;
		}
		cout << a << ' ' << n + 1 << endl;
	}
	return 0;
}