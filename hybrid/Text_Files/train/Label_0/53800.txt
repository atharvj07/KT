import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int d = sc.nextInt();
		long count = 0;
	    int current = 0;
	    int state = 1;
	    long total = 0;
	    for (int i = 0; i < n; i++) {
	        int time = sc.nextInt();
	        int floor = sc.nextInt();
	        if (state - 1 + floor - 1 <= time - current) {
	            total += count * (state - 1);
	            count = 1;
	            current = time;
	            state = floor;
	        } else if (Math.abs(floor - state) <= time - current) {
	            total += count * (time - current);
	            count++;
	            current = time;
	            state = floor;
	            if (count > d) {
	                System.out.println(-1);
	                return;
	            }
	        } else {
	            System.out.println(-1);
	            return;
	        }
	    }
	    total += count * (state - 1);
		System.out.println(total);
	}
}

