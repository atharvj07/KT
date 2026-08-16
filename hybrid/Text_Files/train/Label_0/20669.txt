#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <array>
#include <string>

using Int = long long int;
using std::array;
using std::string;
using std::vector;

template <int MOD>
class ModInt {
    using lint = long long;

public:
    int val;

    // constructor
    ModInt(lint v = 0) : val(v % MOD) {
        if (val < 0) val += MOD;
    };

    // assignment
    ModInt& operator=(const ModInt& x) {
        if (this != &x) { this->val = x.val; }
        return *this;
    }

    // unary operator
    ModInt operator+() const { return ModInt(val); }
    ModInt operator-() const { return ModInt(MOD - val); }
    ModInt operator~() const { return *this ^ (MOD - 2); }

    // increment / decrement
    ModInt& operator++() { return *this += 1; }
    ModInt& operator--() { return *this -= 1; }
    ModInt operator++(int) {
        ModInt before = *this;
        ++(*this);
        return before;
    }
    ModInt operator--(int) {
        ModInt before = *this;
        --(*this);
        return before;
    }

    // arithmetic
    ModInt operator+(const ModInt& x) const { return ModInt(*this) += x; }
    ModInt operator-(const ModInt& x) const { return ModInt(*this) -= x; }
    ModInt operator*(const ModInt& x) const { return ModInt(*this) *= x; }
    ModInt operator%(const ModInt& x) const { return ModInt(*this) %= x; }
    ModInt operator/(const ModInt& x) const { return ModInt(*this) /= x; }
    ModInt operator^(const ModInt& x) const { return ModInt(*this) ^= x; }

    // compound assignment
    ModInt& operator+=(const ModInt& x) {
        if ((val += x.val) >= MOD) val -= MOD;
        return *this;
    }
    ModInt& operator-=(const ModInt& x) {
        if ((val -= x.val) < 0) val += MOD;
        return *this;
    }
    ModInt& operator*=(const ModInt& x) {
        val = lint(val) * x.val % MOD;
        return *this;
    }
    ModInt& operator%=(const ModInt& x) {
        val %= x.val;
        return *this;
    }
    ModInt& operator/=(const ModInt& x) { return *this *= ~x; }
    ModInt& operator^=(const ModInt& x) {
        int n = x.val;
        ModInt b = *this;
        if (n < 0) n = -n, b = ~b;

        *this = 1;
        while (n > 0) {
            if (n & 1) *this *= b;
            n >>= 1;
            b *= b;
        }
        return *this;
    }

    // compare
    bool operator==(const ModInt& b) const { return val == b.val; }
    bool operator!=(const ModInt& b) const { return val != b.val; }
    bool operator<(const ModInt& b) const { return val < b.val; }
    bool operator<=(const ModInt& b) const { return val <= b.val; }
    bool operator>(const ModInt& b) const { return val > b.val; }
    bool operator>=(const ModInt& b) const { return val >= b.val; }

    // I/O
    friend std::ostream& operator<<(std::ostream& os, const ModInt& x) noexcept { return os << x.val; }
    friend std::istream& operator>>(std::istream& is, ModInt& x) noexcept { return is >> x.val; }
};

constexpr Int MOD = 1000000007;
using mint = ModInt<MOD>;

int main() {
    mint m;
    string s;
    std::cin >> m >> s;

    array<mint, 10> mods;
    for (char c : s) {
        for (auto& x : mods) x *= 10;
        mods[c - '0'] += 1;
    }

    int head = s.front() - '0';

    array<int, 10> perm;
    std::iota(perm.begin(), perm.end(), 0);
    do {
        // leading zero
        if (s.length() > 1 && perm[head] == 0) continue;

        mint x = 0;
        for (int i = 0; i < 10; ++i) {
            x += mods[i] * perm[i];
        }

        if (x == m) {
            for (char c : s) {
                std::cout << perm[c - '0'];
            }
            std::cout << std::endl;
            return 0;
        }
    } while (std::next_permutation(perm.begin(), perm.end()));

    std::cout << -1 << std::endl;
    return 0;
}

