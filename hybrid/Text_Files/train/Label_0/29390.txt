#include <iostream>
#include <algorithm>
using namespace std; 
int n;
long long la, lb, k;
void solve() {
	int a, b;
	cin >> n;
	la = lb = 1;
	for(int i = 0; i < n; ++i)
	{
		cin >> a >> b;
		k = (la + a - 1) / a;
		k = max(k, (lb + b - 1) / b);
		la = a * k;
		lb = b * k;
	}
}



int main() {
	solve();
	cout << la + lb << endl;
	return 0;
}