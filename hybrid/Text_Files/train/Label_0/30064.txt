#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;
static const double EPS = 1e-8;
typedef long long ll;


const int MAX = 100000;
const int mod = 100000007;

int dp5[MAX + 5], dp3[MAX + 3];
int dpp5[MAX + 6], dpp3[MAX + 4];

char buf[MAX + 1];

int main()
{
	dp5[0] = dp3[0] = 1;
	for (int i = 0; i < MAX; ++i)
	{
		for (int j = 1; j <= 5; ++j)
			(dp5[i + j] += dp5[i]) %= mod;
		for (int j = 1; j <= 3; ++j)
			(dp3[i + j] += dp3[i]) %= mod;
	}
	for (int i = 1; i <= MAX; ++i)
	{
		dpp5[i + 5] = ((dpp5[i] += dp5[i]) %= mod);
		dpp3[i + 3] = ((dpp3[i] += dp3[i]) %= mod);
	}

	while (scanf("%s", buf), *buf != '#')
	{
		char* p = buf;
		ll res = 1;

		char c = '@';
		int count = 1;
		do
		{
			if (*p == c)
				++count;
			else
			{
				if (c != '8' && c != '0')
					res *= dpp5[count];
				else
					res *= dpp3[count];

				res %= mod;
				c = *p;
				count = 1;
			}
		} while (*p++ != '\0');

		printf("%d\n", res);
	}

	return 0;
}