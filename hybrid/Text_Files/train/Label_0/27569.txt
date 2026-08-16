#include <iostream>
using namespace std;

int main() {
	int A, B, C, ans = 0, sum = 0;
	cin >> A >> B >> C;
	while (C > sum) {
		++ans;
		sum += A;
		if (ans % 7 == 0) sum += B;
	}
	cout << ans << endl;
}
