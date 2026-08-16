import java.util.Scanner;
	import java.util.*;
	
	public class Main{
		
		public static void main(String[] args) {
			
			Scanner sc=new Scanner(System.in);
			
		while(true){int n=sc.nextInt();if(n==0){break;}
		int N[]=new int[n+1];
		
		for(int i=0;i<n+1;i++){N[i]=sc.nextInt();}
		
		bi:for(int i=0;i<n+1;i++){
			List<Integer>tousa=new ArrayList<Integer>();
		for(int p=0;p<n+1;p++){
			tousa.add(N[p]);}
		tousa.remove(i);
			for(int p=0;p<n-2;p++){
				if(tousa.get(p)-tousa.get(p+1)!=tousa.get(p+1)-tousa.get(p+2)){continue bi;}
			}System.out.println(N[i]);break;
		
		}}}}
		
		
		
		
		
		
		
		