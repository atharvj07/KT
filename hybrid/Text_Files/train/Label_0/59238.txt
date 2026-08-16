import java.util.*;
public class GFG {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		ArrayList<Integer> arr=new ArrayList<Integer>();
	    while (n>0)
	    {
	        int n1=n,a=0,b=1;
	        while(n1>0)
	        {
	            if(n1%10!=0)a+=b;
	            b*=10;n1/=10;
	        }
	        n-=a;arr.add(a);
	    }
	    System.out.println(arr.size());
	    Collections.sort(arr);
	    for(int i:arr)
	    System.out.print(i+" ");
	}
}