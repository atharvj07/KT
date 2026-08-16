

import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	    int N = sc.nextInt();
	    int M = sc.nextInt();
	    long A [] = new long [N];
	    
	    for(int i = 0; i < N; i++) {
	    	A[i]=sc.nextLong();
	    }
	    Arrays.sort(A);
	   
	    TreeMap <Long, Long> store = new TreeMap <Long, Long>();
	    
		long Bi=0;
		long Ci=0;
		for (int i = 0; i<M; i++){
			Bi = sc.nextLong();
			Ci = sc.nextLong();
 
			if (store.containsKey(Ci)) 
				store.put(Ci, store.get(Ci) + Bi);
			 else 
				store.put(Ci, Bi);
			}
		sc.close();
		int right = 0;
		
		while (store.isEmpty()==false) {
			
			long c=store.lastKey();
			long b=store.lastEntry().getValue();
			
			long count = 0;
			while (right<(long)(N) && A[right]<c && count<b){
				A[right]=c;
				right++;
				count++;
			}
			
			
			store.pollLastEntry();
		}
		long sum [] = new long [N+2];
		long current = 0;
		
	    for(int i = 0; i < N; i++) {
	    	current = A[i]+current;
	    	sum [i+1]=current;
	    }
	    System.out.println(sum[N]);
		
		
	}

}
