import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int q = sc.nextInt();
		int idx = 0;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < q; i++) {
		    int type = sc.nextInt();
		    int k = sc.nextInt();
		    if (type == 0) {
		        int out = (idx + k) % n;
		        if (out == 0) {
		            out = n;
		        }
		        sb.append(out).append("\n");
		    } else {
		        idx = (idx + k) % n;
		    }
		}
		System.out.print(sb);
	}
}

