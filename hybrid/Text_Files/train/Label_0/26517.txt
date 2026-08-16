#include <iostream>

const int DAYS[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

struct Date {
	int y;
	int m;
	int d;
	Date() {}
	Date(int y, int m, int d) : y(y), m(m), d(d) {}
};

bool isLeap(int y)
{
	if (y % 400 == 0) return true;
	else if (y % 100 == 0) return false;
	else if (y % 4 == 0) return true;
	else return false;
}

int countRestDays(int y, int m, int d)
{
	int res = DAYS[m-1] - d + 1;
	for (int i=m; i<12; i++) {
		res += DAYS[i];
	}
	if (isLeap(y) && m <= 2) res++;
	return res;
}

int main()
{
	int y1, m1, d1, y2, m2, d2;
	while (std::cin >> y1 >> m1 >> d1 >> y2 >> m2 >> d2) {
		if (y1==-1) break;
		int res = countRestDays(y1, m1, d1);
		for (int y=y1+1; y<=y2; y++) {
			res += isLeap(y) ? 366 : 365;
		}
		res -= countRestDays(y2, m2, d2);
		std::cout << res << std::endl;
	}
	return 0;
}


