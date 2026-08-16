#include <bits/stdc++.h>
using namespace std;

int main() {
	ios :: sync_with_stdio(false);
	string s;
	while(getline(cin, s)) {
		for(int t = 0; t < 26; t ++) {
			for(auto &c : s) if(isalpha(c)){
				c = (c - 'a' + 1) % 26 + 'a';
			}
			if(s.find("the") != -1 ||
				s.find("this") != -1 ||
				s.find("that") != -1) {
				cout << s << '\n';
				break;
			}
		}
	}
	return 0;
}