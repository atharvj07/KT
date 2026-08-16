#include <iostream>
#include <vector>
#include <array>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <bitset>
#include <memory>
#include <cmath>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <numeric>
#include <climits>
#include <cfloat>
#include <cassert>
#include <random>
int main() {
	int n, m; std::cin >> n >> m;
	std::vector<std::queue<int>> queues(n);
	for (auto i = 0; i < m; ++i) {
		int type, second_info; std::cin >> type >> second_info;
		int min = INT_MAX;
		switch (type) {
		case 0:
			std::cout << queues[second_info - 1].front() << '\n';
			queues[second_info - 1].pop();
			break;
		case 1:
			for (auto j = 0; j < queues.size(); ++j) {
				min = std::min(min, (int)queues[j].size());
			}
			for (auto& queue : queues) {
				if (queue.size() == min) {
					queue.push(second_info);
					break;
				}
			}
			break;
		default: throw 0;
		}
	}
}
