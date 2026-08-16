import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			int n = sc.nextInt();
			if (n == 0) return;
			
			List<Bridge> bridges = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				bridges.add(new Bridge(sc.nextInt(), sc.nextInt()));
			}
			Collections.sort(bridges);
			
			boolean flag = true;
			int bag = 0;
			for (int i = 0; i < n; i++) {
				Bridge b = bridges.get(i);
				bag += b.tre;
				if (bag > b.max) {
					flag = false;
					break;
				}
			}
			if (flag) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}
		}
	}
	
	static class Bridge implements Comparable<Bridge> {
		int tre, max;
		
		public Bridge(int tre, int max) {
			this.tre = tre;
			this.max = max;
		}
		
		@Override
		public int compareTo(Bridge b) {
			return this.max - b.max;
		}
		
	}
	
}