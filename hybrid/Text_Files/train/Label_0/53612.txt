import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner in = new  Scanner(System.in);
		int loop = in.nextInt();
		for(int i=0; i<loop; i++) {
			int[] ball = new int[10];
			boolean judge = true;
			for(int j=0; j<10; j++) ball[j] = in.nextInt();
			int b, c;
			b = ball[0];
			c = 0;
			for(int j=1; j<10; j++) {
				if(b < c) { //常にcのが小さくなる
					int tmp = b;
					b = c;
					c = tmp;
				}
				if(ball[j] > b) b = ball[j];
				else if(ball[j] > c) c = ball[j];
				else {
					System.out.println("NO");
					judge = false;
					break;
				}
			}
			if(judge) System.out.println("YES");
		}
	}
}