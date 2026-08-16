#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<unordered_map>
#include<unordered_set>
#include<random>
#include<set>
#include<assert.h>
#include<string>
#include<time.h>
using namespace std;
using lld = long long int;
using ulld = unsigned long long int;
using pii = pair<int, int>;
using pli = pair<lld, int>;
using lf = double;
using pff = pair<lf, lf>;
int n, m;
int z[26][6] = {
	{1,0, 0,0, 0,0},
	{1,0, 1,0, 0,0},
	{1,1, 0,0, 0,0},
	{1,1, 0,1, 0,0},
	{1,0, 0,1, 0,0},

	{1,1, 1,0, 0,0},
	{1,1, 1,1, 0,0},
	{1,0, 1,1, 0,0},
	{0,1, 1,0, 0,0},
	{0,1, 1,1, 0,0},

	{1,0, 0,0, 1,0},
	{1,0, 1,0, 1,0},
	{1,1, 0,0, 1,0},
	{1,1, 0,1, 1,0},
	{1,0, 0,1, 1,0},

	{1,1, 1,0, 1,0},
	{1,1, 1,1, 1,0},
	{1,0, 1,1, 1,0},
	{0,1, 1,0, 1,0},
	{0,1, 1,1, 1,0},

	{1,0, 0,0, 1,1},
	{1,0, 1,0, 1,1},
	{0,1, 1,1, 0,1},
	{1,1, 0,0, 1,1},
	{1,1, 0,1, 1,1},

	{1,0, 0,1, 1,1},
};
int a[26][6];
void inil() {
	int i, j, k;
	for (i = 0; i < 26; i++) {
		a[i][0] = z[i][0] + z[i][1];
		a[i][1] = z[i][2] + z[i][3];
		a[i][2] = z[i][4] + z[i][5];
		a[i][3] = z[i][0] + z[i][2] + z[i][4];
		a[i][4] = z[i][1] + z[i][3] + z[i][5];
	}
}
int main() {
	inil();
	int t = 100, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--) {
		int n;
		int b[5];
		for (i = 0; i < 5; i++) {
			scanf("%d", &b[i]);
		}
		for (k = 0; k < 26; k++) {
			for (j = 0; j < 5; j++) {
				if (a[k][j] != b[j])break;
			}
			if (j == 5) {
				printf("%c", k + 'a');
				break;
			}
		}
	}
	printf("\n");
}