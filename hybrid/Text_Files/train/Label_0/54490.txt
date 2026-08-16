import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt(),b=sc.nextInt();
		int n=a+b+1;
		if(a>0){
			int ind=n-a+1;
			System.out.print(1);
			for(int i=ind;i<=n;++i)System.out.print(" "+i);
			while(b-->0)System.out.print(" "+--ind);
			
		}
		else{
			for(int i=n;i>1;--i)System.out.print(i+" ");
			System.out.print(1);
		}
		System.out.println();
		sc.close();
	}

}
