import java.util.*;
import java.math.*;
import java.awt.geom.*;
import java.io.*;
    
    
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Time> list = new ArrayList<Time>();
		int k = sc.nextInt();
		for(int i = 0; i < k; i++) {
			list.add(new Time(sc.next()));
		}
		int n = sc.nextInt();
		Time[][] C = new Time[n][];
		for(int i = 0; i < n; i++) {
			int K = sc.nextInt();
			C[i] = new Time[K];
			for(int j = 0; j < K; j++) {
				C[i][j] = new Time(sc.next());
			}
		}
		int m = sc.nextInt();
		Time[][] S = new Time[m][];
		for(int i = 0; i < m; i++) {
			int K = sc.nextInt();
			S[i] = new Time[K];
			for(int j = 0; j < K; j++) {
				S[i][j] = new Time(sc.next());
			}
		}
		int[] countA = new int[list.size()];
		int[] countB = new int[list.size()];
		for(int i = 0; i < list.size(); i++) {
			for(int j = 0; j < n; j++) {
				for(int K = 0; K < C[j].length; K++) {
					if(C[j][K].coverTo(list.get(i))) {
						countA[i]++;
						break;
					}
				}
			}
		}
		for(int i = 0; i < list.size(); i++) {
			for(int j = 0; j < m; j++) {
				for(int K = 0; K < S[j].length; K++) {
					if(S[j][K].coverTo(list.get(i))) {
						countB[i]++;
						break;
					}
				}
			}
		}
		int sum = 0;
		for(int i = 0; i < list.size(); i++) {
			sum += Math.min(countA[i], countB[i]);
		}
		System.out.println(sum);
		
	}
	
	static class Time implements Comparable<Time> {
		int startTime;
		int endTime;
		@Override
		public int compareTo(Time o) {
			if(this.startTime == o.startTime) return this.endTime - o.endTime;
			return this.startTime - o.startTime;
		}
		public Time(String a) {
			String[] A = a.split("-");
			String[] BA = A[0].split(":");
			String[] BB = A[1].split(":");
			startTime = Integer.parseInt(BA[0]) * 60 + Integer.parseInt(BA[1]);
			endTime   = Integer.parseInt(BB[0]) * 60 + Integer.parseInt(BB[1]);
		}
		public boolean coverTo(Time o) {
			return (this.startTime <= o.startTime && this.endTime >= o.endTime);
		}
	}
}