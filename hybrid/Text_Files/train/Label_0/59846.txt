import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int a=in.nextInt();
		int b=in.nextInt();
		int winA=0,winB=0,draw=0;
		
		if(a==b){
				draw=6;
				winA=0;
				winB=0;
		}
		
		if(a>b){
			if((a+b)%2==1){
			  
			  draw=0;
			}
			else{
				
				draw=1;
			}
			winA=(6-(a+b)/2);
			winB=6-winA-draw;
		}
		if(a<b){
		   if((a+b)%2==1){
			winA=((a+b)/2-1+1);
			draw=0;
		   }
		   else{
			   winA=(a+b)/2-1;
			   draw=1;
		   }
			winB=6-winA-draw;
		}
		System.out.println(winA+" "+draw+" "+winB);
	}
}
