#include <iostream>

int main() {
	int n, i, j;
	std::cin >> n >> i >> j;
	
	// i_forward = n - i, j_back = j - 1
	int first_way = ((n - i) + (j - 1)) % n;
	// i_back = i - 1, j_forward = n - j
	int second_way = ((i - 1) + (n - j)) % n;

	if (first_way > second_way)
		std::cout << second_way;
	else
		std::cout << first_way;

	return 0;
}