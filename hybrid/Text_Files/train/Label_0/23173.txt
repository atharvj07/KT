#include <iostream>
#include <stdio.h>
using namespace std;


int walk(int, int);
char f[100][100];
int H, W;

int main(void){
	while (cin >> H >> W, (H || W)){
		for (int i = 0; i < H; i++){
			for (int j = 0; j < W; j++){
				cin >> f[i][j];
			}
		}
		walk(0, 0);
	}
}

int walk(int y, int x){
	switch (f[x][y]){
	case '.':
		printf("%d %d\n", y, x);
		break;
	case 'v':
		f[x][y]= 'a';
		walk(y, x+1);
		break;
	case '^':
		f[x][y] = 'a';
		walk(y, x-1);
		break;
	case '>':
		f[x][y] = 'a';
		walk(y+1, x);
		break;
	case '<':
		f[x][y] = 'a';
		walk(y-1, x);
		break;
	case 'a':
		printf("LOOP\n");
		break;

	}

	return 0;
}