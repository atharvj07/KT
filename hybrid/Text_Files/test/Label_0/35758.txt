import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int w = sc.nextInt();
		int h = sc.nextInt();
		int t = sc.nextInt();
		int[][] field = new int[h][w];
		int p = sc.nextInt();
		for (int i = 0; i < p; i++) {
		    int ww = sc.nextInt();
		    int hh = sc.nextInt();
		    int tt = sc.nextInt();
		    field[hh][ww]++;
		}
		long total = 0;
		for (int i = 0; i < h; i++) {
		    for (int j = 0; j < w; j++) {
		        if (sc.nextInt() == 1) {
		            total += field[i][j];
		        }
		    }
		}
	    System.out.println(total);
	}
}

