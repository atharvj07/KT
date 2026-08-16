
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

	static Scanner scanner;
	public static void main(String[] args) {
	    scanner = new Scanner(System.in);

	    int N=gi();
	    int M=gi();
	    long[] A=new long[M];
	    long[] B=new long[M];
	    Map<Long, Integer> map=new HashMap<Long, Integer>();

	    long sum=0;
	    for(int i=0; i<M; i++) {
	        A[i]=gl();
	        B[i]=gl();
	        if(A[i]==1) {
	        	if(map.containsKey(B[i])) {
	        		System.out.println("POSSIBLE");
                    return;
	        	} else {
	        		map.put(B[i], 0);
	        	}
	        }
	        if(B[i]==N) {
	        	if(map.containsKey(A[i])) {
	        		System.out.println("POSSIBLE");
                    return;
	        	} else {
	        		map.put(A[i], 0);
	        	}
	        }
	    }


		System.out.println("IMPOSSIBLE");
	}

	// 文字列として入力を取得
	public static String gs() {
		return scanner.next();
	}

	// intとして入力を取得
	public static int gi() {
		return Integer.parseInt(scanner.next());
	}

	// longとして入力を取得
	public static long gl() {
		return Long.parseLong(scanner.next());
	}

	// doubleとして入力を取得
	public static double gd() {
		return Double.parseDouble(scanner.next());
	}
}