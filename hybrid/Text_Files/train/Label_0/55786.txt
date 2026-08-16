import java.util.Scanner;

class Main {
	public static void main (String[] args) {
		Scanner scanner = new Scanner(System.in);
		int X = scanner.nextInt();
		int max = 1;

		for (int i = 1; i <= X; i++) {
			for (int j = 2; j <= X; j++) {
				double expo = Math.pow(i,  j);
				if (expo > X) {
					break;
				}

				if (max < expo) {
					max = (int)expo;
				}
				//System.out.println(i + "^" + j + "=" + (int)expo);
			}
		}
		System.out.println(max);
	}
}
