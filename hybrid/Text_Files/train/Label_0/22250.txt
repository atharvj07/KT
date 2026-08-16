#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

const int N = 40005;
const long double eps = 1e-8;

struct Point {
	long double x, y;
	
	void read() {
		cin >> x >> y;
		//scanf("%lf%lf", &x, &y);
	}
};
long double mat[25][25];

int n;
Point p[N];

long double sqr(long double x) {
	return x * x;
}

void init() {
	cin >> n;
	for (int i = 1; i <= n; i ++) {
		p[i].read();
	}
}

void gauss() {
	for (int i = 1; i <= 3; i ++) {
		int best;
		long double cc = -5.0;
		
		for (int j = i; j <= 3; j ++) {
			if (abs(mat[j][i]) > cc) {
				cc = abs(mat[j][i]);
				best = j;
			}
		}
		for (int j = 1; j <= 4; j ++) {
			swap(mat[i][j], mat[best][j]);
		}
		
		for (int j = i + 1; j <= 3; j ++) {
			if (abs(mat[j][i]) > eps) {
				long double t = mat[i][i] / mat[j][i];
				for (int k = 1; k <= 4; k ++) {
					mat[j][k] *= t;
				}
				for (int k = 1; k <= 4; k ++) {
					mat[j][k] -= mat[i][k];
				}
			}
		}
	}
	
	long double ans[5];
	for (int i = 3; i >= 1; i --) {
		if (abs(mat[i][i]) > eps) {
			ans[i] = mat[i][4] / mat[i][i];
		} else {
			ans[i] = 0.0;
		}
		for (int j = i - 1; j >= 1; j --) {
			mat[j][4] -= mat[j][i] * ans[i];
		}
	}
	
	for (int i = 1; i <= 3; i ++) {
		printf("%.6f%c", (double)ans[i], i == 3 ? '\n' : ' ');
	}
}

void work() {
	for (int i = 1; i <= n; i ++) {
		long double tmp[6];
		tmp[1] = p[i].x, tmp[2] = p[i].y;
		tmp[3] = 1.0, tmp[4] = p[i].x * p[i].x + p[i].y * p[i].y;
		
		for (int j = 1; j <= 4; j ++) {
			mat[1][j] += tmp[j] * p[i].x;
		}
		for (int j = 1; j <= 4; j ++) {
			mat[2][j] += tmp[j] * p[i].y;
		}
		for (int j = 1; j <= 4; j ++) {
			mat[3][j] += tmp[j];
		}
	}
	for (int i = 1; i <= 3; i ++) {
		mat[i][4] *= -1.0;
	}
	
	gauss();
}

int main() {
	//freopen("A.in", "r", stdin);
	//ios::sync_with_stdio(false);
	
	init(), work();
	
	return 0;
}