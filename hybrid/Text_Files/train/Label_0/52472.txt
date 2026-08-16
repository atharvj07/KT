import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	try {
    		final int N = sc.nextInt();
    		int K = sc.nextInt();
    		StringBuilder S = new StringBuilder(sc.next());
    		boolean firstTime = true;
    		int step = 1;

    		while (K > 0) {
    			StringBuilder T = new StringBuilder(S.toString());
    			T.reverse();
    			StringBuilder revU = new StringBuilder(S.toString() + T.toString());
    			revU.reverse();
    			String sDash = S.toString();
    			for (int i=N; i>=0; i-=step) {
    				String tmp = revU.substring(i, i+N);
    				if (sDash.compareTo(tmp) > 0) {
    					sDash = tmp;
    				} else {
    					if (!firstTime) {
        					break;
    					}
    				}
    			}
				if (firstTime) {
					firstTime = false;
					if (Math.pow(2, K) > N) {
						char c = sDash.charAt(0);
						for (int i=0; i<N; i++) {
							System.out.print(c);
						}
						System.out.println();
						System.exit(0);
					}
				} else {
					step += step;
				}

    			K--;
    			S = new StringBuilder(sDash);
    			S.reverse();
    		}
    		System.out.println(S.reverse());

    	} finally {
    		sc.close();
    	}
    }
/*
    public static int compareTo(String value, String anotherString, int step) {
        int len1 = value.length();
        int len2 = anotherString.length();
        int lim = Math.min(len1, len2);
        char v1[] = value.toCharArray();
        char v2[] = anotherString.toCharArray();

        int k = 0;
        while (k < lim) {
        	System.out.print(lim + " / ");
        	System.out.println(k);
            char c1 = v1[k];
            char c2 = v2[k];
            if (c1 != c2) {
                return c1 - c2;
            }
            k+=step;
        }
        return len1 - len2;
    }
    */
}

