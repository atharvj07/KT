#include <iostream>
using namespace std;

int main () {
	int sharps = 0;
	int H, W;
	char a;
	cin >> H >> W;
	for(int i = 0; i < H; i++)
	{
		for(int j = 0; j < W; j++)
		{
			cin >> a;
			if(a == '#') sharps++;
		}
	}
	if(sharps == H + W - 1) {
		cout << "Possible" << endl;
	}else {
		cout << "Impossible" << endl;
	}
}