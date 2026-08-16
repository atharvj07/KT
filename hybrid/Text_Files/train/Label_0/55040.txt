import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			int n = sc.nextInt();
			if (n == 0) {
				break;
			}
			int[] hand = new int[n];
			int pool = 0;
			String card = sc.next();
			for(int i=0;i<100;i++) {
				int turn = i % n;
				switch (card.charAt(i)) {
				case 'M':
					hand[turn]++;
					break;
				case 'S':
					pool += hand[turn] + 1;
					hand[turn] = 0;
					break;
				case 'L':
					hand[turn] += pool + 1;
					pool = 0;
					break;
				}
			}
			Arrays.sort(hand);
			StringBuilder sb = new StringBuilder();
			for(int i=0;i<n;i++) {
				if (i > 0) {
					sb.append(" ");
				}
				sb.append(hand[i]);
			}
			sb.append(" " + pool);
			System.out.println(sb.toString());
		}
	}

}