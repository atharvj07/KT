import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int a[]=new int[n];
		for(int i=0;i<n;i++){
			a[i]=s.nextInt();
		}
		int max=a[1]-a[0];
		int min=a[0];
		for(int j=2;j<n;j++){
			min=Math.min(min,a[j-1]);
			int sub;
			sub=a[j]-min;
			if(sub>max) max=sub;
		}
		System.out.println(max);
	}
}
