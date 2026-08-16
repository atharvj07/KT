#include <algorithm>
#include <deque>
#include <cstdio>

using namespace std;

int main() {

	double i;
	deque<double> n;

	while(scanf("%lf", &i)!=EOF)
		n.push_back(i);

	sort(n.begin(), n.end());
	printf("%.1f\n", *n.rbegin()-*n.begin());

	return 0;

}