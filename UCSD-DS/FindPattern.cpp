#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using std::string;
typedef unsigned long long ull;
constexpr auto MOD_P = 18446744073709551589;

struct Data {
    string pattern, text;
};

Data read_input() {
    Data data;
    std::cin >> data.pattern >> data.text;
    return data;
}

void print_occurrences(const std::vector<ull>& output) {
    for (size_t i = 0; i < output.size(); ++i)
        std::cout << output[i] << " ";
    std::cout << "\n";
}

std::vector<ull> get_occurrences(const Data& input) {
    const string& s = input.pattern, t = input.text;
    //std::vector<int> ans;
    //for (size_t i = 0; i + s.size() <= t.size(); ++i)
    //    if (t.substr(i, s.size()) == s)
    //        ans.push_back(i);

    std::vector<ull> ans;
    ull pattern_hash = 0;
    ull randomval = 4;
    for (ull i = 0; i < s.length(); i++) {
        pattern_hash += ((s[s.length() - 1 - i] % MOD_P) * (static_cast<ull>(std::pow(randomval, i)) % MOD_P)) % MOD_P;
    }

    ull substr_hash = 0;
    for (ull i = 0; i < t.length(); i++) {
        std::cout << i << " " << pattern_hash << " " << substr_hash << "\n";
        if (i != 0 && i >= s.length()) {
            if (substr_hash == pattern_hash) {
                if (t.substr(i - s.length(), s.length()) == s) {
                    ans.push_back(i - s.length());
                }
            }
            substr_hash -= ((t[i-s.length()] % MOD_P) * (static_cast<ull>(std::pow(randomval, (s.length() - 1))) % MOD_P)) % MOD_P;
            substr_hash *= randomval;
            substr_hash %= MOD_P;
            substr_hash += static_cast<ull>(t[i]) % static_cast<ull>(MOD_P);
            continue;
        }
        substr_hash += ((t[i] % MOD_P) * (static_cast<ull>(std::pow(randomval, (s.length() - static_cast<ull>(i % s.length()) - 1))) % MOD_P)) % MOD_P;
    }

    if (substr_hash == pattern_hash) {
        if (t.substr(t.length() - s.length(), s.length()) == s) {
            ans.push_back(t.length() - s.length());
        }
    }

    return ans;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    print_occurrences(get_occurrences(read_input()));
    return 0;
}
