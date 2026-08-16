#include <iostream>
#include <string>
using namespace std;

int main() {
	string S;
	int w;
	cin >> S >> w;
	for (int i = 0; i < S.size(); i++) {
		if (i % w == 0) {
			cout << S[i];
		}
	}
}