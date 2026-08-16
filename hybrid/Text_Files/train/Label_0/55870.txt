import java.util.*;
import java.lang.*;
  
public class Main{
  public static void main(String[] args){
    Scanner stdIn=new Scanner(System.in);
    int i,n,x;
    n=stdIn.nextInt();
    long max=-133333333,min=133333333,sum=0;
    for (i=0;i<n;i++){
	x=stdIn.nextInt();
	sum+=x;
	if (x>max){
	    max=x;
	}
	if (x<min){
	    min=x;
	}
    }
    System.out.println(min+" "+max+" "+sum);
  }
}

