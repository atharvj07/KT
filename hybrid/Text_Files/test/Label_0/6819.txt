#include <cmath>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int number[10];
int table[15][15];

bool check(int x)
{
	for (int i = 4; i >= 1; --i)
		number[i] = x % 10, x /= 10;

	number[5] = 0;	// check number

	for (int i = 1; i <= 4; ++i)
		number[5] = table[number[5]][number[i]];

	/*
	cout << "number" << endl;
	for (int i = 1; i <= 5; ++i)
		cout << number[i] << " ";
	cout << endl;
	*/

	//	error1

	for (int i = 1; i <= 5; ++i)
		for (int j = 0; j < 10; ++j)
			if (j != number[i])
			{
				int tmp = 0;

				for (int k = 1; k <= 5; ++k)
				{
					if (k == i)
						tmp = table[tmp][j];
					else
						tmp = table[tmp][number[k]];
				}

				if (!tmp)return true;
			}

	//	error2

	for (int i = 1, j = 2; i <= 4; ++i, ++j)
		if (number[i] != number[j])
		{
			int tmp = 0;

			for (int k = 1; k <= 5; ++k)
			{
				if (k == i)
					tmp = table[tmp][number[j]];
				else if (k == j)
					tmp = table[tmp][number[i]];
				else
					tmp = table[tmp][number[k]];
			}

			if (!tmp)return true;
		}

	return false;
}

signed main(void)
{
	for (int i = 0; i < 10; ++i)
		for (int j = 0; j < 10; ++j)
			cin >> table[i][j];

	int answer = 0;

	for (int i = 0; i < 10000; ++i)
		if (check(i))++answer;

	cout << answer << endl;
}