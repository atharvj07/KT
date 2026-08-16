#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	int a, l, x;
	
	while (scanf("%d %d %d", &a, &l, &x) == 3){
		double s1 = (a + 2 * l) / 2.0;
		double s2 = (x + 2 * l) / 2.0;
		double m = (l + x) / 2.0;
		
		s1 = sqrt(s1 * (s1 - a) * (s1 - l) * (s1 - l));
		s2 = 2 * sqrt(s2 * (s2 - m) * (s2 - m) * (s2 - l));
		
		printf("%lf\n", s1 + s2);
	}
	
	return (0);
}