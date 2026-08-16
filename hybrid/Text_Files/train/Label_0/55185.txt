import java.math.BigInteger;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int count = 0;
		for(int i = 0; i < n; i++) {
			int s = sc.nextInt();
			boolean ok = false;
			for(int j = 1; j*j <= s+1; j++) {
				if((s - j) % (1 + 2 * j) == 0) {
					ok = true;
					break;
				}
			}
			if(!ok) count++;
		}
		System.out.println(count);
	}
}