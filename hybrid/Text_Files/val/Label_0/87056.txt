import java.io.*;
import java.util.*;

public final class Test {
	static void rec(String s,int n){
		if(n==1){
			System.out.println(s);
			return ;
		}
		rec(s.substring(0,n-1)+" "+s.substring(n-1),n-1);
		rec(s,n-1);
		 
	}
	
	
	public static void main(String...args) throws Exception{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
		int a=0,b=0,s1=0,s2=0,nSize=n;
		while(n>0){
			int value=(int)Math.pow(2,n);
			n--;
			if(a<b){
				if(s1<nSize/2){
					a+=value;
					s1++;
				}
				else{
					b+=value;
					s2++;
				}
			}
			else{
				if(s2<nSize/2){
					b+=value;
					s2++;
					
				}
				else{
					a+=value;
					s1++;
				}
			}
		}
		System.out.println(Math.abs(a-b));
		}
		
	}
	
}