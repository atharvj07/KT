#include <iostream>

#define BOARD_SIZE 10

void init(int a[BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) a[i] = 0;
}

void init(int a[][BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) {
		for (int j=0; j<BOARD_SIZE; j++) a[i][j] = 0;
	}
}

void copy(int a[][BOARD_SIZE], int b[][BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) {
		for (int j=0; j<BOARD_SIZE; j++) a[i][j] = b[i][j];
	}
}

bool next(int a[BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) {
		if (a[i] == 0) { a[i] = 1; return true; }
		a[i] = 0;
	}
	return false;
}

void point(int a[], int board[][BOARD_SIZE], int i, int j)
{
	board[i][j] = 1 - board[i][j];
	if (i>0) board[i-1][j] = 1 - board[i-1][j];
	if (i<BOARD_SIZE-1) board[i+1][j] = 1 - board[i+1][j];
	if (j>0) board[i][j-1] = 1 - board[i][j-1];
	if (j<BOARD_SIZE-1) board[i][j+1] = 1 - board[i][j+1];
}

bool isCorrect(int board[][BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) {
		for (int j=0; j<BOARD_SIZE; j++) {
			if (board[i][j] == 1) return false;
		}
	}
	return true;
}

void show(int a[][BOARD_SIZE])
{
	for (int i=0; i<BOARD_SIZE; i++) {
		std::cout << a[i][0];
		for (int j=1; j<BOARD_SIZE; j++) {
			std::cout << " " << a[i][j];
		}
		std::cout << std::endl;
	}
}

bool check(int a[], int board[][BOARD_SIZE], int ans[][BOARD_SIZE])
{
	for (int j=0; j<BOARD_SIZE; j++) {
		if (a[j] == 1) { point(a, board, 0, j); ans[0][j] = 1; }
	}
	
	for (int i=1; i<BOARD_SIZE; i++) {
		for (int j=0; j<BOARD_SIZE; j++) {
			if (board[i-1][j] == 1) { point(a, board, i, j); ans[i][j] = 1; }
		}
	}
	return isCorrect(board);
}

int main()
{
	int board[BOARD_SIZE][BOARD_SIZE];
	int board_cpy[BOARD_SIZE][BOARD_SIZE];
	int a[BOARD_SIZE];
	int ans[BOARD_SIZE][BOARD_SIZE];
	int n; std::cin >> n;
	for (int k=0; k<n; k++) {
		for (int i=0; i<BOARD_SIZE; i++) {
			for (int j=0; j<BOARD_SIZE; j++) std::cin >> board[i][j];
		}
		init(a);
		do {
			init(ans);
			copy(board_cpy, board);
			if (check(a, board_cpy, ans)) { show(ans); break; }
		} while (next(a));
	}
	
	return 0;
}


