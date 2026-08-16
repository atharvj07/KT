import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int w = sc.nextInt();
		PriorityQueue<Long> qH = new PriorityQueue<>();
		PriorityQueue<Long> qW = new PriorityQueue<>();
		for (int i = 0; i < h; i++) {
		    qH.add(sc.nextLong());
		}
		for (int i = 0; i < h; i++) {
		    qW.add(sc.nextLong());
		}
		long total = 0;
		while (qH.size() > 0 && qW.size() > 0) {
		    if (qH.peek() > qW.peek()) {
		        total += qH.size() * qW.poll();
		    } else {
		        total += qW.size() * qH.poll();
		    }
		}
        System.out.println(total);
	}
}

