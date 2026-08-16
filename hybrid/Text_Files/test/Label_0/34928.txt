import java.util.Scanner;

public class Main {

	Scanner sc = new Scanner(System.in);

	void run() {
		while (true) {
			if (!sc.hasNext()) {
				break;
			}
			char[] str = sc.next().toCharArray();
			boolean flag = false;
			for (int i = 0; i < str.length; i++) {
				if (i == str.length - 1) {
					flag = true;
					break;
				}
				switch (str[i]) {
				case 'A':
					if (str[i + 1] != 'B' && str[i + 1] != 'D') {
						i = str.length;
					}
					break;
				case 'B':
					if (str[i + 1] != 'A' && str[i + 1] != 'C'
							&& str[i + 1] != 'E') {
						i = str.length;
					}
					break;
				case 'C':
					if (str[i + 1] != 'B' && str[i + 1] != 'F') {
						i = str.length;
					}
					break;
				case 'D':
					if (str[i + 1] != 'A' && str[i + 1] != 'E'
							&& str[i + 1] != 'G') {
						i = str.length;
					}
					break;
				case 'E':
					if (str[i + 1] != 'D' && str[i + 1] != 'B'
							&& str[i + 1] != 'F' && str[i + 1] != 'H') {
						i = str.length;
					}
					break;
				case 'F':
					if (str[i + 1] != 'C' && str[i + 1] != 'E'
							&& str[i + 1] != 'I') {
						i = str.length;
					}
					break;
				case 'G':
					if (str[i + 1] != 'D' && str[i + 1] != 'H') {
						i = str.length;
					}
					break;
				case 'H':
					if (str[i + 1] != 'G' && str[i + 1] != 'E'
							&& str[i + 1] != 'I') {
						i = str.length;
					}
					break;
				case 'I':
					if (str[i + 1] != 'F' && str[i + 1] != 'H') {
						i = str.length;
					}
					break;
				}
			}
			if (flag) {
				System.out.println(str);
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}

}