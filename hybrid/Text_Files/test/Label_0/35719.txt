import java.util.*;
import static java.util.Arrays.*;
import static java.lang.Math.*;

// AOJ 0027
public class Main {

	static Scanner sc = new Scanner(System.in);
	static int M, D;
	static final String[] ss = {
		"Thursday",
		"Friday",
		"Saturday",
		"Sunday",
		"Monday",
		"Tuesday",
		"Wednesday"
	};
	static final int[] is = {
		31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
	};
	
	public static void main(String[] args) {
		while (true) {
			M = sc.nextInt(); D = sc.nextInt();
			if (M == 0 && D == 0) break;
			int ds = 0;
			for (int i = 1; i < M; i++) {
				ds += is[i - 1];
			}
			
			ds += D - 1;
			System.out.println(ss[ds % 7]);
		}

	}
}