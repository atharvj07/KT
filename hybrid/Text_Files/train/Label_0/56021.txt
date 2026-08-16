import java.util.*;
import java.io.*;
public class A644 {

	public static void main(String[] args) {
		Scanner s=new  Scanner(System.in);
		int t =s.nextInt();
		while(t-->0) {
			int n=s.nextInt();
			int a[]=new int[n];
			for (int i=0;i<n;i++) {
				a[i]=s.nextInt();
			}
			Arrays.sort(a);
			int o=0,e=0;
			for(int i=0;i<n;i++) {
				if(a[i]%2==0)e++;
				else o++;
			}
			if(o%2==0 && e%2==0) {
				System.out.println("YES");
			}else {
				boolean f=false;
				for(int i=n-1;i>0;i--) {
					if(a[i]-a[i-1]==1) {
						f=true;
						break;
					}
				}
				if(f) {
				System.out.println("YES");
				}
				else {
					System.out.println("NO");
				}
			 }
		}
	}

}
