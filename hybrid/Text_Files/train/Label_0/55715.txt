import java.util.*;

public class Main {
    static Dish[] dishes;
    static int[][] dp;
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int t = sc.nextInt();
		dishes = new Dish[n];
		dp = new int[n][t + 1];
		for (int i = 0; i < n; i++) {
		    dishes[i] = new Dish(sc.nextInt(), sc.nextInt());
		}
		Arrays.sort(dishes);
		System.out.println(dfw(n - 1, t));
   }
   
   static int dfw(int idx, int time) {
       if (idx < 0) {
           return 0;
       }
       if (time <= 0) {
           return 0;
       }
       if (dp[idx][time] == 0) {
           dp[idx][time] = Math.max(dfw(idx - 1, time), dfw(idx - 1, time - dishes[idx].time) + dishes[idx].taste);
       }
       return dp[idx][time];
   }
   
   static class Dish implements Comparable<Dish> {
       int time;
       int taste;
       
       public Dish(int time, int taste) {
           this.time = time;
           this.taste = taste;
       }
       
       public int compareTo(Dish another) {
           return another.time - time;
       }
   }
}
