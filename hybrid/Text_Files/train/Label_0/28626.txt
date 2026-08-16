//#include <D:\Programming\template\gp1.h>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;

int main() {

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;

		vi a(n), b(n), d(n);
		vi pos, neg;
		int tmp = 0;
		for (int i = 0; i < n; i++) cin >> a[i];
		for (int i = 0; i < n; i++) cin >> b[i];
		for (int i = 0; i < n; i++) {
			d[i] = a[i] - b[i];
			tmp += d[i];
			if (d[i] > 0)pos.push_back(i);
			else if (d[i] < 0)neg.push_back(i);
		}

		vector<pii> out;
		if (tmp != 0) cout << "-1" << endl;
		else {
			while (!pos.empty()) {
				while (d[pos.front()] != 0) {

					out.push_back(make_pair(pos.front() + 1, neg.front() + 1));
					d[pos.front()]--;
					d[neg.front()]++;
					if (d[neg.front()] == 0) neg.erase(neg.begin());
				}
				pos.erase(pos.begin());
			}
			cout << out.size() << endl;
			for (auto &p : out) cout << p.first << ' ' << p.second << endl;
		}
	}
	return 0;
}