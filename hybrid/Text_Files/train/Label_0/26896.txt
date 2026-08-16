#include <iostream>
#include <bitset>

const int ms = 8080;
const int mv = ms * 2 + 10;

std::bitset<mv> bits[2];

int main() {
	std::string str;
	int x, y;
	std::cin >> str >> x >> y;
	int state = 0;
	bits[0][ms] = bits[1][ms] = true;
	int on = 0;
	while(on < str.size() && str[on] == 'F') {
		on++;
	}
	bits[0] <<= on;
	int get = 0;
	//std::cout << "got here on " << on << "\n";
	for(; on < str.size(); on++) {
		//std::cout << "on " << on << ", state is " << state << "\n";
		/*for(int j = 0; j < 2; j++) {
			for(int k = 0; k < mv; k++) {
				if(bits[j][k]) {
					//std::cout << "(" << j << ", " << k - ms << ")\n";
				}
			}
		}*/
		if(str[on] == 'T') {
			bits[state] = (bits[state] >> get) | (bits[state] << get);
			get = 0;
			state = 1 - state;
		} else {
			get++;
		}
	}
	bits[state] = (bits[state] >> get) | (bits[state] << get);
	if(bits[0][ms + x] && bits[1][ms + y]) {
		std::cout << "Yes\n";
	} else {
		std::cout << "No\n";
	}
}