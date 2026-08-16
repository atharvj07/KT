import java.util.*;
import java.util.Map.Entry;
 
 
 class Main {
	 static int mod =  (int) (Math.pow(10,9)+7);
	 static List<ArrayList<Integer>>  list = new ArrayList<ArrayList<Integer>>();
    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        long[] a = new long[M];
        long[] b = new long[M];
        long[] m = new long[M];
        for (int i=0 ; i<M; i++) {
            a[i] = sc.nextLong();
            b[i] = sc.nextLong();
            for(int j=0;j<b[i];j++) {
            	m[i]=(long) (m[i]+Math.pow(2, sc.nextInt()-1));
            }
        }
        
        //2^12
        int[] dp=new int[(int) Math.pow(2, N)];
        for(int i=0;i<(int) Math.pow(2, N);i++)dp[i]=9999999;
        dp[0]=0;
        for(int i=1;i<Math.pow(2, N);i++) {
        	for(int j=0;j<M;j++) {
        		int tmp=0;
        		for(int k=0;k<=N;k++) {
        			if((i>>k)%2==1&&(m[j]>>k)%2==0) {
        				tmp=(int) (tmp+Math.pow(2, k));
        			}
        		}
        		if(tmp==i)continue;
        		dp[i]=(int) Math.min(dp[i], dp[tmp]+a[j]);
        	}
        }
        
        int ans=dp[(int) (Math.pow(2,N)-1)];
        if(ans==9999999) {
        	ans=-1;
        }
        System.out.println(ans);  	
               		
    }

}