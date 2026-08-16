import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		Integer[] cards = new Integer[N];
		for (int i = 0; i < cards.length; i++) {
			cards[i] = sc.nextInt();
		}
		Arrays.sort(cards, Comparator.reverseOrder());
		int ans = 0;
		for (int i = 0; i < K; i++) {
			ans += cards[i];
		}
		System.out.println(ans);
		sc.close();
	}
}