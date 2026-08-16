import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] member = new int[n];
        for(int i = 0;i < n-1;i++){
            int num = sc.nextInt();
            member[num-1]++;
        }
        for(int ans:member)
            System.out.println(ans);
    }
}