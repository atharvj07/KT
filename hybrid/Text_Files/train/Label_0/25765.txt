#include <vector>
#include <iostream>
using namespace std;
const vector<int> dir = { 0, 1, 0, -1 };
int Q, x;
int main() {
	cin >> Q;
	while (Q--) {
		vector<int> a(10);
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cin >> x; a[i] |= x << j;
			}
		}
		for (int i = 0; i < 1 << 10; i++) {
			vector<int> b = a, c(10); c[0] = i;
			for (int j = 0; j < 10; j++) {
				if (i & (1 << j)) {
					for (int k = 0; k < 4; k++) {
						int tx = dir[k], ty = j + dir[k ^ 1];
						if (0 <= tx && tx < 10 && 0 <= ty && ty < 10) {
							b[tx] ^= 1 << ty;
						}
					}
					b[0] ^= 1 << j;
				}
			}
			for (int j = 0; j < 9; j++) {
				c[j + 1] = b[j];
				for (int k = 0; k < 10; k++) {
					if (b[j] & (1 << k)) {
						for (int l = 0; l < 4; l++) {
							int tx = j + 1 + dir[l], ty = k + dir[l ^ 1];
							if (0 <= tx && tx < 10 && 0 <= ty && ty < 10) {
								b[tx] ^= 1 << ty;
							}
						}
						b[j + 1] ^= 1 << k;
					}
				}
			}
			if (b[9] == 0) {
				for (int j = 0; j < 10; j++) {
					for (int k = 0; k < 10; k++) {
						if (k) cout << ' ';
						cout << ((c[j] & (1 << k)) ? 1 : 0);
					}
					cout << endl;
				}
			}
		}
	}
	return 0;
}