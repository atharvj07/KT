#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int rank[128];
	for(int i = 2; i <= 9; ++i)
		rank[i + '0'] = i;

	rank['T'] = 10;
	rank['J'] = 11;
	rank['Q'] = 12;
	rank['K'] = 13;
	rank['A'] = 14;

	string cards[4][13];

	for(char trump; cin >> trump, trump != '#';) {
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 13; ++j)
				cin >> cards[i][j];

		int win[2] = {};
		int first = 0;
		for(int i = 0; i < 13; ++i) {
			int mx = 0, winner;
			char led = cards[first][i][1];
			for(int j = 0; j < 4; ++j) {
				const int player = (first + j) % 4;
				const string& card = cards[player][i];
				int score = rank[card[0]];
				if(card[1] == trump)
					score += 100;

				else if(card[1] == led)
					score += 50;

				if(mx < score) {
					mx = score;
					winner = player;
				}

			}

			++win[winner & 1];
			first = winner;
		}

		if(win[1] > win[0])
			cout << "EW " << win[1] - 6 << endl;
		else
			cout << "NS " << win[0] - 6 << endl;
	}

	return EXIT_SUCCESS;
}