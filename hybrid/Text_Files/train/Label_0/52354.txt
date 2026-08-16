import java.util.*;

public class Main{
    public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int a = sc.nextInt();
	int b = sc.nextInt();
	int c = sc.nextInt();
	int count=0,point=0;
	while(point < c){
	    count++;
	    if(count%7==0){
		point+=b;
	    }
	    point+=a;
	}
	System.out.println(count);
    }
}
