#include <string>
#include <vector>
#include <iostream>
using namespace std;
string s;
int main() {
	cin >> s;
	vector<int> v;
	int ptr = 0;
	while (ptr < s.size()) {
		if (s[ptr] == 'c') v.push_back(0), ptr += 7;
		else v.push_back(1), ptr += 3;
	}
	v.push_back(v.back());
	int p = 0, m = 0, ret = -1;
	for (int i = 1; i < v.size(); i++) {
		if (v[i - 1] == v[i]) {
			int sa = i - p; p = i;
			if (sa > m) m = sa, ret = v[i - 1];
		}
	}
	cout << (ret ? "egg" : "chicken") << endl;
	return 0;
}