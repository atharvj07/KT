import java.util.Scanner;

public class Main{
 public static void main(String[] args){
  Scanner sc = new Scanner(System.in);
  int sheep = sc.nextInt(), wolf=sc.nextInt();
  if(wolf>=sheep) System.out.println("unsafe");
  else System.out.println("safe");
 }
}
		