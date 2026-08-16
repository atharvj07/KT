import java.io.*;
import java.util.*;

public class Main{
	
	public static void main(String[] args){
		solve();
	}
	
	public static void solve(){
		Scanner sc = new Scanner(System.in);
		int z = sc.nextInt();
		int x = z;
		int a = x/1000;
		x -= x/1000*1000;
		int b = x/100;
		x -= x/100*100;
		int c = x/10;
		x -= x/10*10;
		int ans = 0;
		int[] count = new int[3];
		for(int i=0;i<2;i++){
			for(int j=0;j<2;j++){
				for(int k=0;k<2;k++){
					ans = a;
					if(i==0){
						ans += b;
					}
					else{
						ans -= b;
					}
					if(j==0){
						ans += c;
					}
					else{
						ans -= c;
					}
					if(k==0){
						ans += x;
					}
					else{
						ans -= x;
					}
					if(ans == 7){
						count[0] = i;
						count[1] = j;
						count[2] = k;
					}
				}
			}
		}
		for(int i=0;i<4;i++){
			System.out.print(z/(int)Math.pow(10,3-i));
			z -= z/(int)Math.pow(10,3-i)*(int)Math.pow(10,3-i);
			if(i!=3){
				if(count[i]==0){
					System.out.print("+");
				}
				else{
					System.out.print("-");
				}
			}
		}
		System.out.println("=7");

	}

}
