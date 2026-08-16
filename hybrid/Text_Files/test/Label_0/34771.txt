import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[][] result = null;
		for (int t = 0; t < n; t++) {
			char[] train = s.next().toCharArray();
			if (train.length > 1) {
				result = createTrainGraph(train);
				/* 先頭車両を決定する */
				int next = NO_CONNECTION;
				for (int i = 0; i < result.length; i++) {
					if (result[i][0] == NO_CONNECTION
							&& result[i][1] != NO_CONNECTION) {
						next = i;
					}
				}
				/* 出力 */
				while (next != -1) {
					System.out.printf("%c", next + 'a');
					next = result[next][REAR];
				}
				System.out.println();
			} else {
				System.out.println(train[0]);
			}
		}
	}

	static final int FRONT = 0;
	static final int REAR = 1;
	static final int NO_CONNECTION = -1;

	static int[][] createTrainGraph(char[] input) {
		int[][] train = new int[26][2];
		for (int i = 0; i < train.length; i++) {
			for (int j = 0; j < train[0].length; j++) {
				train[i][j] = NO_CONNECTION;
			}
		}
		boolean front = false;
		int before = input[0];
		for (int i = 1; i < input.length; i++) {
			int current = input[i];
			if ('a' <= current && current <= 'z') {
				if (front) {
					train[before - 'a'][FRONT] = current - 'a';
					train[current - 'a'][REAR] = before - 'a';
				} else {
					train[before - 'a'][REAR] = current - 'a';
					train[current - 'a'][FRONT] = before - 'a';
				}
				before = current;
			} else if (current == '>') {
				front = false;
			} else if (current == '<') {
				front = true;
			}
		}
		return train;
	}
}