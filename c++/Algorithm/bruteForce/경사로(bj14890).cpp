#include <iostream>

using namespace std;
int N, L;
int board[100][100];

int main() {
	cin >> N >> L;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cin >> board[i][j];
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cout << board[i][j];
		cout << '\n';
	}
}