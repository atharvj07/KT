
import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner as = new Scanner(System.in);
		int n = Integer.parseInt(as.next());
		int l = n;
		int[] a;
		int b = 0;
		int c = (int)Math.pow(2, n);
		a = new int[c];
		for(int i=0;i<c;i++){
			a[i]  = Integer.parseInt(as.next());
		}
		for(int s=0;s<n;s++){
			for(int i=0;i<(int)(Math.pow(2, l));i+=2){
				if(a[i]<a[i+1]){
					a[i+1]-=a[i];
					a[b]=a[i+1];
					b+=1;
				}else if(a[i]>a[i+1]){
					a[i]-=a[i+1];
					a[b]=a[i];
					b+=1;
				}else{
					a[b]=a[i];
					b+=1;
				}
			}
			l-=1;
			b = 0;
		}
		System.out.println(a[0]);
	}
}