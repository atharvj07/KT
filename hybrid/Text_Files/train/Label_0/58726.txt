import java.util.*;
import java.math.*;
import java.awt.geom.*;
import java.io.*;
    
    
public class Main {
	static int INF = 2 << 27;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int n = sc.nextInt();
			if(n == 0) break;
			int[] count = new int[3];
			int[] sum   = new int[3];
			for(int i = 0; i < n; i++) {
				String[] in = sc.next().split(":");
				if(in[0].equals("00")) {
					in[0] = "24";
				}
				if(in[0].equals("01")) {
					in[0] = "25";
				}
				int MM = sc.nextInt();
				int time = Integer.parseInt(in[0]) * 60 + Integer.parseInt(in[1]);
				
				int TIMEA = Integer.parseInt(in[0]) * 60 + MM - time;
				int TIMEB = Integer.parseInt(in[0]) * 60 + MM + 60 - time;
				int DIS   = (TIMEA < 0)?TIMEB:Math.min(TIMEA, TIMEB);
				if(time >= 11 * 60 && time <= 14*60 + 59) {
					count[0]++;
					if(DIS <= 8) {
						sum[0]++;
					}
				}
				else if(time >= 18 * 60 && time <= 20 * 60 + 59) {
					count[1]++;
					if(DIS <= 8) {
						sum[1]++;
					}
				}
				else if(time >= 21 * 60 && time <= 25 * 60 + 59) {
					count[2]++;
					if(DIS <= 8) {
						sum[2]++;
					}
				}
			}
			double A = 0;
			double B = 0;
			double C = 0;
			if(count[0] != 0) A = (sum[0]/(double)count[0]) * 100;
			if(count[1] != 0) B = (sum[1]/(double)count[1]) * 100;
			if(count[2] != 0) C = (sum[2]/(double)count[2]) * 100;
			
			int AA = (int)A;
			int BB = (int)B;
			int CC = (int)C;
			
			System.out.println("lunch " + ((count[0] == 0)?"no guest":AA));
			System.out.println("dinner " + ((count[1] == 0)?"no guest":BB));
			System.out.println("midnight " + ((count[2] == 0)?"no guest":CC));
			
		}
	}
}