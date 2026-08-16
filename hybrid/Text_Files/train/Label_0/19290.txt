#include <cstdio>

int main() {
	int I, O, J, L, x;
	scanf("%d%d%*d%d%d", &I, &O, &J, &L);
	x = I % 2 + J % 2 + L % 2;
	printf("%lld\n", (long long)O + I + J + L - (I && J && L && x > 1 ? 3 - x : x));
	return 0;
}