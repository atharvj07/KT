import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    
    long n = scan.nextLong();
    long k = scan.nextLong();
    
    long res = n % k;
    
    System.out.println(Math.min(Math.abs(res-k),res));
  } 
}