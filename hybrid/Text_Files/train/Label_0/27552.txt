/**
    Lost Arrow (Aryan V S)
    Wednesday 2020-11-25
**/

#ifdef LOST_IN_SPACE
#  if   __cplusplus > 201703LL
#    include "lost_pch1.h" // C++20
#  elif __cplusplus > 201402LL
#    include "lost_pch2.h" // C++17
#  else
#    include "lost_pch3.h" // C++14
#  endif
#else
#  include <bits/stdc++.h>
#endif

namespace competitive_programming::utility {

    class timer {
      private:
        std::chrono::time_point <std::chrono::steady_clock> begin, end;
      public:
#ifdef LOST_IN_SPACE
         timer () : begin (std::chrono::steady_clock::now()), end () { }
        ~timer () {
            end = std::chrono::steady_clock::now();
            std::cerr << "\n\nDuration: " << std::chrono::duration <double> (end - begin).count() << "s\n";
        }
#else
         timer () : begin (), end () { }
        ~timer () { }
#endif
    };
}

constexpr bool test_cases = true;

auto solve () -> void {
    int64_t d, k;
    std::cin >> d >> k;

    int64_t x = 0, y = 0, which = 1;
    while (true) {
        if (which & 1) {
            if ((x + k) * (x + k) + y * y <= d * d)
                x += k;
            else break;
        }
        else {
            if (x * x + (y + k) * (y + k) <= d * d)
                y += k;
            else break;
        }
        ++which;
    }

    std::cout << ((which + 1) & 1 ? "Ashish" : "Utkarsh") << '\n';
}

int main () {

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.precision(10);
    std::cerr.precision(10);
    std::cout << std::fixed << std::boolalpha;
    std::cerr << std::fixed << std::boolalpha;

    competitive_programming::utility::timer t;
    int32_t cases = 1;
    if (test_cases)
        std::cin >> cases;
    while (cases--)
        solve();

    return 0;
}

// g++.exe -Wall -Weffc++ -Wextra -pedantic -std=c++20 -g -D_GLIBCXX_DEBUG -DLOST_IN_SPACE -H
