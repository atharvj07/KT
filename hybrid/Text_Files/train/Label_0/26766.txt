#include <iostream>
#include <cmath>

using namespace std;

void solve()
{
	double x, h;
	while(cin >> x >> h, x || h)
	{
		double Sum = x * x;
		double Height = sqrt(h * h + (x / 2) * (x / 2));
		Sum += Height * x * 2;
		printf("%.6f\n", Sum);
	}
}

int main()
{
	solve();
	return(0);
}