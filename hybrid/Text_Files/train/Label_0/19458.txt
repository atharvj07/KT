#include <bits/stdc++.h>
using namespace std;
 
int main()
{
	int d, n;
	cin >> d >> n;
	cout << (int)pow(100, d) * ((n == 100)?n + 1:n) << endl;
	return 0;
}