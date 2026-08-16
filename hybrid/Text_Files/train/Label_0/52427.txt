import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;


public class E {
	public void solve(){
		int MODULAR = 1000000007;
		
		PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a = new int[N];
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < N; i++){
			a[i] = sc.nextInt();
			max = Math.max( max, a[i]);
		}
		Arrays.sort(a);
				
		long ans = 0;
		for(int i = 1; i <= max; i++){
			ArrayList<Integer> factors = getFactors(i);
			int[] count = new int[ factors.size() ];
			int sum = 0;
		
			for(int j = factors.size()-1; j >= 0; j--){
				int c = bs(a, factors.get(j));				
				count[j] = c - sum;
				sum += count[j];				
			}			
			long tmp = 1;
			for(int j = 0; j < factors.size(); j++){
				if( j == factors.size() - 1){
					tmp = tmp * ( pow(j+1, count[j], MODULAR) - pow(j, count[j], MODULAR) + MODULAR) % MODULAR;
				}
				else{
					tmp = tmp * pow(j+1, count[j], MODULAR) % MODULAR;
				}				
			}
			ans = (ans + tmp) % MODULAR;
		}		
		ans = ans % MODULAR;
		out.println(ans);
		out.close();
	}
	
	public ArrayList<Integer> getFactors(int num){
		ArrayList<Integer> ret = new ArrayList<Integer>();
		for(int i = 1; i*i <= num; i++){
			if( num % i == 0) {
				ret.add(i);
				if( !ret.contains( num/i )){
					ret.add( num/i);
				}
			}			
		}
		Collections.sort(ret);
		return ret;
	}
	
//	public long pow(int n, int p, int mod){
//		if(p == 0) return 1;
//		if( p % 2 == 0) return pow( n*n%mod, p/2, mod);
//		return n * pow(n, p-1, mod) %mod;
//	}
	long pow(long a, int k, long mod) {
        if (k == 0) return 1;
        if (k % 2 == 0) return pow(a * a % mod, k / 2, mod);
        return a * pow(a, k - 1, mod) % mod;
	}
	
	public int bs(int[] a, int num){		
		int begin = 0;
		int end = a.length-1;
		
		if( begin == end ){
			if(a[begin] >= num)
				return 1;
			else
				return 0;			
		}
		
		int mid = begin;
		while( begin < end){
			mid = (begin + end) / 2;
			if( a[mid] >= num ){
				end = mid;
			}
			else{
				begin = mid+1;
			}
		}
		int ret = a.length - mid;
		if( a[mid] < num) ret--;
		return ret;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new E().solve();
	}

}
