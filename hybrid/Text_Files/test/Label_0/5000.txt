#include <cstdio>
#include <vector>
using namespace std;

typedef struct P {
	int p, d;
	bool operator<(const P &r) {
		return d < r.d;
	}
} P;
int n;;

int main(){
	int p, d1, d2;
	while (true) {
		scanf("%d", &n);
		if (n == 0) break;
		P m = { 0,-1 };
		P t;
		for (int i = 0; i < n; i++) {
			scanf("%d %d %d", &p, &d1, &d2);
			t = { p,d1 + d2 };
			if (m < t) {
				m = t;
			}
		}
		printf("%d %d\n", m.p, m.d);
	}

	return 0;
}