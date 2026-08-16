import java.util.*;
public class Main{
	public static void main(String [] args){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n=sc.nextInt();
			int a[]=new int [n];
			int b[]=new int [n];
			int count=0;
			if(n==0)break;
			for(int i=0;i<n;i++){
				a[i]=sc.nextInt();
				b[i]=a[i];

			}
			Arrays.sort(b);
			while(!judge(a,b)){
				for(int i=1;i<a.length;i++){
					//System.err.println(count);
					int temp=0;
					if(a[i-1]>a[i]){
						temp=a[i];
						a[i]=a[i-1];
						a[i-1]=temp;
						count++;
					}
				}
			}
			 System.out.println(count);
		}

	}

	static boolean judge(int a[],int b[]){
		boolean judge=true;
		for(int i=0;i<a.length;i++){
			if(a[i]!=b[i]){
				judge=false;
			}
		}
		if(judge){
			return true;
		}
		return false;
	}
}