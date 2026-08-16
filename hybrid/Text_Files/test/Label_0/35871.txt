import java.util.*;
import java.math.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int y1 = sc.nextInt(), m1 = sc.nextInt(), d1 = sc.nextInt();
		int y2 = sc.nextInt(), m2 = sc.nextInt(), d2 = sc.nextInt();
		boolean mdsame = m1==m2 && d1==d2;
		int diff = Math.abs(y1-y2)+1;
		if(mdsame) {
			System.out.println(diff-1);
			return;
		}
		if(y1 < y2) {
			if(dmcomp(m1,d1,m2,d2)) {
				//
			} else {
				diff-=1;
			}
		} else if(y1 > y2) {
			if(!dmcomp(m1,d1,m2,d2)) {
				//
			} else {
				diff-=1;
			}
		} else if(y1==y2) {
			System.out.println(1);
			return;
		}

		System.out.println(diff);
	}

	static boolean dmcomp(int m1,int d1,int m2,int d2) {
		return 100*m1+d1 < 100*m2+d2;
	}
}
