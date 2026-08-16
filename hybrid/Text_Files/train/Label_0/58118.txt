import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
      int A = sc.nextInt();
      int B = sc.nextInt();
      int C = sc.nextInt();
      int[] E = new int[]{A,B,C};
      Arrays.sort(E);
      
      System.out.println(E[2]*10+E[1]+E[0]);
    }
}