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

struct Swap {
	int a, b;
	int min() const { return std::min(a, b); }
	int max() const { return std::max(a, b); }
	int swap(int pos) const {
		if (a == pos) return b;
		if (b == pos) return a;
		return pos;
	}
};
class Replacer {
	std::vector<std::vector<std::vector<int>>> jump;
	std::vector<std::vector<int>> swap_history;
	std::vector<Swap> swap;
public:
	Replacer(const int n, const std::vector<Swap>& _swap) : jump(_swap.size(), std::vector<std::vector<int>>(2)), swap_history(n), swap(_swap) {
		for (auto t = 0; t < swap.size(); ++t) {
			swap_history[swap[t].a].push_back(t);
			swap_history[swap[t].b].push_back(t);
		}
		for (int t = swap.size() - 1; t >= 0; --t) {
			jump[t][0].push_back(swap[t].max());
			jump[t][1].push_back(swap[t].min());
			for (auto i = 1; (1 << i) + t <= swap.size(); ++i) {
				jump[t][0].push_back(move(swap[t].max(), t + 1, t + (1 << i) - 1));
				jump[t][1].push_back(move(swap[t].min(), t + 1, t + (1 << i) - 1));
			}
		}
	}
	int move(int pos, int s, int t) const {
		if (s == t) return swap[s].swap(pos);
		if (swap[s].swap(pos) == pos) {
			auto next = std::upper_bound(swap_history[pos].begin(), swap_history[pos].end(), s);
			if (next != swap_history[pos].end() && *next <= t) {
				return move(pos, *next, t);
			}
			else {
				return pos;
			}
		}
		else {
			auto idx = (swap[s].min() == pos) ? 0 : 1;
			auto next = 0;
			while ((1 << next) + s <= t && next < jump[s][idx].size()) ++next;
			--next;
			return move(jump[s][idx][next], s + (1 << next), t);
		}
	}
};


int main() {
	int n, k, q; std::cin >> n >> k >> q;
	std::vector<Swap> swap(k);
	for (auto& s : swap) {
		std::cin >> s.a>> s.b; --s.a; --s.b;
	}
	Replacer forward(n, swap);
	std::reverse(swap.begin(), swap.end());
	Replacer backward(n, swap);
	for (auto c = 0; c < q; ++c) {
		int type, s, t, x; std::cin >> type >> s >> t >> x; --s; --t; --x;
		switch (type) {
		case 1:
			std::cout << backward.move(x, k - t - 1, k - s - 1) + 1 << '\n';
			break;
		case 2:
			std::cout << forward.move(x, s, t) + 1 << '\n';
			break;
		default: throw 0;
		}
	}
}
