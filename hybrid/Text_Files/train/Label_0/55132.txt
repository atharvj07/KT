import java.util.*;
class Main {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = Integer.parseInt(sc.next());
	int m = Integer.parseInt(sc.next());
	int[] ax = new int[n];
	int[] ay = new int[n];
	int[] bx = new int[m];
	int[] by = new int[m];

	for(int i = 0; i<n; i++) {
	    ax[i] = Integer.parseInt(sc.next());
	    ay[i] = Integer.parseInt(sc.next());
	}

	for(int i = 0; i<m; i++) {
            bx[i] = Integer.parseInt(sc.next());
            by[i] = Integer.parseInt(sc.next());
        }

	int min = Integer.MAX_VALUE;
	int minI = 0;

	for(int i = 0; i<n; i++) {
	    min= Integer.MAX_VALUE;
	    for(int j = 0; j<m; j++) {
		int manhattan = (int)Math.abs(ax[i]-bx[j]) + (int)Math.abs(ay[i]-by[j]);
		if(manhattan < min ) {
		    min = manhattan;
		    minI = j+1;
		}
	    }
	    System.out.println(minI);
	}

    }
}