#include <iostream>
#include <bitset>

int main()
{	
	std::bitset<64> bs(0);
	
	int q; std::cin >> q;
	for (int i=0; i<q; i++) {
		int op, k;
		std::cin >> op;
		switch (op) {
		case 0:
			std::cin >> k;
			std::cout << bs.test(k) << std::endl;
			break;
		case 1:
			std::cin >> k;
			bs.set(k);
			break;
		case 2:
			std::cin >> k;
			bs.reset(k);
			break;
		case 3:
			std::cin >> k;
			bs.flip(k);
			break;
		case 4:
			std::cout << bs.all() << std::endl;
			break;
		case 5:
			std::cout << bs.any() << std::endl;
			break;
		case 6:
			std::cout << bs.none() << std::endl;
			break;
		case 7:
			std::cout << bs.count() << std::endl;
			break;
		case 8:
			std::cout << bs.to_ullong() << std::endl;
			break;
		}
	}
	return 0;
}

