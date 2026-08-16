import java.util.*;
public class Study{
	public static boolean ispossible(long mid,long arr[]) {
		long supervisor=0;
		for(int i=0;i<arr.length;i++) {
			if(mid-arr[i]<0)
				return false;
			supervisor+=mid-arr[i];}
		
		if(supervisor>=mid)
			return true;
		return false;
	}
	public static long bsearch(long arr[],long sum) {
		long l=0;
		long r=sum;
		long answer=sum;
		while(l<=r){
			long mid=(l+r)/2;
			if(ispossible(mid,arr)) {
				answer=mid;
				r=mid-1;}
			else
				l=mid+1;
		}
		return answer;
	}
	public static void main(String args[]) {
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		long arr[]=new long[n];
		long sum=0;
		for(int i=0;i<arr.length;i++) {
			arr[i]=in.nextInt();
			sum+=arr[i];}
		long ans=bsearch(arr,sum);
		System.out.println(ans);
	}
}