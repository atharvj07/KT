#include <iostream>
#define rep(i, n) for(i = 0; i < n; i++)
using namespace std;

int n, q, a, b;
bool flag[100002];

int main() {
	cin >> n >> q;
	int i, pos = 1;
	
	flag[1] = flag[2] = true;
	rep(i, q) {
		cin >> a >> b;
		if (pos == a) pos = b;
		else if (pos == b) pos = a;
		swap(flag[a], flag[b]);
		flag[pos-1] = flag[pos] = flag[pos+1] = true;
	}
	
	int ans = 0;
	rep(i, n) ans += flag[i+1];
	cout << ans << endl;
	return 0;
}