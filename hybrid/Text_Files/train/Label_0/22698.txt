#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int H, W,i,j,cnt=0;
	char map[50][51];
	cin >> H>>W;
	for (i = 0; i < H; i++)
	{
		for (j = 0; j < W; j++)
		{
			cin >> map[i][j];
		}
	}
	for (i = 0; i < H; i++)
	{
		for (j = 0; j < W; j++)
		{
			if (map[i][j] == '#' && map[i - 1][j] != '#' && map[i][j - 1] != '#' && map[i + 1][j] != '#' && map[i][j + 1] != '#')cnt++;
		}
	}
	if (cnt == 0)printf("Yes");
	else printf("No");
	return 0;
}