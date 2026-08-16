#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
map<string,int>mp;
int main() {
	int q;
	cin >> q;
	while (q--) {
		int Q;
		cin >> Q;
		string s;
		int x;
		switch (Q) {
		case 0:
			cin >> s >> x;
			mp[s] = x;
			break;
		case 1:
			cin >> s;
			cout << mp[s] << endl;
			break;
		case 2:
			cin >> s;
			mp.erase(s);
		}
	}
	return 0;
}
