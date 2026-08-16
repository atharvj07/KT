import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    long a=sc.nextLong(),b=sc.nextLong(),c=sc.nextLong(),k=sc.nextLong();
    long res=0;
    if(k<=a) {
    	System.out.println(k);
    }else if(k<=a+b){
    	System.out.println(a);
    }else {
    	System.out.println(a-(k-a-b));
    }
  }
}
