

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SMSC {
	static int n;
	
	public static void main(String[] args){
		FastScanner sc = new FastScanner();
		n = sc.nextInt();
		long time = 0;
		long size = 0;
		long largestSize = 0;
		int[] remain = new int[n+1];
		int[] jobsArrive = new int[n+1];
		int[] jobsLength = new int[n+1];
		for(int i=0;i<n;i++){
			jobsArrive[i] = sc.nextInt();
			jobsLength[i] = sc.nextInt();
		}
		jobsArrive[n] = Integer.MAX_VALUE;
		
		time = jobsArrive[0];
		remain[0] = jobsLength[0];
		size = jobsLength[0];
		largestSize = size;
		int lastTask = 0;
		int curTask = 0;
		while(curTask != n){
			largestSize = Math.max(size, largestSize);
			long consumption = Math.min(remain[curTask], jobsArrive[lastTask+1]-time);
			size -= consumption;
			time += consumption;
			remain[curTask] -= consumption;
			if(remain[curTask] == 0){
				curTask++;
			}
			
			if(curTask != n && (curTask > lastTask || jobsArrive[lastTask+1] == time)){
				//get new job
				lastTask++;
				remain[lastTask] = jobsLength[lastTask];
				size += jobsLength[lastTask];
				time = jobsArrive[lastTask];
			}
		}
		System.out.println(time + " " + largestSize);
	}
	
	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner(String s) {
			try {
				br = new BufferedReader(new FileReader(s));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String nextToken() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(nextToken());
		}

		long nextLong() {
			return Long.parseLong(nextToken());
		}

		double nextDouble() {
			return Double.parseDouble(nextToken());
		}
	}
}
