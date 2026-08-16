import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = Integer.parseInt(sc.nextLine());
    String[] S = sc.nextLine().split(" ");
    int[] nums = new int[N];
    int sum = 0;
    for(int i = 0; i < N; i++){
      nums[i] = Integer.parseInt(S[i]);
      sum += nums[i];
    }
    
    int ans = 0;
    double d = (double)sum/N;
    int ave = (int)Math.round(d);
    for(int i = 0; i < N; i++){
      ans += (int)Math.pow(nums[i]-ave, 2);
    }
    System.out.println(ans);
  }
}
