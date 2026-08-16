import java.util.*;
public class Main{
    public static void main(String[]args){
        
        Scanner sc=new Scanner(System.in);
		//System.out.println("s");
		int s=sc.nextInt();
		int v1=sc.nextInt();
		int v2=sc.nextInt();
		int t1=sc.nextInt();
		int t2=sc.nextInt();
		int val1=(s*v1)+2*t1;
		int val2=(s*v2)+2*t2;
		String result="Friendship";
		if(val1<val2){
			result="First";
		}else if(val2<val1){
			result="Second";
		}
       System.out.println(result);
        
        
        
    }}