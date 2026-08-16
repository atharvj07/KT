import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int count1 = -1;
		int count2 = 0;
		while (n > 0) {
		    count2 += n % 2;
		    n >>= 1;
		    count1++;
		}
		System.out.println(Math.max(count1, count2));
	}
}

