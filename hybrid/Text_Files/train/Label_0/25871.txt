#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int i, n, s=0, m=0, a[25];
	cin >> n;
	for (i=0; i<n; i++)
	{
		cin >> a[i];
		if (a[i]>=m)
		{
			m=a[i];
			s++;
		}
	}
	cout << s << endl;
	return 0;
}