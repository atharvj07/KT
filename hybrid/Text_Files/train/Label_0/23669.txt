#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

int main()
{
	int N;
	int X, Y, Z;
	cin >> N; 
	cin >> X;
	vector<int> a(X,0);
	for (int i = 0; i < X; i++)
		cin >> a[i];

	cin >> Y;
	vector<int> b(Y,0);
	for (int i = 0; i < Y; i++)
		cin >> b[i];

	cin >> Z;
	vector<int> c(Z,0);
	for (int i = 0; i < Z; i++)
		cin >> c[i];

	int conf = 0;
	int i = 0;
	int j = 0;
	int k = 0;
	bool fnd = false;
	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < Z; j++) {
			if (b[i] == c[j]) {
				fnd = true;
				b.erase(b.begin() + i);
				i--;
				Y--;
				c.erase(c.begin() + j);
				j--;
				Z--;
				conf++;

			}
		}
	}
	for (int i = 0; i < X; i++) {
		for (int j = 0; j < Z; j++) {
			if (a[i] == c[j]) {
				c.erase(c.begin() + j);
				j--;
				Z--;
			}
		}
	}
	cout << conf + c.size() << endl;
	int m;
	cin >> m;
	return 0;

}