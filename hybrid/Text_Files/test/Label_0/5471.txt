#include <iostream>

using namespace std;
static const int INF = 9999999;

void solve()
{
	int n, m;
	cin >> n >> m;
	int d[21][21];
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			d[i][j] = INF;
		}
	}
	char c;
	for(int i = 0; i < m; ++i)
	{
		int a1, b1, c1, d1;
		cin >> a1 >> c >> b1 >> c >> c1 >> c >> d1;
		--a1;
		--b1;
		d[a1][b1] = c1;
		d[b1][a1] = d1;
	}
	for(int k = 0; k < n; ++k)
	{
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
			{
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
	int x1, x2, y1, y2;
	cin >> x1 >> c >> x2 >> c >> y1 >> c >> y2;
	--x1;
	--x2;
	cout << y1 - y2 - d[x1][x2] - d[x2][x1] << endl;
}

int main()
{
	solve();
	return(0);
}