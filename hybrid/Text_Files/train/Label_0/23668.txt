#include <bits/stdc++.h>

using namespace std;

int N, X, Y, Z;
bool Data[3][100];

void solve() {
	int sum;

	sum = 0;
	for (int i = 0; i < N; ++i) {
		if ((!Data[0][i] && Data[2][i]) || (Data[1][i] && Data[2][i])) {
			++sum;
		}
	}
	cout << sum << endl;
}

int main() {
	int num;

	memset(Data, false, sizeof(Data));
	cin >> N >> X;
	for (int i = 0; i < X; ++i) {
		cin >> num;
		Data[0][num - 1] = true;
	}
	cin >> Y;
	for (int i = 0; i < Y; ++i) {
		cin >> num;
		Data[1][num - 1] = true;
	}
	cin >> Z;
	for (int i = 0; i < Z; ++i) {
		cin >> num;
		Data[2][num - 1] = true;
	}
	solve();

	return 0;
}

