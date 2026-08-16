#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)

struct Box { double x, y, r; };

const double EPS = 1e-9;

void solve(int n) {
	vector< double > h, w;
	vector< Box > vb;
	
	for_(i,0,n) {
		double x, y, r;
		cin >> x >> y >> r;
		vb.push_back(Box{x, y, r});
		h.push_back(y - r);
		h.push_back(y + r);
		w.push_back(x - r);
		w.push_back(x + r);
	}
	
	sort(h.begin(), h.end());
	sort(w.begin(), w.end());
	
	h.erase(unique(h.begin(), h.end()), h.end());
	w.erase(unique(w.begin(), w.end()), w.end());
	
	int H = h.size(), W = w.size();
	double ans = 0;
	
	for_(i,0,H-1) for_(j,0,W-1) {
		double lx = w[j], rx = w[j + 1];
		double ly = h[i], ry = h[i + 1];
		
		for_(k,0,n) {
			Box b = vb[k];
			
			if (b.x - b.r < lx + EPS &&
				b.y - b.r < ly + EPS &&
				b.x + b.r > rx - EPS &&
				b.y + b.r > ry - EPS) {
				ans += (rx - lx) * (ry - ly);
				break;
			}
		}
	}
	
	cout << setprecision(2) << setiosflags(ios::fixed) << ans << endl;
}

int main() {
	int case_number = 0, n;
	
	while (cin >> n, n) {
		++case_number;
		cout << case_number << " ";
		solve(n);
	}
}