import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();

		int v[]=new int[n+1];
		int c[]=new int[n+1];
		for(int i=1;i<=n;i++){
			v[i]=sc.nextInt();
		}
		for(int i=1;i<=n;i++){
			c[i]=sc.nextInt();
		}
int ans=0;
		for(int i=1;i<=n;i++){
			if(v[i]-c[i]>=0){
			ans=ans+v[i]-c[i];
			}
		}
		System.out.println(ans);

	}
}