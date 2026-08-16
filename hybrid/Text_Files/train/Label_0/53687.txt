import java.util.*;
import java.io.PrintWriter;
public class Main{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int k=sc.nextInt();
		double[] a=new double[n];
		double[] tmp=new double[n];
		long ans=0;
		for(int i=0; i<n; i++){
			a[i]=sc.nextInt()-k;
			if(i!=0){
				a[i]+=a[i-1];
			}
			tmp[i]=a[i];
			if(tmp[i]>=0){
				ans++;
			}
		}
		Arrays.sort(tmp);
		for(int i=0; i<n; i++){
			a[i]=-Arrays.binarySearch(tmp,a[i]+0.1);
		}
		BIT b=new BIT(n+1);
		for(int i=0; i<n; i++){
			ans+=b.get((int)a[i]);
			b.add((int)a[i]);
		}
		System.out.println(ans);
	}
	static class BIT{
		int n;
		int[] data;
		BIT(int n){
			this.n=n;
			data = new int[n+1];
		}
		void add(int i){
			for(;i<=n;i+=i&(-i))data[i]++;
		}
		int get(int i){
			int res = 0;
			for(;i>0;i-=i&(-i))res+=data[i];
			return res;
		}
	}
}
