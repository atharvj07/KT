#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	string s, comp[2] = { "JOI", "IOI" };
	
	while (cin >> s) {
		for (int k = 0; k < 2; ++k) {
			int ans = 0;
			for (int i = 0; (i = s.find(comp[k], i)) != string::npos; ++i) {
				ans++;
			}
			cout << ans << endl;
		}
	}

	return 0;
}