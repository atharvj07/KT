import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static char tramp;
	static char[][] suit = new char[13][4];
	static int[][] num = new int[13][4];

	public static void main(String[] args) {
		while (true) {
			tramp = sc.next().charAt(0);
			if (tramp == '#') break;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 13; ++j) {
					String card = sc.next();
					num[j][i] = num(card.charAt(0));
					suit[j][i] = card.charAt(1);
				}
			}
			int parent = 0;
			int[] score = new int[2];
			for (int i = 0; i < 13; ++i) {
				int winner = parent;
				for (int j = 1; j < 4; ++j) {
					int player = (parent + j) % 4;
					if (win(suit[i][winner], num[i][winner], suit[i][player], num[i][player])) {
						winner = player;
					}
				}
				score[winner % 2]++;
				parent = winner;
			}
			System.out.println((score[0] > score[1] ? "NS " : "EW ") + (Math.max(score[0], score[1]) - 6));
		}
	}

	static boolean win(char ps, int pn, char cs, int cn) {
		if (ps == cs) return pn < cn;
		return cs == tramp;
	}

	static int num(char c) {
		if (c == 'T') return 10;
		if (c == 'J') return 11;
		if (c == 'Q') return 12;
		if (c == 'K') return 13;
		if (c == 'A') return 14;
		return c - '0';
	}
}