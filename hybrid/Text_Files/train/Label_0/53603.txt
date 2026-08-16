import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		long A, B, C, D;
		for (int i = 0; i < n; i++) {
			A = scn.nextLong();
			B = scn.nextLong();
			C = scn.nextLong();
			D = scn.nextLong();
			boolean can = true;
			if (A < B) {
				can = false;
			} else {
				if (D < B) {
					can = false;
				}else {
					if (D % B == 0) {
						if (A % B > C)
							can = false;
					} else {
						long a = A % B;
						long b = D % B;
						b = yu(B,b);
						long buf = (B-a-1)/b;
						if((b * buf + a > C && B > b * buf + a) || b * (buf-1) + a > C) {
							can = false;
						}
					}
				}
			}
			System.out.println(can ? "Yes" : "No");
		}
		scn.close();
	}

	public static long yu(long a,long b) {
		long buf;
		while(a%b !=0) {
			buf = a%b;
			a = b;
			b = buf;
		}
		return b;
	}

}
