#include<iostream>
#include<cmath>

using namespace std;

typedef long long ll;

ll A, B;

int main() {
	cin >> A >> B;
	for (ll i = 1; i <= A; i++) {
		ll gaku = ceil(i * (long double)B / (long double)A) * A;
		if ((gaku % B) + (gaku / B) > gaku / A) {
			cout << gaku << endl;
			return 0;
		}
	}
	cout << -1 << endl;
	return 0;
}
