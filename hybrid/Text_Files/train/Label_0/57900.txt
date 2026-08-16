import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class VasyaMagic {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] ns = bf.readLine().split(" ");
		int n,d,l;
		n = Integer.parseInt(ns[0]);
		d = Integer.parseInt(ns[1]);
		l = Integer.parseInt(ns[2]);
		int a,b;
		if(n%2==0){
			b = n/2;
			a = b;
		}
		else{
			b = n/2;
			a = b+1;
		}
		int x = 0,y = 0;
		int sumPos = 0,sumNeg = 0;
		for(int i = a;i<=a*l;i++)
			for(int j = b;j<=b*l;j++){
				if(i-j==d){
					x = i;
					y = j;
					for(int k = 0;k<n;k++){
						if(k%2==0){
							System.out.print(((x-sumPos)/a)+" ");
							sumPos += (x-sumPos)/a;
							a--;
						}
						else{
							System.out.print(((y-sumNeg)/b)+" ");
							sumNeg += (y-sumNeg)/b;
							b--;
						}
					}
					return;
				}
			}
		System.out.println(-1);
	}
}
