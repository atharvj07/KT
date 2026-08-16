import java.util.HashMap;
import java.util.Scanner;

public class ABChess {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int white = 0;
		int black = 0;

		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		map.put('Q', 9);
		map.put('R', 5);
		map.put('N', 3);
		map.put('B', 3);
		map.put('P', 1);
		map.put('K', 0);
		map.put('q', 9);
		map.put('r', 5);
		map.put('n', 3);
		map.put('b', 3);
		map.put('p', 1);
		map.put('k', 0);

		for (int j = 0; j < 8; j++) {
			String line = scanner.nextLine();
			for (int i = 0; i < line.length(); i++) {
				char c = line.charAt(i);

				if (c == '.' || c == 'k' || c == 'K')
					continue;

				if (c > 'a')
					black += map.get(c);
				else
					white += map.get(c);
			}

		}

		if (black > white)
			System.out.println("Black");
		if (white > black)
			System.out.println("White");
		if (white == black)
			System.out.println("Draw");
	}
}
