#include <bits/stdc++.h>

using namespace std;
using LL = long long;
using VI = vector<int>;
using PI = pair<int, int>;

struct Dice {
	Dice() { d = new int[6]; }
	~Dice() { delete[] d; }

	void get() {
		for (int i = 0; i < 6; i++) {
			cin >> d[i];
		}
	}
	void roll(char c) {
		int t = d[0];
		int tmp = d[1];
		switch (c) {
		case 'N':
			d[0] = d[1]; d[1] = d[5]; d[5] = d[4]; d[4] = t;
			break;
		case 'S':
			d[0] = d[4]; d[4] = d[5]; d[5] = d[1]; d[1] = t;
			break;
		case 'W':
			d[0] = d[2]; d[2] = d[5]; d[5] = d[3]; d[3] = t;
			break;
		case 'E':
			d[0] = d[3]; d[3] = d[5]; d[5] = d[2]; d[2] = t;
			break;
		case 'r':
			d[1] = d[2]; d[2] = d[4]; d[4] = d[3]; d[3] = tmp;
			break;
		default:
			break;
		}
	}
	int top() { return d[0]; }
	int right() { return d[2]; }
	int front() { return d[1]; }
	int left() { return d[3]; }
	bool operator==(Dice & obj) {
		for (int i = 0; i < 6; i++) {
			if (this->d[i] != obj.d[i]) { return false; }
		}
		return true;
	}
	int* d;
};

int main() {
	Dice d[100];
	bool f = true;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		d[i].get();
	}
	for (int k = 1; k < n; k++) {
		for (auto & e : "WWWNNNN") {
			for (int i = 0; i < 4; i++) {
				if (d[0] == d[k]) {
					f = false;
				}
				d[k].roll('r');
			}
			d[k].roll(e);
		}
	}
	cout << (f ? "Yes" : "No") << endl;
	return 0;
}

