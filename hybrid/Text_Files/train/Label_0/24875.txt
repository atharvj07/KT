#include <iostream>
#define foreach(i,upper) for (int i = 0; i < upper; ++i)
using namespace std;

#define MAX_R 10
#define MAX_C 10000
int R, C;
bool os[MAX_R][MAX_C];

int main() {
	while (true) {
		cin >> R >> C;
		if (R == 0 && C == 0) break;
		foreach (i,R) foreach (j,C) cin >> os[i][j];
		int result = 0;
		foreach (mask, 1 << R) {
			int acc = 0;
			bool masks[MAX_R];
			foreach (i,R) { masks[i] = !! (mask & (1 << i)); }
			foreach (i,C) {
				int cnt = 0;
				foreach (j,R) {
					if (os[j][i] == masks[j]) { ++cnt; }
				}
				acc += max(cnt,R-cnt);
			}
			result = max(result,acc);
		}
		cout << result << endl;
	}
	return 0;
}