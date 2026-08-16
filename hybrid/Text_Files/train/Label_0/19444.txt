#include <iostream>
using namespace std;

int main()
{
	int a, b, n;
	while (cin >> a >> b >> n)
	{
		int ans = 0;
		a = 10 * (a % b);
		
		while (n--)
		{
			ans += a / b;
			a = 10 * (a % b);
		}
		cout << ans << endl;
	}

	return 0;
}