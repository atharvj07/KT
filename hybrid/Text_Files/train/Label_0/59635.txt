import java.util.*;
import java.io.*;
public class EdE {
	static long num = 998244353;
	public static void main(String[] args) throws Exception{
		

		// TODO Auto-generated method stub
 		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
 		PrintWriter out = new PrintWriter(System.out);
 		StringTokenizer st = new StringTokenizer(bf.readLine());
 		int n = Integer.parseInt(st.nextToken());
 		int k = Integer.parseInt(st.nextToken());
 		PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
 		StringTokenizer st1 = new StringTokenizer(bf.readLine());
 		for(int j =0;j<n;j++){
 			int number = Integer.parseInt(st1.nextToken());
 			pq.add(new Pair(number, 1));
 		}
 		for(int j = 0;j<k-n;j++){
 			Pair nu = pq.remove();
 			Pair p = new Pair(nu.number, nu.priority+1);
 			pq.add(p);
 		}
 		
 		long sum = 0;
 		while(!pq.isEmpty()){
 			Pair ns = pq.remove();
 			sum+=(long)(ns.totalDiff(ns.priority));
 		}
 		
 		
 		out.println(sum);
	 		
 		out.close();
 		
 		
 		
 	}
	static class Pair implements Comparable<Pair>{
		private int number;
		private int priority;
		public Pair(int number, int priority){
			this.number = number;
			this.priority = priority;
		}
		public int compareTo(Pair other){
			long val1 = totalDiff(priority)-totalDiff(priority+1);
			long val2 = other.totalDiff(other.priority) - other.totalDiff(other.priority+1);
			return Long.compare(val2,  val1);
		}
		public long totalDiff(int priority){
			int one = number%priority;
			int zero = priority-number%priority;
			
			return (long)(zero)*(long)(number/priority)*(long)(number/priority) + (long)(one)*(long)(number/priority+1)*(long)(number/priority+1);
		}
	}
}
 	
 
//StringJoiner sj = new StringJoiner(" "); 
//sj.add(strings)
//sj.toString() gives string of those stuff w spaces or whatever that sequence is

 		
 		
 		
 		
	


